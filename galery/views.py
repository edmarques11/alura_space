from django.shortcuts import render

def index(request):
  return render(request, 'galery/index.html')

# Create your views here.
