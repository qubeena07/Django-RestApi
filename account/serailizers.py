from rest_framework import serializers
from account.models import User

class UserRegistratorSerializer(serializers.ModelSerializer):
    password2 =serializers.CharField(style={
        'input_type': 'password'
    },
    write_only=True)
    class Meta:
        model = User
        fields = ['email','fullname','address','phonenumber' ,'password','password2','is_subscribed' ]
        extra_kwargs = {
            'password':{'write_only':True}
        }
    #validate password and password
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            return serializers.ValidationError("Password does not match")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2', None)
        return User.objects.create(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        max_length=255
    )
    class Meta:
        model = User
        fields = ['email','password']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','fullname','address','phonenumber','is_subscribed' ]
