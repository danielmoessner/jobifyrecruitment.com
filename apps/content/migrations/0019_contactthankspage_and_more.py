# Generated by Django 4.0.3 on 2022-04-14 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0018_applicantshowitworkspage_quote_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactThanksPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thanks_title', models.CharField(blank=True, max_length=200, verbose_name='Thanks > Title')),
                ('thanks_title_de', models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Title')),
                ('thanks_title_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Title')),
                ('thanks_text', models.TextField(blank=True, verbose_name='Thanks > Text')),
                ('thanks_text_de', models.TextField(blank=True, null=True, verbose_name='Thanks > Text')),
                ('thanks_text_en', models.TextField(blank=True, null=True, verbose_name='Thanks > Text')),
                ('thanks_button', models.CharField(blank=True, max_length=200, verbose_name='Thanks > Button')),
                ('thanks_button_de', models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Button')),
                ('thanks_button_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Button')),
            ],
            options={
                'verbose_name': 'Page > Contact Thanks',
            },
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='thanks_button',
            field=models.CharField(blank=True, max_length=200, verbose_name='Thanks > Button'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='thanks_button_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Button'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='thanks_button_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Button'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='thanks_text',
            field=models.TextField(blank=True, verbose_name='Thanks > Text'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='thanks_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Thanks > Text'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='thanks_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Thanks > Text'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='thanks_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Thanks > Title'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='thanks_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Title'),
        ),
        migrations.AddField(
            model_name='initiativeapplicationthankspage',
            name='thanks_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Title'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='thanks_button',
            field=models.CharField(blank=True, max_length=200, verbose_name='Thanks > Button'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='thanks_button_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Button'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='thanks_button_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Button'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='thanks_text',
            field=models.TextField(blank=True, verbose_name='Thanks > Text'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='thanks_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Thanks > Text'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='thanks_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Thanks > Text'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='thanks_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Thanks > Title'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='thanks_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Title'),
        ),
        migrations.AddField(
            model_name='submitpositionthankspage',
            name='thanks_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Title'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='thanks_button',
            field=models.CharField(blank=True, max_length=200, verbose_name='Thanks > Button'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='thanks_button_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Button'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='thanks_button_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Button'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='thanks_text',
            field=models.TextField(blank=True, verbose_name='Thanks > Text'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='thanks_text_de',
            field=models.TextField(blank=True, null=True, verbose_name='Thanks > Text'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='thanks_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Thanks > Text'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='thanks_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Thanks > Title'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='thanks_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Title'),
        ),
        migrations.AddField(
            model_name='submitreferralthankspage',
            name='thanks_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Thanks > Title'),
        ),
    ]
