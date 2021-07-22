from rest_framework import serializers
from .models import *


# Serializer of GET method for ID card.
class GetIDCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDCard
        fields = [
            "id_card_number", 
            "name", "dob", 
            "nationality", 
            "sex", 
            "hometown", 
            "address", 
            "expires", 
        ]

# Serializer of POST method for ID card.
class PostIDCardSerializer(serializers.Serializer):
    image = serializers.ImageField()