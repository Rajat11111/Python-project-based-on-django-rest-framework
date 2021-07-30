from django.db.models import fields
from rest_framework import serializers
from onboarding.models import Product_description, User_details, User_role, MyUser, NewUserDetails
import django.contrib.auth.password_validation as validators


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):

    profile_pic = serializers.ImageField(max_length=None, use_url=True)


    class Meta:
        model = MyUser
        fields = ['id','email', 'first_name', 'last_name', 'contact', 'address', 'password', 'profile_pic']
        extra_kwargs = {'password': {'write_only': True}}


class UserBookingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id','email', 'first_name', 'last_name', 'contact', 'address', 'password', 'profile_pic', 'city_name', 'ticket', 'date_of_booking', 'date_of_onboarding', 'date_of_returning']
        extra_kwargs = {'password': {'write_only': True}}

   

class UserBookingSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField()
    class Meta:
        model = MyUser
        fields = ['id', 'first_name','details']

    def get_details(self, obj):
        details = {"city_name":obj.city_name,
                   "ticket" : obj.ticket,
                   "date_of_booking" : obj.date_of_booking,
                   "date_of_onboarding":obj.date_of_onboarding,
                   "date_of_returning" : obj.date_of_returning}
        return details

    


        


    def validate(self, data):
        
        user = MyUser(**data)

         
        password = data.get('password')

        errors = dict() 
        try:
            validators.validate_password(password=password, user=MyUser)

        
        except serializers.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(RegisterSerializer, self).validate(data)


    

    def create(self, validated_data):
        user = MyUser.objects.create_user(validated_data['email'], validated_data['first_name'], validated_data['last_name'], validated_data['contact'], validated_data['address'], validated_data['password'], validated_data['profile_pic'], validated_data['city_name'], validated_data['ticket'], validated_data['date_of_booking'], validated_data['date_of_onboarding'], validated_data['date_of_returning'])
        return user


    


    



class User_role_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_role
        fields = "__all__"


    def create(self, validated_data):
        return User_role.objects.create(**validated_data)





class User_details_Serializer(serializers.ModelSerializer):
    jobs_role = User_role_serializer()
    class Meta:
        model = User_details
        fields = "__all__"
        


    def create(self, validated_data):
        return User_details.objects.create(**validated_data)


class Product_description_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_description
        fields = "__all__"

    def create(self, validated_data):
        return Product_description.objects.create(**validated_data)




    