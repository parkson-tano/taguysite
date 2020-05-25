from django.shortcuts import render
from django.http import HttpResponse
from .models import Research,About
# Create your views here.

def index(request):
    about = About.objects.all()
    papers = Research.objects.all()
    return render(request, 'index.html', {'about':about, 'papers':papers})
