# Generated by Django 4.0.3 on 2022-04-25 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0025_navigation_employer_how_it_works_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='firstname',
            field=models.CharField(max_length=100, verbose_name='Firstname'),
        ),
    ]
