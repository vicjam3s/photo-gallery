from django.shortcuts import render, get_object_or_404
from .models import Photo, Album, Like, Tag, Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import ProfileForm, PhotoForm, RegistrationForm

# Landing page view
def landing(request):
    return render(request, "landing.html")


# Photo list view
def photo_list(request):
    tag_name = request.GET.get("tag")
    tags = Tag.objects.all()

    if tag_name:
        photos = Photo.objects.filter(tags__name=tag_name)
    else:
        photos = Photo.objects.all()

    return render(
        request,
        "photo_list.html",
        {
            "photos": photos,
            "tags": tags,
            "active_tag": tag_name,
        },
    )

# Photo creation view
@login_required
def photo_create(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploaded_by = request.user
            photo.save()
            
            # Handle tags
            tags_input = form.cleaned_data.get("tags", "")
            if tags_input:
                tag_names = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
                for tag_name in tag_names:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    photo.tags.add(tag)
            
            return redirect("photo-list")
    else:
        form = PhotoForm()
    
    return render(request, "photo_create.html", {"form": form})

# Photo details view
def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    user_liked = False
    if request.user.is_authenticated:
        user_liked = Like.objects.filter(user=request.user, photo=photo, is_liked=True).exists()
    return render(request, "photo_detail.html", {"photo": photo, "user_liked": user_liked})

# User registration view
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistrationForm()

    return render(request, "registration.html", {"form": form})

# User profile view
@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    liked_photos = Photo.objects.filter(like__user=request.user, like__is_liked=True).distinct()

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "profile.html", {"form": form, "liked_photos": liked_photos})

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

# Toggle like view
@login_required
def toggle_like(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)

    like, created = Like.objects.get_or_create(
        user=request.user,
        photo=photo,
        defaults={"is_liked": True},
    )

    if not created:
        like.is_liked = not like.is_liked
        like.save()

    return redirect("photo-detail", photo_id=photo.id)
