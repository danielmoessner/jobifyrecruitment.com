# Generated by Django 4.0.3 on 2022-05-13 09:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0041_employerfaqpage_quote_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='salutation',
        ),
        migrations.AddField(
            model_name='applicant',
            name='currently_attend_school',
            field=models.BooleanField(default=False, verbose_name='I currently attend here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='degree',
            field=models.CharField(default='', max_length=200, verbose_name='Degree'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='field_of_study',
            field=models.CharField(default='', max_length=200, verbose_name='Field of Study'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='graduation_end_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Graduation End Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='graduation_start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Graduation Start Date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='profession',
            field=models.CharField(default='', max_length=200, verbose_name='Profession'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='school_location',
            field=models.CharField(default='', max_length=200, verbose_name='School Location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='school_name',
            field=models.CharField(default='', max_length=200, verbose_name='School Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='state_province',
            field=models.CharField(default='', max_length=100, verbose_name='State / Province'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='wanted_job_title',
            field=models.CharField(default='', max_length=200, verbose_name='Wanted Job Title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language1',
            field=models.CharField(max_length=50, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language1knowledge',
            field=models.CharField(choices=[('MOTHER', 'Mother tongue'), ('FLUENT', 'Fluent'), ('GOOD', 'Good'), ('BASIC', 'Basic')], max_length=50, verbose_name='Knowledge'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language2',
            field=models.CharField(blank=True, max_length=50, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language2knowledge',
            field=models.CharField(blank=True, choices=[('MOTHER', 'Mother tongue'), ('FLUENT', 'Fluent'), ('GOOD', 'Good'), ('BASIC', 'Basic')], max_length=50, verbose_name='Knowledge'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language3',
            field=models.CharField(blank=True, max_length=50, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language3knowledge',
            field=models.CharField(blank=True, choices=[('MOTHER', 'Mother tongue'), ('FLUENT', 'Fluent'), ('GOOD', 'Good'), ('BASIC', 'Basic')], max_length=50, verbose_name='Knowledge'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language4',
            field=models.CharField(blank=True, max_length=50, verbose_name='Language'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language4knowledge',
            field=models.CharField(blank=True, choices=[('MOTHER', 'Mother tongue'), ('FLUENT', 'Fluent'), ('GOOD', 'Good'), ('BASIC', 'Basic')], max_length=50, verbose_name='Knowledge'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='postal',
            field=models.CharField(max_length=10, verbose_name='Zip Code'),
        ),
    ]