from django.urls import path
from . import views

urlpatterns = [
    path("", views.photo_list, name="photo-list"),
    path("photo/<int:photo_id>/", views.photo_detail, name="photo-detail"),
]
