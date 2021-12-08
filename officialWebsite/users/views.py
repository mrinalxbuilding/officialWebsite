from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from officialWebsite.users.models import User
from officialWebsite.users.serializers import UserSerializer


class LeadListView(APIView):
    """List all leads"""

    def get(self, request, format=None):
        leads = User.objects.all().filter(role__iexact="Lead")
        serializer = UserSerializer(leads, many=True)
        return Response(serializer.data)


class CoLeadListView(APIView):
    """List all leads"""

    def get(self, request, format=None):
        leads = User.objects.all().filter(role__icontains="Co-Lead")
        serializer = UserSerializer(leads, many=True)
        return Response(serializer.data)


class UserViewset(generics.ListAPIView):
    """Manage members in the database"""

    serializer_class = UserSerializer
    queryset = User.objects.all().filter(role__icontains="Core")