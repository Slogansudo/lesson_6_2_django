# Generated by Django 5.0.3 on 2024-04-08 01:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_students_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.address'),
        ),
    ]