# Generated by Django 4.0.3 on 2022-06-02 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0071_aboutpage_meta_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='employer',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Employer'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='from_date',
            field=models.DateField(blank=True, null=True, verbose_name='From Date'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='until_date',
            field=models.DateField(blank=True, null=True, verbose_name='Until Date'),
        ),
    ]
