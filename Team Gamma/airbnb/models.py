from django.db import models
from django.utils import timezone
from django.db.models.fields.related import ForeignKey
from django.template.defaultfilters import length
from django.db.models.deletion import CASCADE

# Create your models here.


class categorie(models.Model):
    #categorie_id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __init__(self):
        return "%s %s" % (self.nom, self.description)


class salles(models.Model):
    """docstring for ClassName"""
    #Salle_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    description = models.TextField(null=True)
    categorie = models.ForeignKey('airbnb.categorie', on_delete=CASCADE)

    def __init__(self):
        return "%s %s %s" % (self.code, self.adresse, self.description)


class usersGroup(models.Model):
    #usersGroup_id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    diminutif = models.CharField(max_length=100)

    def __init__(self):
        return "%s %s" % (self.nom, self.diminutif)


class users(models.Model):
    #users_id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    numero = models.IntegerField()
    email = models.EmailField()
    mot_de_passe = models.CharField(max_length=50)
    usersGroup = models.ForeignKey('airbnb.usersGroup', on_delete=CASCADE)

    def __init__(self):
        return "%s %s %s %s %s" % (self.nom, self.prenom, self.numero, self.email, self.password)


class reservations(models.Model):
    """docstring for reservations"""
    #reservations_id = models.IntegerField(primary_key=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    salles = models.ForeignKey('airbnb.salles', on_delete=CASCADE)
    users = models.ForeignKey('airbnb.users', on_delete=CASCADE)

    def __init__(self):
        return "%s %s" % (self.date_debut, self.date_fin)


class image(models.Model):
    #image_id = models.IntegerField(primary_key=True)
    photo = models.ImageField()
    salles = models.ForeignKey('airbnb.salles', on_delete=CASCADE)

    def __init__(self):
        return "%s" % (self.photo)


class mode_de_payement(models.Model):
    """docstring for mode_de_payement"""
    mode = models.CharField(max_length=100)

    def __init__(self):
        return "%s" % (self.mode)


class facture(models.Model):
    """docstring for ClassName"""
    remise_pourcentage = models.IntegerField()
    remise_montant = models.IntegerField()
    date = models.DateField()
    salle = models.CharField(max_length=100)
    reservations = models.ForeignKey('airbnb.reservations', on_delete=CASCADE)
    mode_de_payement = models.ForeignKey(
        'airbnb.mode_de_payement', on_delete=CASCADE)

    def __init__(self):
        return "%s %s" % (self.remise_pourcentage, self.remise_montant, self.date, self.salle, self.reservations, self.mode_de_payement)
