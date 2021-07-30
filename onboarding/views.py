from copy import error
import re
from django.core.checks import messages
from django.http import response
from django.http.response import HttpResponse
from onboarding.models import MyUser, Product_description, User_details,User_role
from onboarding.serializers import User_details_Serializer, User_role_serializer,Product_description_Serializer, RegisterSerializer,UserBookingDetailSerializer, UserBookingSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class User_details_list(APIView):
    def post(self, request, format=None):
        email_id = request.data['email_id']
        print(email_id)

       
        try:
               
            if User_details.objects.get(email_id=email_id):
            
                return Response({'message': 'user is already exist'})
        except User_details.DoesNotExist:
            import pprint
            pprint.pprint(request.data)
            
            
            serializer = User_details_Serializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
           
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Get_user_details(APIView):
    def post(self, request, format=None):
        
        email_id = request.data['email_id']
        
        print(email_id)
        try:
            user = User_details.objects.get(email_id=email_id)
            serializer = User_details_Serializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except User_details.DoesNotExist:
            return Response({'message': 'user is not exists'})

class User_delete(APIView):
    def post(self, request, format=None):
        email_id = request.data['email_id']

        try:
            user = User_details.objects.get(email_id=email_id)  
            user.delete()
            return Response({'message': 'user is deleted'})
        except User_details.DoesNotExist:
            return Response({'message': 'user is not exists'})

class Get_User_role(APIView):
    def post(self, request, format=None):
        role = request.data['role'].capitalize()
        print(role)
        try:
            user = User_role.objects.get(role = role)
            return Response({'message': 'This role is already exist'})
        except:
            User_role.objects.create(role = role)
            return Response({'message': 'This new role is saved'})


class Get_user(APIView):
    def get(self, request, format=None):
        user = User_role.objects.all()
        serializer = User_role_serializer(user, many=True)
        return Response(serializer.data)


class Products_detail(APIView):
    def post(self, request, format=None):
        serializer = Product_description_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, format=None):
        user = Product_description.objects.all()
        serializer = Product_description_Serializer(user, many=True)
        return Response(serializer.data)


class Get_detail_by_id(APIView):
    def post(self, request, format=None):
        id = request.data['id']
        try:
            user = Product_description.objects.get(id=id)
            serializer = Product_description_Serializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Product_description.DoesNotExist:
            return Response({'message':"id is not exist"})

class User_register(APIView):
    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class User_login(APIView):
    def post(self, request, format=None):
        print(request)
        email = request.data['email']
        password = request.data['password']

        try:
            user = MyUser.objects.get(email=email)
            if user.check_password(password):     
                serializer = RegisterSerializer(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except MyUser.DoesNotExist:
            return Response({"message":"Invalid credentials"})


class User_details_get_by_id(APIView):
    def get(self, request, format=None):
        id = request.data['id']
        user = MyUser.objects.get(id=id)
        serializer = RegisterSerializer(user)
        return Response(serializer.data)


class UserBookingRegister(APIView):
    def post(self, request, format=None):
        serializer = UserBookingDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserBookingLogin(APIView):
    def get(self, request, format=None):
        id = request.data['id']
        user =  MyUser.objects.get(id=id)
        serializer =  UserBookingSerializer(user)
        return Response(serializer.data)


        
        











        





