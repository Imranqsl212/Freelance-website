from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Vacansy(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    isDone = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    selected_freelancer = models.ForeignKey(
        User,
        related_name="selected_vacancies",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    participants = models.ManyToManyField(User, related_name="participants", blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        if len(self.description) >= 40:
            return self.body[0:41] + " ..."
        else:
            return self.description


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.body


class Apply(models.Model):
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    vacansy = models.ForeignKey(
        Vacansy, on_delete=models.CASCADE, default=None, null=False
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    telegram = models.CharField(max_length=100,default='')
    

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.description
