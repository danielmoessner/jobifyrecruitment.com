# Generated by Django 4.0.3 on 2022-04-22 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0019_contactthankspage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='area_of_expertise',
        ),
        migrations.AddField(
            model_name='applicant',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='applicants', to='content.staffcategory'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='experience',
            field=models.CharField(choices=[('1', '1 Year'), ('5', '1 to 5 Years'), ('10', '5 to 10 Years'), ('MAX', 'More Than 10 Years')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language1knowledge',
            field=models.CharField(choices=[('MOTHER', 'Mother tongue'), ('FLUENT', 'Fluent'), ('GOOD', 'Good'), ('BASIC', 'Basic')], max_length=50),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language2knowledge',
            field=models.CharField(blank=True, choices=[('MOTHER', 'Mother tongue'), ('FLUENT', 'Fluent'), ('GOOD', 'Good'), ('BASIC', 'Basic')], max_length=50),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language3knowledge',
            field=models.CharField(blank=True, choices=[('MOTHER', 'Mother tongue'), ('FLUENT', 'Fluent'), ('GOOD', 'Good'), ('BASIC', 'Basic')], max_length=50),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='language4knowledge',
            field=models.CharField(blank=True, choices=[('MOTHER', 'Mother tongue'), ('FLUENT', 'Fluent'), ('GOOD', 'Good'), ('BASIC', 'Basic')], max_length=50),
        ),
    ]