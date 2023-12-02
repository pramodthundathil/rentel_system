# Generated by Django 3.2.7 on 2023-12-02 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Place', models.CharField(max_length=255)),
                ('Date', models.DateField(auto_now_add=True)),
                ('District', models.CharField(max_length=255)),
                ('State', models.CharField(max_length=255)),
                ('Rent_per_momth', models.FloatField()),
                ('Description', models.CharField(max_length=1000)),
                ('Image', models.FileField(upload_to='Property_image')),
                ('Status', models.BooleanField(default=True)),
                ('User_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
