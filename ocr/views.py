from django.conf import settings
from django.shortcuts import render, redirect

from .forms import *
from .main import *


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
            path = settings.MEDIA_ROOT + "\images\\" + image.name
            # Pass upload image path to ocr function
            res = extract(path)
            # Get result from ocr function and save to the fields of IdCard database.
            save_result.idcard = str(res.get('ID'))
            save_result.name = str(res.get('Name'))
            save_result.dob = str(res.get('DOB'))
            save_result.nationality = str(res.get('Nationality'))
            save_result.sex = str(res.get('Sex'))
            save_result.hometown = str(res.get('Hometown'))
            save_result.address = str(res.get('Address'))

            save_result.save()

            return redirect("home")

    form = IdCardForm()
    result = IDCard.objects.last()

    context = {
        "form": form,
        "result": result,
    }

    return render(request, "CMND.html", context)


# View to handle student card upload images.
def student_card_page(request):
    # text = ""
    # if request.method == "POST":
    #     form = ImagesForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         save_image = Images.objects.create(image=form.cleaned_data.get("image"))

    #         # Get upload image name
    #         image = request.FILES["image"]
    #         # Get upload image path
    #         path = settings.MEDIA_ROOT + "\images\\" + image.name
    #         # Pass upload image path to ocr function
    #         text = text + str(extract(path))

    #         print("text: \n" + text)
    #         save_image.result = text
    #         save_image.save()

    #         return redirect("home")

    # form = ImagesForm()
    # images = Images.objects.all()

    # context = {
    #     "form": form,
    #     "images": images,
    # }

    # return render(request, "TSV.html", context)
    return render(request, "TSV.html")


# View to handle driving license upload images.
def driving_license_page(request):
    # text = ""
    # if request.method == "POST":
    #     form = ImagesForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         save_image = Images.objects.create(image=form.cleaned_data.get("image"))

    #         # Get upload image name
    #         image = request.FILES["image"]
    #         # Get upload image path
    #         path = settings.MEDIA_ROOT + "\images\\" + image.name
    #         # Pass upload image path to ocr function
    #         text = text + str(extract(path))

    #         print("text: \n" + text)
    #         save_image.result = text
    #         save_image.save()

    #         return redirect("home")

    # form = ImagesForm()
    # images = Images.objects.all()

    # context = {
    #     "form": form,
    #     "images": images,
    # }

    # return render(request, "GPLX.html", context)
    return render(request, "GPLX.html")
