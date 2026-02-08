from django.contrib import admin
from .models import Profile, Photo, Album, Tag, Like

# Register your models here.

admin.site.register(Profile)
admin.site.register(Photo)
admin.site.register(Album)
admin.site.register(Tag)
admin.site.register(Like)
