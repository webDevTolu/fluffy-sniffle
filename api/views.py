from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def index(request):
    apiUrls = {
        'project-list': '/projects/',
    }
    return Response(apiUrls)
