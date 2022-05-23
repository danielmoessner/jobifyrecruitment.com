# Generated by Django 4.0.3 on 2022-05-23 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0062_remove_videoresumepage_video_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffingsolutionspage',
            name='solutions_title',
            field=models.TextField(blank=True, verbose_name='Solutions > Title'),
        ),
        migrations.AlterField(
            model_name='staffingsolutionspage',
            name='solutions_title_de',
            field=models.TextField(blank=True, null=True, verbose_name='Solutions > Title'),
        ),
        migrations.AlterField(
            model_name='staffingsolutionspage',
            name='solutions_title_en',
            field=models.TextField(blank=True, null=True, verbose_name='Solutions > Title'),
        ),
    ]
