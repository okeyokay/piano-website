from django.shortcuts import render
from .models import PracticeSession
from django.db import models

def leaderboard(request):
    leaderboard_data = (
        PracticeSession.objects.values('user__username')
        .annotate(total_minutes=models.Sum('minutes'))
        .order_by('-total_minutes')
    )
    return render(request, 'practice/leaderboard.html', {'leaderboard': leaderboard_data})
