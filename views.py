from django.shortcuts import render, redirect, get_object_or_404
from computerApp.models import Machine, Personne, Groupe
from .models import Machine, Personne, Groupe
from computerApp.forms import AddMachineForm, AddPersonneForm, AddGroupeForm, DeleteMachineForm, DeletePersonneForm, DeleteGroupeForm



def index(request) :
    # Ajout de la ligne de recuperation des machines
    machines = Machine.objects.all()
    personnes = Personne.objects.all()
    groupes = Groupe.objects.all()
    ## Filtrage par numero de machine
    #machines = Machine.objects.filtrer(id=1)
    ## Filtrage par debut de nom
    #machines = Machine.objects.filtrer(nom_startwith='10')
    ## trier les machines selon un champ particulier
    #machines = Machine.objects.order_by('-id')
    context = {
        'machines' : machines,
        'personnes' : personnes,
        'groupes' : groupes
    }
    return render(request, 'templates/index.html', context)
    

def machine_list_view(request) :
    machines = Machine.objects.all()
    context = {'machines' : machines}
    return render(request ,'computerApp/machine_list.html' , context)

def machine_detail_view(request, pk) :
    machine = get_object_or_404(Machine, id=pk)
    context={'machine' : machine}
    return render(request, 'computerApp/machine_detail.html', context)

def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'],
                                    mach=form.cleaned_data['mach'],
                                    etat=form.cleaned_data['etat'],
                                    ip=form.cleaned_data['ip'])
            new_machine.save()
            return redirect('machines')
    
    else:
        form = AddMachineForm()
        context = {'form' : form}
        return render(request, 'computerApp/machine_add.html' ,context)

def machine_delete_form(request):
    if request.method == 'POST':
        form = DeleteMachineForm(request.POST)
        if form.is_valid():
            form.delete_machine()
            return redirect('machines')
    
    else:
        form = DeleteMachineForm()
        context = {'form' : form}
        return render(request, 'computerApp/machine_delete.html' ,context)

def personne_list_view(request) :
    personnes = Personne.objects.all()
    context = {'personnes' : personnes}
    return render(request ,'computerApp/personne_list.html' , context)

def personne_detail_view(request, pk) :
    personne = get_object_or_404(Personne, id=pk)
    context={'personne' : personne}
    return render(request, 'computerApp/personne_detail.html', context)



def personne_add_form(request):
    if request.method == 'POST':
        form = AddPersonneForm(request.POST or None)
        if form.is_valid():
            new_personne = Personne(nom=form.cleaned_data['nom'],
                                    prenom=form.cleaned_data['prenom'],
                                    email=form.cleaned_data['email'],
                                    sexe=form.cleaned_data['sexe'],
                                    secteur=form.cleaned_data['secteur'],
                                    )
            new_personne.save()
            return redirect('personnes')
    
    else:
        form = AddPersonneForm()
        context = {'form' : form}
        return render(request, 'computerApp/personne_add.html' ,context)


def personne_delete_form(request):
    if request.method == 'POST':
        form = DeletePersonneForm(request.POST)
        if form.is_valid():
            form.delete_personne()
            return redirect('personnes')
    
    else:
        form = DeletePersonneForm()
        context = {'form' : form}
        return render(request, 'computerApp/personne_delete.html' ,context)


def groupe_list_view(request) :
    groupes = Groupe.objects.all()
    context = {'groupes' : groupes}
    return render(request ,'computerApp/groupe_list.html' , context)

def groupe_detail_view(request, pk) :
    groupe = get_object_or_404(Groupe, id=pk)
    context={'groupe' : groupe}
    return render(request, 'computerApp/groupe_detail.html', context)



def groupe_add_form(request):
    if request.method == 'POST':
        form = AddGroupeForm(request.POST or None)
        if form.is_valid():
            new_groupe = Groupe(nom=form.cleaned_data['nom'],
                                    responsable=form.cleaned_data['responsable'])
            new_groupe.save()
            return redirect('groupes')
    
    else:
        form = AddGroupeForm()
        context = {'form' : form}
        return render(request, 'computerApp/groupe_add.html' ,context)


def groupe_delete_form(request):
    if request.method == 'POST':
        form = DeleteGroupeForm(request.POST)
        if form.is_valid():
            form.delete_groupe()
            return redirect('groupes')
    
    else:
        form = DeleteGroupeForm()
        context = {'form' : form}
        return render(request, 'computerApp/groupe_delete.html' ,context)


def changement_etat_view(request, machine_id):
    # Récupérer la machine correspondant à l'ID
    machine = get_object_or_404(Machine, id=machine_id)

    # Inverser le statut de la machine
    machine.etat = not machine.etat
    machine.save()

    # Rediriger vers la page de détail de la machine
    return redirect('machine_detail', pk=machine_id)

