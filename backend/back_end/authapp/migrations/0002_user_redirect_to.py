# Generated by Django 4.2.16 on 2024-12-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='redirect_to',
            field=models.BooleanField(default=False),
        ),
    ]
