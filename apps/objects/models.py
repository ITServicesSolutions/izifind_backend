from django.db import models
from accounts.models import CustomUser
from apps.mycountry.models import *
# Create your models here.

class CategoryObjet(models.Model):
    
    #Objets volés, perdus, retrouvés
    #Au cas où on voudrait ajouter d'autre category d'objet ça se fera sans soucis
    
    name = models.CharField(max_length=200, verbose_name="Titre")
    description = models.TextField(verbose_name="Description", null = True)

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Genre(models.Model):
    #Téléphone, Ordinateur, Clé, Portefeuil, 
    name = models.CharField(max_length=200, verbose_name="Genre d'objets")
    description = models.TextField(verbose_name="Description", null = True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Priority(models.Model):
    
    #Priorité attribuée en fonction du type d'objet
    
    code = models.CharField(max_length=20, verbose_name="Code")
    name = models.CharField(max_length=100, verbose_name="Titre")
    description = models.TextField(verbose_name="Description", null = True)

    class Meta:
        verbose_name = "Priorité"
        verbose_name_plural = "Priorités"

    def __str__(self):
        return self.name


class Objet(models.Model):
    
    # Tous les objets (retrouvés, perdus, volés)
    
    author = models.ForeignKey(
        CustomUser, 
        on_delete = models.CASCADE,
        related_name = "auteur",
        verbose_name="Propio de l'objet",
        )
    
    manager = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        related_name = "admin",
        verbose_name = "Admin IZIFIND"
    )
    
    title = models.CharField(max_length = 200, verbose_name= "Désignation de l'objet")
    
    reference = models.CharField(max_length=50, verbose_name= "Reference Objet")
    
    category = models.ForeignKey(
        CategoryObjet, 
        on_delete = models.CASCADE, 
        related_name = 'categorie',
        verbose_name = "Categorie d'objet"
        )

    genre = models.ForeignKey(
        Genre,
        related_name = "gender",
        verbose_name = "Genre",
        on_delete = models.CASCADE
    )
    
    priority = models.ForeignKey(
        Priority,
        on_delete = models.CASCADE,
        related_name = "priorite",
        verbose_name = "Priorité"
    )
    
    description = models.TextField(verbose_name="Description")
    
    last_address = models.ForeignKey(
        Adresse, 
        related_name="adresse",
        verbose_name="Adresse",
        on_delete=models.CASCADE
        )
    
    date_added = models.DateTimeField(auto_now_add=True)
    
    # Pour gérer les suppressions. On ne supprime jamais les données d'une BD
    
    is_visible = models.BooleanField(default=True)
    
    #Pour gérer le retour des objets
    rendu = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Objet"
        verbose_name_plural = "Objets"

    def __str__(self):
        return self.title

class Image(models.Model):
    
    object = models.ForeignKey(
        Objet,
        on_delete = models.CASCADE,
        related_name = "objet",
        verbose_name = "Objet concerné",
        )
    name = models.CharField(max_length=100, verbose_name = "Titre de l'image")
    image = models.ImageField(upload_to = "objet/")
    caption = models.TextField(verbose_name = "Caption", null = True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return self.name

