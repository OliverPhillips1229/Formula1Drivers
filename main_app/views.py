from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Driver, Helmet
from .forms import ResultForm, HelmetForm, DriverForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def driver_index(request):
    drivers = Driver.objects.all().order_by('name')
    return render(request, 'drivers/index.html', {'drivers': drivers})

def driver_detail(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    available_helmets = Helmet.objects.exclude(
        id__in=driver.helmets.all().values_list('id', flat=True)
    )
    return render(request, 'drivers/detail.html', {
        'driver': driver,
        'available_helmets': available_helmets
    })

def add_result(request, driver_id):
    form = ResultForm(request.POST)
    if form.is_valid():
        new_result = form.save(commit=False)
        new_result.driver_id = driver_id
        new_result.save()
    return redirect('driver-detail', driver_id=driver_id)

def associate_helmet(request, driver_id, helmet_id):
    if request.method == 'POST':
        Driver.objects.get(id=driver_id).helmets.add(helmet_id)
    return redirect('driver-detail', driver_id=driver_id)

def remove_helmet(request, driver_id, helmet_id):
    if request.method == 'POST':
        driver = get_object_or_404(Driver, id=driver_id)
        driver.helmets.remove(helmet_id)
    return redirect('driver-detail', driver_id=driver_id)

# --- CBVs for C/U/D on Driver ---

class DriverCreate(CreateView):
    model = Driver
    form_class = DriverForm
    # get_absolute_url on Driver will handle redirect after create, if defined

class DriverUpdate(UpdateView):
    model = Driver
    form_class = DriverForm

class DriverDelete(DeleteView):
    model = Driver
    success_url = '/drivers/'
    
class HelmetCreate(CreateView):
    model = Helmet
    form_class = HelmetForm

class HelmetList(ListView):
    model = Helmet

class HelmetDetail(DetailView):
    model = Helmet

class HelmetUpdate(UpdateView):
    model = Helmet
    form_class = HelmetForm

class HelmetDelete(DeleteView):
    model = Helmet
    success_url = '/helmets/'