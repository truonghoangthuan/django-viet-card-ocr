# Generated by Django 3.2.4 on 2021-06-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0002_auto_20210625_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/student-card/')),
                ('student_card_number', models.CharField(blank=True, max_length=15, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('major', models.CharField(blank=True, max_length=255, null=True)),
                ('falculty', models.CharField(blank=True, max_length=255, null=True)),
                ('course', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='idcard',
            name='image',
            field=models.ImageField(upload_to='images/id-card/'),
        ),
    ]
