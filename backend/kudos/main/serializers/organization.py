from rest_framework import serializers
from main.models import Organization, CustomUser
from .orguser import OrgUserSerializer

class OrgSerializer(serializers.Serializer):
	name = serializers.CharField()
	members = OrgUserSerializer(many=True)

	class Meta:
		model = CustomUser
