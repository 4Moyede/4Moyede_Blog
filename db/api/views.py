from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from datetime import datetime

from api.models import Introduce, Projects, TechStack
from api.serializers import IntroduceSerializer, ProjectsSerializer, TechStackSerializer


class GetData(APIView):
    def get(self, request, format=None):
        response = {}
        
        introduceQuery = Introduce.objects.all()
        response['introduce'] = IntroduceSerializer(introduceQuery, many=True).data
        projectsQuery = Projects.objects.all()
        response['projects'] = ProjectsSerializer(projectsQuery, many=True).data
        techstackQuery = TechStack.objects.all()
        response['techstack'] = TechStackSerializer(techstackQuery, many=True).data

        print("[ Request Data ]", datetime.now(), "HTTP_200_OK")
        
        return Response(response, status=status.HTTP_200_OK)
        