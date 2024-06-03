from django.shortcuts import render

# Create your views here.

def home(request):
    # Your view logic here
    return render(request, 'home.html')