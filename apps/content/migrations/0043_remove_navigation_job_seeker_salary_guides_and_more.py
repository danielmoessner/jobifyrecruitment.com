# Generated by Django 4.0.3 on 2022-05-13 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0042_remove_applicant_salutation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navigation',
            name='job_seeker_salary_guides',
        ),
        migrations.RemoveField(
            model_name='navigation',
            name='job_seeker_salary_guides_de',
        ),
        migrations.RemoveField(
            model_name='navigation',
            name='job_seeker_salary_guides_en',
        ),
    ]
