# Generated by Django 5.0.4 on 2024-04-21 12:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoviePerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='kinopoisk/images/person/photos/')),
                ('role', models.CharField(blank=True, choices=[('actor', 'Actor'), ('director', 'Director')], max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=355)),
                ('description', models.TextField()),
                ('release_date', models.DateField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('duration', models.PositiveSmallIntegerField()),
                ('budget', models.PositiveIntegerField()),
                ('poster', models.ImageField(blank=True, null=True, upload_to='kinopoisk/images/movies/posters/')),
                ('genres', models.ManyToManyField(related_name='movies', to='film.genre')),
                ('actors', models.ManyToManyField(related_name='acted_in_movies', to='film.movieperson')),
                ('directors', models.ManyToManyField(related_name='directed_movies', to='film.movieperson')),
            ],
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='film.movie')),
            ],
        ),
    ]
