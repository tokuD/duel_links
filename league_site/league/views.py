from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    return render(request, 'league/index.html')

def users_detail(request, pk):
    return render(request, 'league/users_detail.html')
