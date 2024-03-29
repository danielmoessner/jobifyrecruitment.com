# Generated by Django 4.0.3 on 2022-09-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0076_submitreferralpage_email_html_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=1000)),
                ('text', models.TextField()),
                ('ordering', models.IntegerField(default=0)),
                ('show', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
                'ordering': ['ordering'],
            },
        ),
        migrations.AddField(
            model_name='applicant',
            name='preview',
            field=models.ImageField(blank=True, null=True, upload_to='content/applicant/preview/'),
        ),
    ]
