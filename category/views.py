from django.shortcuts import render
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from .models import category 
from .serializers import categorySerializer 

# Create your views here.
class allcategoryview(APIView):
    
    def get(self,request):
        category_objs=category.objects.all()
        data=categorySerializer(category_objs,many=True).data
        return Response(data,status=status.HTTP_200_OK)


class grandfather_category_view(APIView):
    
    def get(self,request):
        category_objs=category.objects.filter(parent=None)
        data=categorySerializer(category_objs,many=True).data
        return Response(data,status=status.HTTP_200_OK)

class fatherandchild_category_view(APIView):
    
    def get(self,request,id):
        category_objs=category.objects.filter(parent=id)
        data=categorySerializer(category_objs,many=True).data
        return Response(data,status=status.HTTP_200_OK)

class createcategory(APIView):

    def post(self,request):
        data=request.data
        try:
            data._mutable=True
        except Exception as e:
            pass
        if not request.data.get('parent'):  
            data['parent']=None
        serializer=categorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_206_PARTIAL_CONTENT)