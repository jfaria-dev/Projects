from _auth.models import UserAuth
from _api.serializers import UserSerializer
from rest_framework import serializers

class UserAuthSerializer(serializers.ModelSerializer):
    information = serializers.SerializerMethodField()
    
    class Meta:
        model = UserAuth
        fields = '__all__'
        
    def get_information(self, obj):
        if obj.user_client:  # Check for child categories
            return UserSerializer(obj.user_client).data
        return None