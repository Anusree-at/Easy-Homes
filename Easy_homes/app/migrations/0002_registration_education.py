# Generated by Django 5.0.3 on 2024-08-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='education',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
