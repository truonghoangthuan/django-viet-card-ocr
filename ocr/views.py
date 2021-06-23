from django.conf import settings
from django.shortcuts import render, redirect

from .forms import *
from .main import *


# Create your views here.
def base(request):
    text = ""
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            save_image = Images.objects.create(image=form.cleaned_data.get('image'))

            # Get upload image name
            image = request.FILES['image']
            # Get upload image path
            path = settings.MEDIA_ROOT + '\images\\' + image.name
            # Pass upload image path to ocr function
            text = text + str(extract(path))
            print('text: ' + text)
            save_image.result = text
            save_image.save()

            return redirect('home')

    form = ImagesForm()
    images = Images.objects.all()

    context = {
        'form': form,
        'images': images,
    }

    return render(request, 'CMND.html', context)


def student_card_page(request):
    return render(request, 'TSV.html')


def driving_license_page(request):
    return render(request, 'GPLX.html')
