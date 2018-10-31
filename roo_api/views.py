from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from student.models import UserProfile

from roo_api.serializers import UserSerializer


class Users(APIView):

    def get(self, request):
        users = UserProfile.objects.all()
        serializaer = UserSerializer(users, many=True)
        return Response(serializaer.data)