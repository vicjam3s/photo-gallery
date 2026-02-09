from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.landing, name="landing"),
    path("gallery/", views.photo_list, name="photo-list"),

    path("photo/<int:photo_id>/", views.photo_detail, name="photo-detail"),

    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="photo-list"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    path("albums/", views.album_list, name="album-list"),
    path("albums/create/", views.album_create, name="album-create"),
    path("albums/<int:album_id>/", views.album_detail, name="album-detail"),
    path("albums/<int:album_id>/add/<int:photo_id>/", views.add_to_album, name="add-to-album"),
    path("photo/<int:photo_id>/like/", views.toggle_like, name="toggle-like"),

    
]    

