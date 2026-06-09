from django.shortcuts import render,redirect,get_object_or_404
from .models import Employe
from .forms import EmployeForm

def liste_employes(request):
    employes = Employe.objects.all()
    context = {
        'employes':employes
        }
    return render(request, "employe/list.html", context)

def ajouter_employe(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_employe')
    context = {
        'form':form
        }
    return render(request, "employe/formulaire.html", context)

def modifier_employe(request,id):
    employe = get_object_or_404(Employe,id=id)
    form = EmployeForm(request.POST or None, instance=employe) 
    if form.is_valid():
        form.save()
        return redirect('liste_employes')
    context = {
        'form':form
        }
    return render(request, "employe/formulaire.html", context)  

def supprimer_employe(request,id):
    employe = get_object_or_404(Employe,id=id)
    if request.method == "POST":
        employe.delete()
        return redirect('liste_employe')
    context = {
        'employe': employe
        }
    return render(request, "employe/confirmer_supression.html", context)  


