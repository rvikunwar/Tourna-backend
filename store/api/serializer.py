from rest_framework import serializers
from store.models import Tournament, Contact
from django.contrib.auth import get_user_model



class TournamentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Tournament
        fields=['name','date_time','description','timeline','submission','rules','registration','contact','amount','id','prize','open_closed','link']

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model=Contact
        fields=['name','email','phone_no','message']