# from django.contrib.auth.models import User
# from rest_framework import serializers
# from django.contrib.auth import get_user_model


# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'email', 'password', 'name')

# # 패스워드가 필요없는 다른 테이블에서 사용할 용도
# class UserInfoSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'email', 'name')
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    Department = serializers.CharField()
    StudentID = serializers.CharField()

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'Department': self.validated_data.get('Departent', ''),
            'StudentID': self.validated_data.get('StudentID', '')
        }