from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def base(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = ImagesForm()
    images = Images.objects.all()

    context = {
        'form': form,
        'images': images,
    }

    return render(request, 'base.html', context)
