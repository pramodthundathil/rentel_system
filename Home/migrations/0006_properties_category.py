# Generated by Django 5.0.2 on 2024-03-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_auto_20231202_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='category',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('House', 'House'), ('office', 'office'), ('Villa', 'Villa')], default='House', max_length=50),
        ),
    ]
