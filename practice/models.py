# practice/models.py
from django.db import models
from django.contrib.auth.models import User

class PracticeSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} practiced {self.minutes} min on {self.date}"
