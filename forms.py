import re
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
    etat = forms.BooleanField(required=False, label='Etat de la machine')
    ip = forms.GenericIPAddressField(label="Adresse IP")

    # On ajoute une fonction de validation
    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) > 20:
            raise ValidationError(("Erreur de format pour le champ nom"))
        return data
    
    def cleaned_ip(self):
        data = self.cleaned_data["ip"]
        address = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        if not (re.search(address, data)):
            raise ValidationError(("Erreure de format pour le champ Adresse IP"))
        return data
    

class AddPersonneForm(forms.Form) :

    TYPE = (
    ('Employer Masculin', ('Employer Masculin')),
    ('Employer Féminin', ('Employer Féminin')),
    ('Non Défini', ('Non Défini')),
    )

    TYPE2 = (
    ('Non défini', ('Non défini')),
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
    email = forms.EmailField(max_length=70, label="email de l'employer")
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
    
    def clean_email(self):
        data = self.cleaned_data["email"]
        if len(data) > 70:
            raise ValidationError(("Erreur de format pour le champ email"))
        return data

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


class DeleteMachineForm(forms.Form) :
    
    nom_de_la_machine = forms.ModelChoiceField(queryset=Machine.objects.all())

    # On ajoute une fonction de validation
    def delete_machine(self):
        machine = self.cleaned_data.get('nom_de_la_machine')
        if machine:
            machine.delete()

class DeletePersonneForm(forms.Form) :
    
    nom_de_la_personne = forms.ModelChoiceField(queryset=Personne.objects.all())

    # On ajoute une fonction de validation
    def delete_personne(self):
        personne = self.cleaned_data.get('nom_de_la_personne')
        if personne:
            personne.delete()

    

class DeleteGroupeForm(forms.Form) :
    
    nom_du_groupe = forms.ModelChoiceField(queryset=Groupe.objects.all())

    # On ajoute une fonction de validation
    def delete_groupe(self):
        groupe = self.cleaned_data.get('nom_du_groupe')
        if groupe :
            groupe.delete()
