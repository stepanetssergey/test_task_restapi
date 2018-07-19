from rest_framework.serializers import ModelSerializer
from . import models


class UserAPISerializer(ModelSerializer):
    """User's serializer for API"""
    class Meta:
        model = models.UserAPI
        fields = ("id","name","lastname","email","password",)
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, data):
        """Create new user from API"""

        user = models.UserAPI(
            email = data['email'],
            name = data['name'],
            lastname = data['lastname']
        )
        user.set_password(data['password'])
        user.save()
        return user
