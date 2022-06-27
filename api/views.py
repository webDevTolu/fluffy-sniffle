from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework import serializers
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def index(request):
    apiUrls = {
        'List': '/projects/',
        'Detail': '/project/<str:pk>/',
        'Create': '/project/create/',
        'Update': '/project/<str:pk>/update',
        'Delete': '/project/<str:pk>/delete',
    }
    return Response(apiUrls)


@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def project_detail(request, pk):
    try:
        project = Project.objects.get(id=pk)
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data)
    except Project.DoesNotExist:
        message = {'error': 'Project with id {} does not exist'.format(pk)}
        return Response(message, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def project_create(request):
    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def project_update(request, pk):
    project = Project.objects.get(id=pk)
    serializer = ProjectSerializer(instance=project, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def project_delete(request, pk):
    try:
        project = Project.objects.get(id=pk)
        project.delete()
        return Response('Project Deleted Successfully')
    except Project.DoesNotExist:
        message = {'error': 'Project with id {} does not exist'.format(pk)}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)
    
