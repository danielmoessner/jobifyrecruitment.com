# Generated by Django 4.0.3 on 2022-03-25 11:22

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_workinginaustriapage'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoResumePage',
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
                ('text_text', tinymce.models.HTMLField(verbose_name='Text > Text')),
                ('text_text_de', tinymce.models.HTMLField(null=True, verbose_name='Text > Text')),
                ('text_text_en', tinymce.models.HTMLField(null=True, verbose_name='Text > Text')),
                ('benefits_left_title', models.CharField(max_length=200, verbose_name='Benefits > Title Left')),
                ('benefits_left_title_de', models.CharField(max_length=200, null=True, verbose_name='Benefits > Title Left')),
                ('benefits_left_title_en', models.CharField(max_length=200, null=True, verbose_name='Benefits > Title Left')),
                ('benefits_left_text', models.TextField(verbose_name='Benefits > Text Left')),
                ('benefits_left_text_de', models.TextField(null=True, verbose_name='Benefits > Text Left')),
                ('benefits_left_text_en', models.TextField(null=True, verbose_name='Benefits > Text Left')),
                ('benefits_right_title', models.CharField(max_length=200, verbose_name='Benefits > Title Right')),
                ('benefits_right_title_de', models.CharField(max_length=200, null=True, verbose_name='Benefits > Title Right')),
                ('benefits_right_title_en', models.CharField(max_length=200, null=True, verbose_name='Benefits > Title Right')),
                ('benefits_right_text', models.TextField(verbose_name='Benefits > Text Right')),
                ('benefits_right_text_de', models.TextField(null=True, verbose_name='Benefits > Text Right')),
                ('benefits_right_text_en', models.TextField(null=True, verbose_name='Benefits > Text Right')),
                ('video_title', models.CharField(max_length=200, verbose_name='Video > Title')),
                ('video_title_de', models.CharField(max_length=200, null=True, verbose_name='Video > Title')),
                ('video_title_en', models.CharField(max_length=200, null=True, verbose_name='Video > Title')),
                ('faq_title', models.CharField(max_length=100, verbose_name='FAQ > Title')),
                ('faq_title_de', models.CharField(max_length=100, null=True, verbose_name='FAQ > Title')),
                ('faq_title_en', models.CharField(max_length=100, null=True, verbose_name='FAQ > Title')),
                ('faq_question_1', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 1')),
                ('faq_question_1_de', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 1')),
                ('faq_question_1_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 1')),
                ('faq_answer_1', models.TextField(blank=True, verbose_name='FAQ > Answer 1')),
                ('faq_answer_1_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 1')),
                ('faq_answer_1_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 1')),
                ('faq_question_2', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 2')),
                ('faq_question_2_de', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 2')),
                ('faq_question_2_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 2')),
                ('faq_answer_2', models.TextField(blank=True, verbose_name='FAQ > Answer 2')),
                ('faq_answer_2_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 2')),
                ('faq_answer_2_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 2')),
                ('faq_question_3', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 3')),
                ('faq_question_3_de', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 3')),
                ('faq_question_3_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 3')),
                ('faq_answer_3', models.TextField(blank=True, verbose_name='FAQ > Answer 3')),
                ('faq_answer_3_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 3')),
                ('faq_answer_3_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 3')),
                ('faq_question_4', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 4')),
                ('faq_question_4_de', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 4')),
                ('faq_question_4_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 4')),
                ('faq_answer_4', models.TextField(blank=True, verbose_name='FAQ > Answer 4')),
                ('faq_answer_4_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 4')),
                ('faq_answer_4_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 4')),
                ('faq_question_5', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 5')),
                ('faq_question_5_de', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 5')),
                ('faq_question_5_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 5')),
                ('faq_answer_5', models.TextField(blank=True, verbose_name='FAQ > Answer 5')),
                ('faq_answer_5_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 5')),
                ('faq_answer_5_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 5')),
                ('faq_question_6', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 6')),
                ('faq_question_6_de', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 6')),
                ('faq_question_6_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Question 6')),
                ('faq_answer_6', models.TextField(blank=True, verbose_name='FAQ > Answer 6')),
                ('faq_answer_6_de', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 6')),
                ('faq_answer_6_en', models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 6')),
            ],
            options={
                'verbose_name': 'Page > Video Resume',
            },
        ),
        migrations.AlterModelOptions(
            name='servicespage',
            options={'verbose_name': 'Page > Courses'},
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_text',
            field=tinymce.models.HTMLField(verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_text_de',
            field=tinymce.models.HTMLField(null=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_text_en',
            field=tinymce.models.HTMLField(null=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='text_text',
            field=tinymce.models.HTMLField(verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_text',
            field=tinymce.models.HTMLField(verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_text_de',
            field=tinymce.models.HTMLField(null=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_text_en',
            field=tinymce.models.HTMLField(null=True, verbose_name='Text > Text'),
        ),
    ]