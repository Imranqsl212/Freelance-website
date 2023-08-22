from django.db import models
from django.contrib.auth.models import User


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
            return self.body[0:41] + ' ...'
        else:
            return self.description
        


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Vacansy, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.body
