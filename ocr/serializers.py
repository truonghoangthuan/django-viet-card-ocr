from rest_framework import serializers
from .models import *

class IDCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDCard
        fields = [
            "image", 
            "id_card_number", 
            "name", "dob", 
            "nationality", 
            "sex", 
            "hometown", 
            "address", 
            "expires", 
        ]