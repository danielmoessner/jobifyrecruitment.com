# Generated by Django 4.0.3 on 2022-05-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0065_footer_column_1_mail_de_footer_column_1_mail_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='employer_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Employer'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='employer_3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Employer'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='from_date_2',
            field=models.DateField(blank=True, null=True, verbose_name='From Date'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='from_date_3',
            field=models.DateField(blank=True, null=True, verbose_name='From Date'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='position_2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Position'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='position_3',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Position'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='until_date_2',
            field=models.DateField(blank=True, null=True, verbose_name='Until Date'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='until_date_3',
            field=models.DateField(blank=True, null=True, verbose_name='Until Date'),
        ),
    ]