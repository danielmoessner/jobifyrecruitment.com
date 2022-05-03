# Generated by Django 4.0.3 on 2022-05-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0030_whytoworkwithuspage_quote_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitreferralpage',
            name='quote_author',
            field=models.CharField(blank=True, max_length=500, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='quote_author_de',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='quote_author_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='quote_text',
            field=models.TextField(blank=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='quote_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='quote_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
    ]
