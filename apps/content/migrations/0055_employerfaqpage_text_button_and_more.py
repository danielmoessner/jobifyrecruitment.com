# Generated by Django 4.0.3 on 2022-05-17 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0054_alter_aboutpage_header_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerfaqpage',
            name='text_button',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Button'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='text_button_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Button'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='text_button_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Button'),
        ),
    ]
