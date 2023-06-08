from datetime import datetime , timedelta
from django.db import models




class Machine(models.Model):

    TYPE = (
    ('PC', ('PC - Run windows')),
    ('Mac', ('MAc - Run MacOS')),
    ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
    ('Switch', ('Switch - To maintains and connect servers')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom= models.CharField(max_length = 20)
    maintenanceDate = models.DateField(default = datetime.now() + timedelta(weeks=2))
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')
    etat = models.BooleanField(default=False)
    ip = models.CharField(max_length=15, default='0.0.0.0')
 

    def __str__(self) :
        return  self.nom

    def get_name(self):
        return  self.nom

class Personne(models.Model):

    TYPE = (
    ('M', ('Employer Masculin')),
    ('F', ('Employer Féminin')),
    ('ND', ('Non Défini')),
    )

    TYPE2 = (
    ('DG', ('Direction Générale')),
    ('RH', ('Ressource Humaine')),
    ('DST', ('Direction des services techniques')),
    ('DF', ('Direction Financière')),
    ('DSI', ('Direction des services informatiques')),
    ('DM', ('Direction Marketing')),
    ('ND', ('Non défini')),
    )



    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length = 20)
    prenom = models.CharField(max_length = 20)
    sexe = models.CharField(max_length= 50, choices=TYPE, default='ND')
    secteur = models.CharField(max_length= 50, choices=TYPE2, default='ND')
    email = models.EmailField(max_length=70)
            
    def __str__(self) :
        return  self.nom + " " + self.prenom

    def get_name(self):
        return  self.nom + " " + self.prenom
    

class Groupe(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length = 50)
    responsable = models.CharField(max_length = 50)
    
            
    def __str__(self) :
        return  self.nom 

    def get_name(self):
        return  self.nom 

