from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer
from .models import UserData

# Create your views here.
class UserEndPoint(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # Check if email exists and say email already exists
        if UserData.objects.filter(Email = request.data["Email"]).exists():
            return Response({"message": "Email already exists!", "status": 101})
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully", "status": 201})