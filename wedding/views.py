from django.shortcuts import render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP
from .models import Photo, Gallery, Image

def home(request):
    return render(request, 'home.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP
    })


def photos(request):
    pics = Photo.objects.all()
    galleries = Gallery.objects.all()
    images = Image.objects.all()
    return render(request, 'photos.html', context={
        'photos': pics, 'galleries': galleries, 'images': images
    })
