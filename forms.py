from typing import Any, Dict #queryset
from django import forms
from django.core.exceptions import ValidationError
from computerApp.models import Machine, Personne, Groupe


class AddMachineForm(forms.Form) :

    TYPE = (
    ('PC', ('PC - Run windows')),
    ('Mac', ('MAc - Run MacOS')),
    ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
    ('Switch', ('Switch - To maintains and connect servers')),
    )
    
    nom = forms.CharField(required=True, label='Nom de la machine')
    mach = forms.ChoiceField(choices=TYPE, required=False)
    etat = forms.BooleanField(required=True, label='Etat de la machine')

    # On ajoute une fonction de validation
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 20:
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data
    
    

class AddPersonneForm(forms.Form) :

    TYPE = (
    ('M', ('Employer Masculin')),
    ('F', ('employer Féminin')),
    ('ND', ('Non défini')),
    )

    TYPE2 = (
    ('ND', ('Non défini')),
    ('DG', ('Direction Générale')),
    ('RH', ('Ressource Humaine')),
    ('DST', ('Direction des services techniques')),
    ('DF', ('Direction financière')),
    ('DSI', ('Direction des services informatiques')),
    ('DF', ('Direction Marketing')),
    )
    
    nom = forms.CharField(required=True, label="Nom de l'employer")
    prenom = forms.CharField(required=True, label="Prénom de l'employer")
    secteur = forms.ChoiceField(choices=TYPE2, required=False)
    #email = forms.CharField(max_length=64, required=False)
    sexe = forms.ChoiceField(choices=TYPE, required=False)

    # On ajoute une fonction de validation
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 20:
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data
    
    def clean_prenom(self):
        data = self.cleaned_data["prenom"]
        if len(data) > 20:
            raise ValidationError(("Erreur de format pour le champ prénom"))
        return data
    


class DeleteMachineForm(forms.Form) :
    
    machine_id = forms.ModelChoiceField(queryset=Machine.objects.all())

    # On ajoute une fonction de validation
    def delete_machine(self):
        machine = self.cleaned_data.get('machine_id')
        if machine:
            machine.delete()

class DeletePersonneForm(forms.Form) :
    
    personne_id = forms.ModelChoiceField(queryset=Personne.objects.all())

    # On ajoute une fonction de validation
    def delete_personne(self):
        personne = self.cleaned_data.get('personne_id')
        if personne:
            personne.delete()


class AddGroupeForm(forms.Form) :
    
    nom = forms.CharField(required=True, label="Nom du groupe")
    responsable = forms.CharField(required=True, label="Nom du responsable")
    # On ajoute une fonction de validation
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 50:
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data
    
    def clean_responsable(self):
        data = self.cleaned_data["responsable"]
        if len(data) > 50:
            raise ValidationError(("Erreur de format pour le champ responsable"))
        return data
    

class DeleteGroupeForm(forms.Form) :
    
    groupe_id = forms.ModelChoiceField(queryset=Groupe.objects.all())

    # On ajoute une fonction de validation
    def delete_groupe(self):
        groupe = self.cleaned_data.get('groupe_id')
        if groupe :
            groupe.delete()
