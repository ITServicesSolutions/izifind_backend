# Generated by Django 3.2.11 on 2022-05-21 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mycountry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryObjet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Titre')),
                ('description', models.TextField(null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'CategoryObjet',
                'verbose_name_plural': 'CategoryObjets',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name="Genre d'objets")),
                ('description', models.TextField(null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='Code')),
                ('name', models.CharField(max_length=100, verbose_name='Titre')),
                ('description', models.TextField(null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Priority',
                'verbose_name_plural': 'Prioritys',
            },
        ),
        migrations.CreateModel(
            name='Objet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name="Désignation de l'objet")),
                ('reference', models.CharField(max_length=50, verbose_name='Reference Objet')),
                ('description', models.TextField(verbose_name='Description')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('rendu', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auteur', to=settings.AUTH_USER_MODEL, verbose_name="Propio de l'objet")),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorie', to='objects.categoryobjet', verbose_name="Categorie d'objet")),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gender', to='objects.genre', verbose_name='Genre')),
                ('last_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adresse', to='mycountry.adresse', verbose_name='Adresse')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL, verbose_name='Admin IZIFIND')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='priorite', to='objects.priority', verbose_name='Priorité')),
            ],
            options={
                'verbose_name': 'Objet',
                'verbose_name_plural': 'Objets',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name="Titre de l'image")),
                ('image', models.ImageField(upload_to='objet/')),
                ('caption', models.TextField(null=True, verbose_name='Caption')),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objet', to='objects.objet', verbose_name='Objet concerné')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
    ]