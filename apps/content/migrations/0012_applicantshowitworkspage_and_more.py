# Generated by Django 4.0.3 on 2022-03-25 10:49

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0011_rename_icon_staffcategory_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantsHowItWorksPage',
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
                ('text_button', models.CharField(max_length=200, verbose_name='Text > Button')),
                ('text_button_de', models.CharField(max_length=200, null=True, verbose_name='Text > Button')),
                ('text_button_en', models.CharField(max_length=200, null=True, verbose_name='Text > Button')),
                ('plan_title', models.CharField(max_length=100, verbose_name='Plan > Title')),
                ('plan_title_de', models.CharField(max_length=100, null=True, verbose_name='Plan > Title')),
                ('plan_title_en', models.CharField(max_length=100, null=True, verbose_name='Plan > Title')),
                ('plan_1', models.TextField(blank=True, verbose_name='Plan > Step 1')),
                ('plan_1_de', models.TextField(blank=True, null=True, verbose_name='Plan > Step 1')),
                ('plan_1_en', models.TextField(blank=True, null=True, verbose_name='Plan > Step 1')),
                ('plan_2', models.TextField(blank=True, verbose_name='Plan > Step 2')),
                ('plan_2_de', models.TextField(blank=True, null=True, verbose_name='Plan > Step 2')),
                ('plan_2_en', models.TextField(blank=True, null=True, verbose_name='Plan > Step 2')),
                ('plan_3', models.TextField(blank=True, verbose_name='Plan > Step 3')),
                ('plan_3_de', models.TextField(blank=True, null=True, verbose_name='Plan > Step 3')),
                ('plan_3_en', models.TextField(blank=True, null=True, verbose_name='Plan > Step 3')),
                ('plan_4', models.TextField(blank=True, verbose_name='Plan > Step 4')),
                ('plan_4_de', models.TextField(blank=True, null=True, verbose_name='Plan > Step 4')),
                ('plan_4_en', models.TextField(blank=True, null=True, verbose_name='Plan > Step 4')),
            ],
            options={
                'verbose_name': 'Page > Applicants How It Works',
            },
        ),
        migrations.AlterModelOptions(
            name='whytoworkwithuspage',
            options={'verbose_name': 'Page > Why To Work With Us'},
        ),
    ]