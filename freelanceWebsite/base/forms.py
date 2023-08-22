from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User


class userForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class ApplyForm(ModelForm):
    class Meta:
        model = Vacansy
        fields = ["selected_freelancer"]
