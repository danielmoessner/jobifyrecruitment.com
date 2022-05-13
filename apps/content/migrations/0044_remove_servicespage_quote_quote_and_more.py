# Generated by Django 4.0.3 on 2022-05-13 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0043_remove_navigation_job_seeker_salary_guides_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicespage',
            name='quote_quote',
        ),
        migrations.RemoveField(
            model_name='servicespage',
            name='quote_quote_de',
        ),
        migrations.RemoveField(
            model_name='servicespage',
            name='quote_quote_en',
        ),
        migrations.AddField(
            model_name='servicespage',
            name='quote_text',
            field=models.TextField(blank=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='quote_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='quote_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
    ]