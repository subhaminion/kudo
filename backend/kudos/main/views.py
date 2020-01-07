from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
	HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND,
	HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from main.dbapi import (
	get_all_users, get_user,
	get_all_kudos_by_user, get_kudos,
	save_kudo, check_organization
)

from main.serializers import (
	UserSerializer, KudosSerializer
)

class LoginView(APIView):
	permission_classes = (AllowAny, )
	def post(self, request, format=None):
		data = request.data

		username = data.get('username', None)
		password = data.get('password', None)

		print(username, password)

		if username is None or password is None:
			return Response({
				"msg": "Please provide both username and password"
			}, status=HTTP_400_BAD_REQUEST)

		user = authenticate(username=username, password=password)
		if not user:
			return Response({
				"msg": "Invalid Credentials"
			}, status=HTTP_404_NOT_FOUND)
		
		token, _ = Token.objects.get_or_create(user=user)
		return Response({
			"token": token.key
		}, status=HTTP_200_OK)


class MeView(viewsets.ViewSet):
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticated, )
	authentication_classes = (TokenAuthentication, )

	def list(self, request):
		queryset = get_user(request.user.id)
		serializer = UserSerializer(queryset, many=True)
		return Response(serializer.data)


class UserView(viewsets.ViewSet):
	serializer_class = UserSerializer
	permission_classes = (IsAuthenticated, )
	authentication_classes = (TokenAuthentication, )

	def list(self, request):
		queryset = get_all_users()
		serializer = UserSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk):
		queryset = get_user(pk)
		serializer = UserSerializer(queryset, many=True)
		return Response(serializer.data)

class KudosView(viewsets.ViewSet):
	serializer_class = KudosSerializer
	permission_classes = (IsAuthenticated, )
	authentication_classes = (TokenAuthentication, )

	def list(self, request):
		queryset = get_all_kudos_by_user(None, request.user)
		serializer = KudosSerializer(queryset, many=True)
		return Response(serializer.data)

	def create(self, request):
		if request.user.kudos_count < 1:
			return Response({'msg': "you ran out of kudos to give :3"}, status=HTTP_400_BAD_REQUEST)

		if str(request.user.id) == str(request.data.get('to_user')):
			return Response({'msg': "you cant give kudo to yourself -_-"}, status=HTTP_400_BAD_REQUEST)

		if not check_organization(request.user.id, request.data.get('to_user')):
			return Response({'msg': "Can't be given to people in other ORG."}, status=HTTP_200_OK)

		queryset = save_kudo(request)
		serializer = KudosSerializer(queryset)
		return Response({'msg': 'Successfully sent!'}, status=HTTP_200_OK)


class UserKudosView(viewsets.ViewSet):
	serializer_class = KudosSerializer
	permission_classes = (IsAuthenticated, )
	authentication_classes = (TokenAuthentication, )

	def list(self, request, user_pk):
		user_pk = self.kwargs.get('user_pk')
		queryset = get_all_kudos_by_user(user_pk)
		serializer = KudosSerializer(queryset, many=True)
		return Response(serializer.data)

	def retrieve(self, request, user_pk, pk):
		queryset = get_kudos(pk)
		serializer = KudosSerializer(queryset, many=True)
		return Response(serializer.data)