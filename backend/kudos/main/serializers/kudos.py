from rest_framework import serializers
from main.models import Kudos
from .user import UserSerializer

class KudosSerializer(serializers.Serializer):
	kudos_header = serializers.CharField()
	kudos_message = serializers.CharField()
	from_user = UserSerializer()
	to_user = UserSerializer()

	class Meta:
		model = Kudos