from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RecordSerializer
from website.models import Record

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
		'List':'/record-list/',
		'Detail View':'/record-detail/<str:pk>/',
		'Create':'/record-create/',
		'Update':'/record-update/<str:pk>/',
		'Delete':'/record-delete/<str:pk>/',
		}
    return Response(api_urls)

# Serializers allow us to return any model object here, a json response.. its just gonna be a json obj

@api_view(['GET'])
def recordList(request):
    records = Record.objects.all().order_by('-id')
    serializer = RecordSerializer(records, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def recordDetail(request, pk):
    records = Record.objects.get(id=pk)
    serializer = RecordSerializer(records, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def recordCreate(request):
    serializer = RecordSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def recordUpdate(request, pk):
    record = Record.objects.get(id=pk)
    serializer = RecordSerializer(instance=record, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def recordDelete(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    
    return Response('Item successfully deleted!')
