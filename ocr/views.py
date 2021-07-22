from django.conf import settings
from django.shortcuts import render, redirect
import os

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .forms import *
from .main import *


# Create your views here.
# View to handle api of ID card.
class IDCardAPIView(APIView):
    # API for GET method.
    def get(self):
        idcard = IDCard.objects.last()
        getData = GetIDCardSerializer(idcard, many=False)
        return Response(getData.data)

    # API for POST method.
    def post(self, request):
        postData = PostIDCardSerializer(request.data)

        # Get the upload image.
        image = postData.data["image"]
        # Insert the upload image to database.
        card = IDCard.objects.create(
            image=image,
        )

        # Get upload image name.
        image = request.FILES["image"]
        # Get upload image path
        path = settings.MEDIA_ROOT + "\images\id-card\\" + image.name
        # Pass upload image path to ocr function
        res = extract(path)
        # Get result from ocr function and save to the fields of IdCard database.
        card.id_card_number = str(res.get("ID"))
        card.name = str(res.get("Name"))
        card.dob = str(res.get("DOB"))
        card.nationality = str(res.get("Nationality"))
        card.sex = str(res.get("Sex"))
        card.hometown = str(res.get("Hometown"))
        card.address = str(res.get("Address"))
        card.expires = str(res.get("Expires"))
        card.save()

        # Get the latest upload image in database.
        idcard = IDCard.objects.last()
        # Convert image information to JSON and return the JSON format.
        getData = GetIDCardSerializer(idcard, many=False)
        return Response(getData.data)


# View to handle upload id card images.
def base(request):
    if request.method == "POST":
        form = IdCardForm(request.POST, request.FILES)
        if form.is_valid():
            # Get uploading image to save to database.
            save_result = IDCard.objects.create(image=form.cleaned_data.get("image"))

            # Get upload image name
            image = request.FILES["image"]
            # Get upload image path
            path = settings.MEDIA_ROOT + "\images\id-card\\" + image.name
            # Pass upload image path to ocr function
            res = extract(path)

            # Get result from ocr function and save to the fields of IdCard database.
            save_result.id_card_number = str(res.get("ID"))
            save_result.name = str(res.get("Name"))
            save_result.dob = str(res.get("DOB"))
            save_result.nationality = str(res.get("Nationality"))
            save_result.sex = str(res.get("Sex"))
            save_result.hometown = str(res.get("Hometown"))
            save_result.address = str(res.get("Address"))
            save_result.expires = str(res.get("Expires"))
            save_result.save()

            return redirect("home")

    form = IdCardForm()
    result = IDCard.objects.last()
    IDCard.objects.all().delete()

    context = {
        "form": form,
        "result": result,
    }

    directory = settings.MEDIA_ROOT + "\images\id-card\\"
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))

    return render(request, "CMND.html", context)


# View to handle student card upload images.
def student_card_page(request):
    if request.method == "POST":
        form = StudentCardForm(request.POST, request.FILES)
        if form.is_valid():
            # Get uploading image to save to database.
            save_result = Student_Card.objects.create(
                image=form.cleaned_data.get("image")
            )

            # Get upload image name
            image = request.FILES["image"]
            # Get upload image path
            path = settings.MEDIA_ROOT + "\images\student-card\\" + image.name
            # Pass upload image path to ocr function
            res = extract(path)

            # Get result from ocr function and save to the fields of Student_Card database.
            save_result.student_card_number = str(res.get("ID"))
            save_result.name = str(res.get("Name"))
            save_result.major = str(res.get("Major"))
            save_result.falculty = str(res.get("Falculty"))
            save_result.course = str(res.get("Course"))

            save_result.save()

            return redirect("tsv")

    form = StudentCardForm()
    result = Student_Card.objects.last()
    Student_Card.objects.all().delete()
    context = {
        "form": form,
        "result": result,
    }

    directory = settings.MEDIA_ROOT + "\images\student-card\\"
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))

    return render(request, "TSV.html", context)


# View to handle driving license upload images.
def driving_license_page(request):
    if request.method == "POST":
        form = DrivingLicenseCardForm(request.POST, request.FILES)
        if form.is_valid():
            # Get uploading image to save to database.
            save_result = Driving_License_Card.objects.create(
                image=form.cleaned_data.get("image")
            )

            # Get upload image name
            image = request.FILES["image"]
            # Get upload image path
            path = settings.MEDIA_ROOT + "\images\driving-license\\" + image.name
            # Pass upload image path to ocr function
            res = extract(path)

            # Get result from ocr function and save to the fields of Student_Card database.
            save_result.driving_license_number = str(res.get("ID"))
            save_result.name = str(res.get("Name"))
            save_result.dob = str(res.get("DOB"))
            save_result.nationality = str(res.get("Nationality"))
            save_result.address = str(res.get("Address"))
            save_result.card_class = str(res.get("Class"))
            save_result.expires = str(res.get("Expires"))

            save_result.save()

            return redirect("gplx")

    form = DrivingLicenseCardForm()
    result = Driving_License_Card.objects.last()
    Driving_License_Card.objects.all().delete()
    context = {
        "form": form,
        "result": result,
    }

    directory = settings.MEDIA_ROOT + "\images\driving-license\\"
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))

    return render(request, "GPLX.html", context)
