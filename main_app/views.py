from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Driver


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def driver_index(request):
    drivers = Driver.objects.all().order_by('name')
    return render(request, 'drivers/index.html', {'drivers': drivers})

def driver_detail(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, 'drivers/detail.html', {'driver': driver})

# --- CBVs for C/U/D ---

class DriverCreate(CreateView):
    model = Driver
    fields = '__all__'

class DriverUpdate(UpdateView):
    model = Driver
    fields = ['current_team', 'description', 'age', 'drive_years']

class DriverDelete(DeleteView):
    model = Driver
    success_url = '/drivers/'