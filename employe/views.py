from django.shortcuts import render
from .models import Employe

def liste_employes(request):
    employes = Employe.objects.all()
    return render(request, "employe/list.html", {'employes':'employes'})
