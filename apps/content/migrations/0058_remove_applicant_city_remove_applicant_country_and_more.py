# Generated by Django 4.0.3 on 2022-05-17 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0057_initiativeapplicationpage_email_html_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='city',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='country',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='number',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='postal',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='state_province',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='street',
        ),
    ]