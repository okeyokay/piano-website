from django.shortcuts import render
from .models import PracticeSession
from django.db import models
import datetime, calendar

def leaderboard(request):
    today = datetime.date.today()
    current_year = today.year
    current_month = today.month
    month_name = calendar.month_name[current_month]

    leaderboard_data = (
        PracticeSession.objects
        .filter(date__year=current_year, date__month=current_month)
        .values('user__username')
        .annotate(total_minutes=models.Sum('minutes'))
        .order_by('-total_minutes')
    )
    return render(request, 'practice/leaderboard.html', {
        'leaderboard': leaderboard_data,
        'current_month': month_name
        })
