from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mascota
from .serializers import MascotaSerializer
# Create your views here.
class MascotaView(APIView):
    def get(self,request):
        mascota=Mascota.objects.all()
        serializer=MascotaSerializer(mascota,many=True)
        return Response(serializer.data)