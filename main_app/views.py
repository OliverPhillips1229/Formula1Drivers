from django.shortcuts import render
from .models import Driver

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def driver_index(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/index.html', {'drivers': drivers})


# Detail view for a specific driver
def driver_detail(request, driver_id):
    driver = Driver.objects.get(id=driver_id)
    return render(request, 'drivers/detail.html', {'driver': driver})


