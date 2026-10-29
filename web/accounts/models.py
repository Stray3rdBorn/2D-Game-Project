import secrets

from django.contrib.auth.models import User
from django.db import models


def generate_key():
    return secrets.token_urlsafe(32)


class ApiKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=64, unique=True, default=generate_key)

    class Meta:
        db_table = "api_keys"

    def __str__(self):
        return f"API key of {self.user.username}"


class Score(models.Model):
    user_id = models.IntegerField()
    player_name = models.CharField(max_length=20)
    score = models.IntegerField()
    wave_reached = models.IntegerField()
    won = models.BooleanField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "scores"
        ordering = ["-score", "created_at"]

    def __str__(self):
        return f"{self.player_name}: {self.score}"