from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required 
from rest_framework.decorators import api_view
from uritemplate import partial
from .serializers import *
from .serializers import *
from . models import *
from .filters import *
from django.contrib.auth.models import User

# Create your views here.


@api_view(['GET'])
def MessagesView(request):
   
    queryset = Message.objects.all()
    filterset = MessageFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = MessageSerializer(queryset, many=True)
    
    return Response(serializer.data)




@api_view(['GET'])
def UserList(request):
    
    queryset = User.objects.all()
    filterset = UserFilter(request.GET, queryset=queryset)
    if filterset.is_valid():
         queryset = filterset.qs
    serializer = UserSerializer(queryset, many=True)
    
    return Response(serializer.data)




@api_view(['POST'])
def MessagesCreate(request):
    #if request.user.is_landlord == True:

        if request.method == "POST":

            serializer = MessageSerializer(data=request.data)
            
        if serializer.is_valid():
                
            serializer.save()

        return Response(serializer.data)