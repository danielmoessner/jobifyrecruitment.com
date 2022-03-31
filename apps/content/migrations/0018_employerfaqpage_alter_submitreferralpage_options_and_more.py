# Generated by Django 4.0.3 on 2022-03-25 12:25

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_videoresumepage_alter_servicespage_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerFaqPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_title', models.CharField(blank=True, max_length=100, verbose_name='Header > Title')),
                ('text_title', models.CharField(blank=True, max_length=200, verbose_name='Text > Title')),
                ('text_sub', models.CharField(blank=True, max_length=200, verbose_name='Text > Sub')),
                ('text_text', tinymce.models.HTMLField(blank=True, verbose_name='Text > Text')),
                ('faq_question_1', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 1')),
                ('faq_answer_1', models.TextField(blank=True, verbose_name='FAQ > Answer 1')),
                ('faq_question_2', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 2')),
                ('faq_answer_2', models.TextField(blank=True, verbose_name='FAQ > Answer 2')),
                ('faq_question_3', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 3')),
                ('faq_answer_3', models.TextField(blank=True, verbose_name='FAQ > Answer 3')),
                ('faq_question_4', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 4')),
                ('faq_answer_4', models.TextField(blank=True, verbose_name='FAQ > Answer 4')),
                ('faq_question_5', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 5')),
                ('faq_answer_5', models.TextField(blank=True, verbose_name='FAQ > Answer 5')),
                ('faq_question_6', models.CharField(blank=True, max_length=100, verbose_name='FAQ > Question 6')),
                ('faq_answer_6', models.TextField(blank=True, verbose_name='FAQ > Answer 6')),
            ],
            options={
                'verbose_name': 'Page > Employer FAQ',
            },
        ),
        migrations.AlterModelOptions(
            name='submitreferralpage',
            options={'verbose_name': 'Page > Submit A Referral'},
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='header_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='header_title_de',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='header_title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_button',
            field=models.CharField(blank=True, max_length=100, verbose_name='Plan > Button'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_button_de',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Plan > Button'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_button_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Plan > Button'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Plan > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_title_de',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Plan > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Plan > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_button',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Button'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_button_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Button'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_button_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Button'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_sub',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_sub_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_sub_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_text',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_text_de',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_text_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='text_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='header_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='text_sub',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='text_text',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='text_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='header_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='header_title_de',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='header_title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_button',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Button'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_button_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Button'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_button_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Button'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_left',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Text > Left'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_left_de',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Left'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_left_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Left'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_right',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Text > Right'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_right_de',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Right'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_right_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Right'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_sub',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_sub_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_sub_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='text_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_left_text',
            field=models.TextField(blank=True, verbose_name='Benefits > Text Left'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_left_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Benefits > Text Left'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_left_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Benefits > Text Left'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_left_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Benefits > Title Left'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_left_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Benefits > Title Left'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_left_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Benefits > Title Left'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_right_text',
            field=models.TextField(blank=True, verbose_name='Benefits > Text Right'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_right_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Benefits > Text Right'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_right_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Benefits > Text Right'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_right_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Benefits > Title Right'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_right_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Benefits > Title Right'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='benefits_right_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Benefits > Title Right'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='FAQ > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_title_de',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='FAQ > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='header_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='header_title_de',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='header_title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='text_sub',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='text_sub_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='text_sub_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='text_text',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='text_text_de',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='text_text_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='text_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='text_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='text_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='video_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Video > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='video_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Video > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='video_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Video > Title'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='header_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='header_title_de',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='header_title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_button',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Button'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_button_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Button'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_button_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Button'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_left',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Text > Left'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_left_de',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Left'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_left_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Left'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_right',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Text > Right'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_right_de',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Right'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_right_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Right'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_sub',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_sub_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_sub_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='text_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='header_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='header_title_de',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='header_title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_sub',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_sub_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_sub_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_text',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_text_de',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_text_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Text'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='text_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
    ]