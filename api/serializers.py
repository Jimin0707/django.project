from rest_framework import serializers

from .models import project,client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=client
        fields=['id','projects','user']


class ProjectSerializer(serializers.ModelSerializer):


    class Meta:
        model = project
        fields = ['id','client_name','created_at','created_by']

