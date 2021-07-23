from rest_framework import serializers
from .models import *


# Serializer of GET method for IDCard.
class GetIDCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = IDCard
        fields = [
            "id_card_number",
            "name",
            "dob",
            "nationality",
            "sex",
            "hometown",
            "address",
            "expires",
        ]


# Serializer of GET method for StudentCard.
class GetStudentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Card
        fields = [
            "student_card_number",
            "name",
            "major",
            "falculty",
            "course",
        ]


# Serializer of GET method for DrivingLicense.
class GetDrivingLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driving_License_Card
        fields = [
            "driving_license_number",
            "name",
            "dob",
            "nationality",
            "address",
            "card_class",
            "expires",
        ]


# Serializer of POST method for all card.
class PostCardSerializer(serializers.Serializer):
    image = serializers.ImageField()
