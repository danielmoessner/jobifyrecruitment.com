# Generated by Django 4.0.3 on 2022-03-25 12:33

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0018_employerfaqpage_alter_submitreferralpage_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_1_de',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 1'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_1_en',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 1'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_2_de',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 2'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_2_en',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 2'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_3_de',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 3'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_3_en',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 3'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_4_de',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 4'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_4_en',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 4'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_5_de',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 5'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_5_en',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 5'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_6_de',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 6'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_answer_6_en',
            field=models.TextField(blank=True, null=True, verbose_name='FAQ > Answer 6'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_1_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 1'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_1_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 1'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_2_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 2'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_2_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 2'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_3_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 3'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_3_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 3'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_4_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 4'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_4_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 4'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_5_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 5'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_5_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 5'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_6_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 6'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='faq_question_6_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 6'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='header_title_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='header_title_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='text_sub_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='text_sub_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Sub'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='text_text_de',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Text'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='text_text_en',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text > Text'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='text_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='text_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Text > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='header_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='header_title_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='header_title_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_button',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Plan > Button'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_button_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Plan > Button'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_button_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Plan > Button'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Plan > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_title_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Plan > Title'),
        ),
        migrations.AlterField(
            model_name='applicantshowitworkspage',
            name='plan_title_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Plan > Title'),
        ),
        migrations.AlterField(
            model_name='employerfaqpage',
            name='faq_question_1',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 1'),
        ),
        migrations.AlterField(
            model_name='employerfaqpage',
            name='faq_question_2',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 2'),
        ),
        migrations.AlterField(
            model_name='employerfaqpage',
            name='faq_question_3',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 3'),
        ),
        migrations.AlterField(
            model_name='employerfaqpage',
            name='faq_question_4',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 4'),
        ),
        migrations.AlterField(
            model_name='employerfaqpage',
            name='faq_question_5',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 5'),
        ),
        migrations.AlterField(
            model_name='employerfaqpage',
            name='faq_question_6',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 6'),
        ),
        migrations.AlterField(
            model_name='employerfaqpage',
            name='header_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='service',
            name='name_de',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='name_en',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='service',
            name='title_de',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='title_en',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='servicespage',
            name='header_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='staffcategory',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='staffcategory',
            name='name_de',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='staffcategory',
            name='name_en',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_1',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 1'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_1_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 1'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_1_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 1'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_2',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 2'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_2_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 2'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_2_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 2'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_3',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 3'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_3_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 3'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_3_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 3'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_4',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 4'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_4_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 4'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_4_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 4'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_5',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 5'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_5_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 5'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_5_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 5'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_6',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 6'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_6_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 6'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_question_6_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 6'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_title',
            field=models.CharField(max_length=1000, verbose_name='FAQ > Title'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_title_de',
            field=models.CharField(max_length=1000, null=True, verbose_name='FAQ > Title'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='faq_title_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='FAQ > Title'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='header_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='header_title_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='submitreferralpage',
            name='header_title_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_1',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 1'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_1_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 1'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_1_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 1'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_2',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 2'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_2_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 2'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_2_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 2'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_3',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 3'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_3_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 3'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_3_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 3'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_4',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 4'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_4_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 4'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_4_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 4'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_5',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 5'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_5_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 5'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_5_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 5'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_6',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Question 6'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_6_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 6'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_question_6_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Question 6'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='FAQ > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_title_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='faq_title_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='FAQ > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='header_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='header_title_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='videoresumepage',
            name='header_title_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='header_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='header_title_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='whytoworkwithuspage',
            name='header_title_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='header_title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='header_title_de',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
        migrations.AlterField(
            model_name='workinginaustriapage',
            name='header_title_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Header > Title'),
        ),
    ]