# Generated by Django 5.1.3 on 2024-11-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='age',
            field=models.IntegerField(),
        ),
    ]