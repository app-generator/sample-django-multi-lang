from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

from .models import *

def home(request):
    
    return render(request, 'home.html') 