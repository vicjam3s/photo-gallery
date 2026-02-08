from django.shortcuts import render, get_object_or_404
from .models import Photo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView


def photo_list(request):
    photos = Photo.objects.all().order_by("-created_at")
    return render(request, "photo_list.html", {"photos": photos})


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, "photo_detail.html", {"photo": photo})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration.html", {"form": form})


@login_required
def profile(request):
    return render(request, "profile.html")


class CustomLoginView(LoginView):
    template_name = "login.html"
