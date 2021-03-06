from rest_framework import serializers
from main.models import CustomUser
from .organization import OrgSerializer


class UserSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	username = serializers.CharField()
	orgranization = OrgSerializer()

	class Meta:
		model = CustomUser