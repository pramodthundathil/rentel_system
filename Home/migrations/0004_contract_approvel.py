# Generated by Django 3.2.14 on 2023-12-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='approvel',
            field=models.BooleanField(default=False),
        ),
    ]
