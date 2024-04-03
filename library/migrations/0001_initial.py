# Generated by Django 5.0.3 on 2024-04-03 00:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(auto_created=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('year', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ManyToManyField(to='library.author')),
                ('book', models.ManyToManyField(to='library.books')),
            ],
        ),
        migrations.CreateModel(
            name='StudentsBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('take_date', models.DateTimeField(auto_now_add=True)),
                ('returned_status', models.BooleanField(default=False)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.address')),
                ('books', models.ManyToManyField(to='library.books')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userstudents')),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.books')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.studentsbook')),
            ],
        ),
    ]
