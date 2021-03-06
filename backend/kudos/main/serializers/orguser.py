from rest_framework import serializers
from main.models import CustomUser

class OrgUserSerializer(serializers.Serializer):
	id = serializers.ReadOnlyField()
	username = serializers.CharField()

	class Meta:
		model = CustomUser