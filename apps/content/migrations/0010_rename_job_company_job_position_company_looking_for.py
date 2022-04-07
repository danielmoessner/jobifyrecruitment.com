# Generated by Django 4.0.3 on 2022-04-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_portalpage_header_title_de_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='job',
            new_name='job_position',
        ),
        migrations.AddField(
            model_name='company',
            name='looking_for',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
