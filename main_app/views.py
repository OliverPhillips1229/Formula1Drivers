from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Driver, Helmet
from .forms import ResultForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def driver_index(request):
    drivers = Driver.objects.all().order_by('name')
    return render(request, 'drivers/index.html', {'drivers': drivers})

def driver_detail(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    result_form = ResultForm()  # <-- for the "Add Result" form on the page
    return render(request, 'drivers/detail.html', {
        'driver': driver,
        'result_form': result_form
    })

def add_result(request, driver_id):
    form = ResultForm(request.POST)
    if form.is_valid():
        new_result = form.save(commit=False)
        new_result.driver_id = driver_id
        new_result.save()
    return redirect('driver-detail', driver_id=driver_id)

# --- CBVs for C/U/D on Driver ---

class DriverCreate(CreateView):
    model = Driver
    fields = '__all__'
    # get_absolute_url on Driver will handle redirect after create, if defined

class DriverUpdate(UpdateView):
    model = Driver
    fields = ['current_team', 'description', 'age', 'drive_years']

class DriverDelete(DeleteView):
    model = Driver
    success_url = '/drivers/'
    
class HelmetCreate(CreateView):
    model = Helmet
    fields = '__all__'

class HelmetList(ListView):
    model = Helmet

class HelmetDetail(DetailView):
    model = Helmet

class HelmetUpdate(UpdateView):
    model = Helmet
    fields = ['name', 'color']

class HelmetDelete(DeleteView):
    model = Helmet
    success_url = '/helmets/'