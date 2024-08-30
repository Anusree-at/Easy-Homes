# Generated by Django 5.0.3 on 2024-08-25 17:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_registration_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Architects_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('image', models.FileField(upload_to='')),
                ('image2', models.FileField(blank=True, null=True, upload_to='')),
                ('project_scale', models.CharField(blank=True, max_length=50, null=True)),
                ('building_type', models.CharField(blank=True, max_length=100, null=True)),
                ('model_type', models.CharField(blank=True, max_length=100, null=True)),
                ('software', models.CharField(blank=True, max_length=100, null=True)),
                ('architect_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
