# Generated by Django 3.2.4 on 2021-06-26 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0005_driving_lisense_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driving_License_Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/driving-license/')),
                ('driving_license_number', models.CharField(blank=True, max_length=15, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('dob', models.CharField(blank=True, max_length=10, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('card_class', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Driving_Lisense_Card',
        ),
    ]
