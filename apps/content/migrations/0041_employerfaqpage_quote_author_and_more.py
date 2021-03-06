# Generated by Django 4.0.3 on 2022-05-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0040_aboutpage_quote_author_aboutpage_quote_author_de_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employerfaqpage',
            name='quote_author',
            field=models.CharField(blank=True, max_length=200, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='quote_author_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='quote_author_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='quote_text',
            field=models.TextField(blank=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='quote_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='quote_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='quote_author',
            field=models.CharField(blank=True, max_length=200, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='quote_author_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='quote_author_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='quote_text',
            field=models.TextField(blank=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='quote_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='quote_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='quote_author',
            field=models.CharField(blank=True, max_length=200, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='quote_author_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='quote_author_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='quote_text',
            field=models.TextField(blank=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='quote_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='quote_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='quote_author',
            field=models.CharField(blank=True, max_length=200, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='quote_author_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='quote_author_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='quote_text',
            field=models.TextField(blank=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='quote_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='quote_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='quote_author',
            field=models.CharField(blank=True, max_length=200, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='quote_author_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='quote_author_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Quote > Author'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='quote_text',
            field=models.TextField(blank=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='quote_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='quote_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Quote > Text'),
        ),
    ]
