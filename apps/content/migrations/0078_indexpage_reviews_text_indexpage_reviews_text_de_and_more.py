# Generated by Django 4.0.3 on 2022-09-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0077_review_applicant_preview'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='reviews_text',
            field=models.TextField(blank=True, verbose_name='Reviews > Text'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='reviews_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Reviews > Text'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='reviews_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Reviews > Text'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='reviews_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Reviews > Title'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='reviews_title_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Reviews > Title'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='reviews_title_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Reviews > Title'),
        ),
    ]
