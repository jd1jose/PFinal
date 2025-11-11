from django.shortcuts import render, redirect
from .forms import PersonaForm
from .models import Persona

def index(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PersonaForm()

    personas = Persona.objects.all()
    return render(request, 'appFinal/index.html', {'form': form, 'personas': personas})