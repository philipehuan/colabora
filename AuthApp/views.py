from django.contrib.auth.models import User

# Create your views here.
from pytz import unicode
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from AuthApp.serializers import UserSerializer


class GetUserView(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args,**kwargs):

        #queryset = User.objects.all().filter(username=request.user)
        #serializer = UserSerializer(queryset=queryset ,many=True)

        content ={
            'user': unicode(request.user),
            'groups':unicode(request.user.get_group_permissions()),
            'permissions':unicode(request.user.get_all_permissions())
        }
        return Response(content)