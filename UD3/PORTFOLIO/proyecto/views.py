from django.shortcuts import render, get_object_or_404
from .models import Proyecto

def proyectos(request):
    proyectos = Proyecto.objects.order_by("titulo")[:6]
    return render(request, 'proyecto/proyecto.html', {"proyectos": proyectos})