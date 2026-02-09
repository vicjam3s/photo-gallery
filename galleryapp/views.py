from django.shortcuts import render, get_object_or_404
from .models import Photo, Album
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView


def photo_list(request):
    photos = Photo.objects.all().order_by("-created_at")
    return render(request, "photo_list.html", {"photos": photos})


# Photo detail view
def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, "photo_detail.html", {"photo": photo})

# User registration view
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration.html", {"form": form})

# User profile view
@login_required
def profile(request):
    return render(request, "profile.html")

# Album list view
@login_required
def album_list(request):
    albums = Album.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "album_list.html", {"albums": albums})

# Custom login view
class CustomLoginView(LoginView):
    template_name = "login.html"

# Album creation view
@login_required
def album_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            Album.objects.create(user=request.user, name=name)
            return redirect("album-list")
    return render(request, "album_create.html")

# Album detail view
@login_required
def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id, user=request.user)
    return render(request, "album_detail.html", {"album": album})

# Add photo to album view
@login_required
def add_to_album(request, album_id, photo_id):
    album = get_object_or_404(Album, id=album_id, user=request.user)
    photo = get_object_or_404(Photo, id=photo_id)

    album.photos.add(photo)
    return redirect("album-detail", album_id=album.id)
