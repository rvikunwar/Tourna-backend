from django.shortcuts import render
from django.http import HttpResponse
from .serializer import TournamentSerializer,ContactSerializer
from store.models import Tournament
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from rest_framework.response import Response

from rest_framework.parsers import JSONParser 


class TournamentsView(ListAPIView):
    serializer_class=TournamentSerializer
    def get_queryset(self):
        queryset=Tournament.objects.all()
        return queryset

    def list(self, request):
        
        queryset = self.get_queryset()
        serializer = TournamentSerializer(queryset, many=True)
        
        return Response(serializer.data)




class TournamentView(RetrieveAPIView):
    serializer_class=TournamentSerializer
    queryset=Tournament.objects.all()
    


class ContactView(CreateAPIView):
    serializer_class=ContactSerializer
    
       