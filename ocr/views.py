from django.shortcuts import render, redirect
from django.conf import settings
from .forms import *

from .main import *

# Create your views here.
def base(request):
    text = ""
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image = request.FILES['image']
            path = settings.MEDIA_ROOT + '\images\\' + image.name
            print(path)
            extract(path)
            return redirect('home')

    form = ImagesForm()
    images = Images.objects.all()

    context = {
        'form': form,
        'images': images,
    }

    return render(request, 'base.html', context)
