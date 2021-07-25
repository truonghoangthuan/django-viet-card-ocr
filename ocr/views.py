import os

from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from .forms import *
from .main import *
from .serializers import *


# Create your views here.
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

    # Get the input form for IDCard.
    form = IdCardForm()
    # Get the latest upload image in database.
    result = IDCard.objects.last()
    # Delete all previous data to prevent from auto load last image information on start.
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

    # Get the input form for StudentCard.
    form = StudentCardForm()
    # Get the latest upload image in database.
    result = Student_Card.objects.last()
    # Delete all previous data to prevent from auto load last image information on start.
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

    # Get the input form for DrivingLicense.
    form = DrivingLicenseCardForm()
    # Get the latest upload image in database.
    result = Driving_License_Card.objects.last()
    # Delete all previous data to prevent from auto load last image information on start.
    Driving_License_Card.objects.all().delete()

    context = {
        "form": form,
        "result": result,
    }

    directory = settings.MEDIA_ROOT + "\images\driving-license\\"
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))

    return render(request, "GPLX.html", context)


# View to handle api of IDCard.
class IDCardAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    # API for GET method.
    def get(self, request, *args, **kwargs):
        idcard = IDCard.objects.last()
        get_data = GetIDCardSerializer(idcard, many=False)
        return Response(get_data.data)

    # API for POST method.
    def post(self, request, *args, **kwargs):
        # post_data = PostCardSerializer(data=request.data)
        post_data = request.data['image']
        print("\n==============\n" + post_data + "\n==============\n")

        # Get the upload image.
        # if post_data.is_valid():
        #     post_image = request.data.get("image")
        # Insert the upload image to database.
        card = IDCard.objects.create(
            image=post_data,
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
        # Delete all previous data to prevent from auto load last image information on start.
        IDCard.objects.all().delete()
        # Convert image information to JSON and return the JSON format.
        get_data = GetIDCardSerializer(idcard, many=False)

        directory = settings.MEDIA_ROOT + "\images\id-card\\"
        for f in os.listdir(directory):
            os.remove(os.path.join(directory, f))

        return Response(get_data.data)


# View to handle api of StudentCard.
class StudentCardAPIView(APIView):
    # API for GET method.
    def get(self):
        student_card = Student_Card.objects.last()
        get_data = GetStudentCardSerializer(student_card, many=False)
        return Response(get_data.data)

    # API for POST method.
    def post(self, request):
        post_data = PostCardSerializer(data=request.data)

        # Get the upload image.
        if post_data.is_valid():
            post_image = request.data.get("image")
        # Insert the upload image to database.
        card = Student_Card.objects.create(
            image=post_image,
        )

        # Get upload image name.
        image = request.FILES["image"]
        # Get upload image path
        path = settings.MEDIA_ROOT + "\images\student-card\\" + image.name
        # Pass upload image path to ocr function
        res = extract(path)

        # Get result from ocr function and save to the fields of Student_Card database.
        card.student_card_number = str(res.get("ID"))
        card.name = str(res.get("Name"))
        card.major = str(res.get("Major"))
        card.falculty = str(res.get("Falculty"))
        card.course = str(res.get("Course"))
        card.save()

        # Get the latest upload image in database.
        student_card = Student_Card.objects.last()
        # Delete all previous data to prevent from auto load last image information on start.
        Student_Card.objects.all().delete()
        # Convert image information to JSON and return the JSON format.
        get_data = GetStudentCardSerializer(student_card, many=False)

        directory = settings.MEDIA_ROOT + "\images\student-card\\"
        for f in os.listdir(directory):
            os.remove(os.path.join(directory, f))

        return Response(get_data.data)


# View to handle api of DrivingLicense.
class DrivingLicenseAPIView(APIView):
    # API for GET method.
    def get(self):
        driving_license = Driving_License_Card.objects.last()
        get_data = GetDrivingLicenseSerializer(driving_license, many=False)
        return Response(get_data.data)

    # API for POST method.
    def post(self, request):
        post_data = PostCardSerializer(data=request.data)

        # Get the upload image.
        if post_data.is_valid():
            post_image = request.data.get("image")
        # Insert the upload image to database.
        card = Driving_License_Card.objects.create(
            image=post_image,
        )

        # Get upload image name
        image = request.FILES["image"]
        # Get upload image path
        path = settings.MEDIA_ROOT + "\images\driving-license\\" + image.name
        # Pass upload image path to ocr function
        res = extract(path)

        # Get result from ocr function and save to the fields of Student_Card database.
        card.driving_license_number = str(res.get("ID"))
        card.name = str(res.get("Name"))
        card.dob = str(res.get("DOB"))
        card.nationality = str(res.get("Nationality"))
        card.address = str(res.get("Address"))
        card.card_class = str(res.get("Class"))
        card.expires = str(res.get("Expires"))
        card.save()

        # Get the latest upload image in database.
        driving_license = Driving_License_Card.objects.last()
        # Delete all previous data to prevent from auto load last image information on start.
        Driving_License_Card.objects.all().delete()
        # Convert image information to JSON and return the JSON format.
        get_data = GetDrivingLicenseSerializer(driving_license, many=False)

        directory = settings.MEDIA_ROOT + "\images\driving-license\\"
        for f in os.listdir(directory):
            os.remove(os.path.join(directory, f))

        return Response(get_data.data)
