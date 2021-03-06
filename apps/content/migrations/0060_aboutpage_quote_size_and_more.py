# Generated by Django 4.0.3 on 2022-05-18 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0059_videoresumepage_benefits_center_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='applicantshowitworkspage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='employerfaqpage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='employerhowitworkspage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='indexpage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationpage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='jobseekerfaqpage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='portalpage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='servicespage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='staffingsolutionspage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='submitpositionpage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='submitreferralpage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='whytoworkwithuspage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
        migrations.AddField(
            model_name='workinginaustriapage',
            name='quote_size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('NORMAL', 'Normal'), ('LARGE', 'Large')], default='NORMAL', max_length=100, verbose_name='Quote > Size'),
        ),
    ]
