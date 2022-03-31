# Generated by Django 4.0.3 on 2022-03-25 11:11

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0015_rename_coursespage_servicespage'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingInAustriaPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.CharField(max_length=100, verbose_name='Header > Title')),
                ('header_title_de', models.CharField(max_length=100, null=True, verbose_name='Header > Title')),
                ('header_title_en', models.CharField(max_length=100, null=True, verbose_name='Header > Title')),
                ('text_title', models.CharField(max_length=200, verbose_name='Text > Title')),
                ('text_title_de', models.CharField(max_length=200, null=True, verbose_name='Text > Title')),
                ('text_title_en', models.CharField(max_length=200, null=True, verbose_name='Text > Title')),
                ('text_sub', models.CharField(max_length=200, verbose_name='Text > Sub')),
                ('text_sub_de', models.CharField(max_length=200, null=True, verbose_name='Text > Sub')),
                ('text_sub_en', models.CharField(max_length=200, null=True, verbose_name='Text > Sub')),
                ('text_text', tinymce.models.HTMLField(verbose_name='Text > Left')),
                ('text_text_de', tinymce.models.HTMLField(null=True, verbose_name='Text > Left')),
                ('text_text_en', tinymce.models.HTMLField(null=True, verbose_name='Text > Left')),
            ],
            options={
                'verbose_name': 'Page > Working In Austria',
            },
        ),
    ]