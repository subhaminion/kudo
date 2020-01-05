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
	save_kudo
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
				"error": "Please provide both username and password"
			}, status=HTTP_400_BAD_REQUEST)

		user = authenticate(username=username, password=password)
		if not user:
			return Response({
				"error": "Invalid Credentials"
			}, status=HTTP_404_NOT_FOUND)
		
		token, _ = Token.objects.get_or_create(user=user)
		return Response({
			"token": token.key
		}, status=HTTP_200_OK)


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

	def create(self, request):
		queryset = save_kudo(request)
		serializer = KudosSerializer(queryset)
		return Response(serializer.data)


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