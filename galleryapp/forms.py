from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Photo

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove help text for cleaner form
        self.fields["username"].help_text = ""
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""
        
        # Add Bootstrap classes
        self.fields["username"].widget.attrs = {"class": "form-control", "placeholder": "Username"}
        self.fields["password1"].widget.attrs = {"class": "form-control", "placeholder": "Password"}
        self.fields["password2"].widget.attrs = {"class": "form-control", "placeholder": "Confirm Password"}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_image"]

class PhotoForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas (e.g., nature, travel, sunset)"
    )
    
    class Meta:
        model = Photo
        fields = ["title", "image", "description", "tags"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Photo title"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Photo description"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tags"].widget.attrs = {"class": "form-control", "placeholder": "Tags (comma-separated)"}
