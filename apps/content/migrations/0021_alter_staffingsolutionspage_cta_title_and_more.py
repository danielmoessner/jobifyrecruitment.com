# Generated by Django 4.0.3 on 2022-03-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0020_staffingsolutionspage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffingsolutionspage',
            name='cta_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Cta > Title'),
        ),
        migrations.AlterField(
            model_name='staffingsolutionspage',
            name='cta_title_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Cta > Title'),
        ),
        migrations.AlterField(
            model_name='staffingsolutionspage',
            name='cta_title_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Cta > Title'),
        ),
    ]