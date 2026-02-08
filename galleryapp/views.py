from django.shortcuts import render, get_object_or_404
from .models import Photo


def photo_list(request):
    photos = Photo.objects.all().order_by("-created_at")
    return render(request, "photo_list.html", {"photos": photos})


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, "photo_detail.html", {"photo": photo})
