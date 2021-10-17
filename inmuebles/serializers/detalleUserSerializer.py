from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class DetalleUserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        #fields = ['is_host']
        fields = '__all__'

