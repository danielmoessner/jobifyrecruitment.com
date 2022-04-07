# Generated by Django 4.0.3 on 2022-04-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_alter_member_options_alter_membercategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortalPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.CharField(blank=True, max_length=1000, verbose_name='Header > Title')),
            ],
            options={
                'verbose_name': 'Page > Portal',
            },
        ),
    ]