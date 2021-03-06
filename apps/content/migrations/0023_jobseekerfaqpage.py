# Generated by Django 4.0.3 on 2022-04-25 09:07

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0022_indexpage_initiativeapplicationpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeekerFaqPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.CharField(blank=True, max_length=1000, verbose_name='Header > Title')),
                ('header_title_de', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title')),
                ('header_title_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title')),
                ('text_title', models.CharField(blank=True, max_length=200, verbose_name='Text > Title')),
                ('text_title_de', models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title')),
                ('text_title_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title')),
                ('text_sub', models.CharField(blank=True, max_length=200, verbose_name='Text > Sub')),
                ('text_sub_de', models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub')),
                ('text_sub_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub')),
                ('text_text', tinymce.models.HTMLField(blank=True, verbose_name='Text > Text')),
                ('text_text_de', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Text')),
                ('text_text_en', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Text')),
                ('faq_question_1', models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 1')),
                ('faq_question_1_de', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 1')),
                ('faq_question_1_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 1')),
                ('faq_answer_1', models.TextField(blank=True, verbose_name='FAQ > Answer 1')),
                ('faq_answer_1_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 1')),
                ('faq_answer_1_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 1')),
                ('faq_question_2', models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 2')),
                ('faq_question_2_de', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 2')),
                ('faq_question_2_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 2')),
                ('faq_answer_2', models.TextField(blank=True, verbose_name='FAQ > Answer 2')),
                ('faq_answer_2_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 2')),
                ('faq_answer_2_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 2')),
                ('faq_question_3', models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 3')),
                ('faq_question_3_de', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 3')),
                ('faq_question_3_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 3')),
                ('faq_answer_3', models.TextField(blank=True, verbose_name='FAQ > Answer 3')),
                ('faq_answer_3_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 3')),
                ('faq_answer_3_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 3')),
                ('faq_question_4', models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 4')),
                ('faq_question_4_de', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 4')),
                ('faq_question_4_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 4')),
                ('faq_answer_4', models.TextField(blank=True, verbose_name='FAQ > Answer 4')),
                ('faq_answer_4_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 4')),
                ('faq_answer_4_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 4')),
                ('faq_question_5', models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 5')),
                ('faq_question_5_de', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 5')),
                ('faq_question_5_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 5')),
                ('faq_answer_5', models.TextField(blank=True, verbose_name='FAQ > Answer 5')),
                ('faq_answer_5_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 5')),
                ('faq_answer_5_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 5')),
                ('faq_question_6', models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 6')),
                ('faq_question_6_de', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 6')),
                ('faq_question_6_en', models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 6')),
                ('faq_answer_6', models.TextField(blank=True, verbose_name='FAQ > Answer 6')),
                ('faq_answer_6_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 6')),
                ('faq_answer_6_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 6')),
            ],
            options={
                'verbose_name': 'Page > Job Seeker FAQ',
            },
        ),
    ]
