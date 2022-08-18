
from urllib import response
from django.views.generic import CreateView
from .models import File

from django.shortcuts import render
from .scripts import file_handler

from .forms import FileForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.exceptions import ParseError
# Create your views here.
from .serializers import FileSerializers
from rest_framework import status


from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import FileSerializers
# 
class FileAPIView(ViewSet):
    serializer_class = FileSerializers
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        return Response("GET API")

    def create(self, request):

        file_uploaded = request.FILES['document']
        file = (file_uploaded)
        data = file_handler(file)
        context = {
            "data":data
        }
        response = context
        return Response(response)

def form_view(request):
    if request.method =='POST':
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES['document']
            
            data = file_handler(file)
            context = {
                "data":data
            }
            
            form.save()
            

        else:
            print("Not a valid form")

        
        #print(request.POST)
        return render(request,'entities.html',context)

    else:
        form = FileForm()
        return render(request,'form.html',{'form':form})
        
    
    