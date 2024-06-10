from django.shortcuts import render


# Create your views here.
from django.shortcuts import render, redirect
from.models import Коллекция, Поставщик, Бух_учет, Каталог
from.forms import КоллекцияForm, ПоставщикForm,Бух_учетForm,КаталогForm 


def коллекция_add(request):
    if request.method == "POST":
        form = КоллекцияForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = КоллекцияForm()
    return render(request, 'project_app/add_collec.html', {'form': form})

def поставщик_add(request):
    if request.method == "POST":
        form = ПоставщикForm(request.POST)
        if form.is_valid():
            form.save()
             
    else:
        form = ПоставщикForm()
    return render(request, 'project_app/add_provider.html', {'form': form})  

def бух_учет_add(request):
    if request.method == "POST":
        form = Бух_учетForm(request.POST)
        if form.is_valid():
            form.save()
             
    else:
        form = Бух_учетForm()
    return render(request, 'project_app/add_accounting.html', {'form': form})  

def каталог_add(request):
    if request.method == "POST":
        form = КаталогForm(request.POST)
        if form.is_valid():
            form.save()
             
    else:
        form = КаталогForm()
    return render(request, 'project_app/add_catalog.html', {'form': form})  

