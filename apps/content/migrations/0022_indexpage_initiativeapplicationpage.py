# Generated by Django 4.0.3 on 2022-04-25 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0021_alter_applicant_department_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.CharField(blank=True, max_length=1000, verbose_name='Header > Title')),
                ('header_title_de', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title')),
                ('header_title_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title')),
                ('header_text', models.TextField(blank=True, verbose_name='Header > Text')),
                ('header_text_de', models.TextField(blank=True, null=True, verbose_name='Header > Text')),
                ('header_text_en', models.TextField(blank=True, null=True, verbose_name='Header > Text')),
                ('header_button_left', models.CharField(blank=True, max_length=100, verbose_name='Header > Button Left')),
                ('header_button_left_de', models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Button Left')),
                ('header_button_left_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Button Left')),
                ('header_button_right', models.CharField(blank=True, max_length=100, verbose_name='Header > Button Right')),
                ('header_button_right_de', models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Button Right')),
                ('header_button_right_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Button Right')),
                ('services_left', models.CharField(blank=True, max_length=300, verbose_name='Services > Left')),
                ('services_left_de', models.CharField(blank=True, max_length=300, null=True, verbose_name='Services > Left')),
                ('services_left_en', models.CharField(blank=True, max_length=300, null=True, verbose_name='Services > Left')),
                ('services_button_left', models.CharField(blank=True, max_length=100, verbose_name='Services > Button Left')),
                ('services_button_left_de', models.CharField(blank=True, max_length=100, null=True, verbose_name='Services > Button Left')),
                ('services_button_left_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Services > Button Left')),
                ('services_center', models.CharField(blank=True, max_length=300, verbose_name='Services > Center')),
                ('services_center_de', models.CharField(blank=True, max_length=300, null=True, verbose_name='Services > Center')),
                ('services_center_en', models.CharField(blank=True, max_length=300, null=True, verbose_name='Services > Center')),
                ('services_button_center', models.CharField(blank=True, max_length=100, verbose_name='Services > Button Center')),
                ('services_button_center_de', models.CharField(blank=True, max_length=100, null=True, verbose_name='Services > Button Center')),
                ('services_button_center_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Services > Button Center')),
                ('services_right', models.CharField(blank=True, max_length=300, verbose_name='Services > Right')),
                ('services_right_de', models.CharField(blank=True, max_length=300, null=True, verbose_name='Services > Right')),
                ('services_right_en', models.CharField(blank=True, max_length=300, null=True, verbose_name='Services > Right')),
                ('services_button_right', models.CharField(blank=True, max_length=100, verbose_name='Services > Button Right')),
                ('services_button_right_de', models.CharField(blank=True, max_length=100, null=True, verbose_name='Services > Button Right')),
                ('services_button_right_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Services > Button Right')),
                ('text_title', models.CharField(blank=True, max_length=1000, verbose_name='Text > Title')),
                ('text_title_de', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Text > Title')),
                ('text_title_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Text > Title')),
                ('text_text', models.TextField(blank=True, verbose_name='Text > Text')),
                ('text_text_de', models.TextField(blank=True, null=True, verbose_name='Text > Text')),
                ('text_text_en', models.TextField(blank=True, null=True, verbose_name='Text > Text')),
                ('applicants_title', models.CharField(blank=True, max_length=1000, verbose_name='Applicants > Title')),
                ('applicants_title_de', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Applicants > Title')),
                ('applicants_title_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Applicants > Title')),
                ('applicants_text', models.TextField(blank=True, verbose_name='Applicants > Text')),
                ('applicants_text_de', models.TextField(blank=True, null=True, verbose_name='Applicants > Text')),
                ('applicants_text_en', models.TextField(blank=True, null=True, verbose_name='Applicants > Text')),
                ('applicants_button', models.CharField(blank=True, max_length=200, verbose_name='Applicants > Button')),
                ('applicants_button_de', models.CharField(blank=True, max_length=200, null=True, verbose_name='Applicants > Button')),
                ('applicants_button_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Applicants > Button')),
            ],
            options={
                'verbose_name': 'Page > Home',
            },
        ),
        migrations.CreateModel(
            name='InitiativeApplicationPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.CharField(blank=True, max_length=200, verbose_name='Header > Title')),
                ('header_title_de', models.CharField(blank=True, max_length=200, null=True, verbose_name='Header > Title')),
                ('header_title_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Header > Title')),
            ],
            options={
                'verbose_name': 'Page > Initiative Application',
            },
        ),
    ]
