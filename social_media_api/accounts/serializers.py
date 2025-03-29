from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()
#start task 0
class UsersRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'bio', 'username', 'profile_picture']
        extra_kwargs = {
            'password': {'minimum_length': 8},
            'password2': {'minimum_length': 8},
            'email': {'required': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio',''),
            profile_picture=validated_data.get('profile_picture', None),
        
            )
        return user
    


class UsersLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if user is None:
                raise AuthenticationFailed('Invalid credentials.')
            data['user'] = user
        else:
            raise serializers.ValidationError('Must include username and password.')
        return data

class AuthTokenSerializer(serializers.Serializer):
    token = serializers.CharField(read_only=True)

#end task 0


#start task 1
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture'] 

#end task 1

#start task 2
class FollowSerializer(serializers.Serializer):
    user_id_to_follow = serializers.IntegerField(min_value=1)
#end task 2