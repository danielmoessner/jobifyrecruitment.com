# Generated by Django 4.0.3 on 2022-05-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0061_alter_aboutpage_quote_size_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videoresumepage',
            name='video_title',
        ),
        migrations.RemoveField(
            model_name='videoresumepage',
            name='video_title_de',
        ),
        migrations.RemoveField(
            model_name='videoresumepage',
            name='video_title_en',
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_1',
            field=models.TextField(blank=True, verbose_name='Advantages > Text 1'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_1_de',
            field=models.TextField(blank=True, null=True, verbose_name='Advantages > Text 1'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_1_en',
            field=models.TextField(blank=True, null=True, verbose_name='Advantages > Text 1'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_2',
            field=models.TextField(blank=True, verbose_name='Advantages > Text 2'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_2_de',
            field=models.TextField(blank=True, null=True, verbose_name='Advantages > Text 2'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_2_en',
            field=models.TextField(blank=True, null=True, verbose_name='Advantages > Text 2'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_3',
            field=models.TextField(blank=True, verbose_name='Advantages > Text 3'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_3_de',
            field=models.TextField(blank=True, null=True, verbose_name='Advantages > Text 3'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_3_en',
            field=models.TextField(blank=True, null=True, verbose_name='Advantages > Text 3'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_4',
            field=models.TextField(blank=True, verbose_name='Advantages > Text 4'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_4_de',
            field=models.TextField(blank=True, null=True, verbose_name='Advantages > Text 4'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_4_en',
            field=models.TextField(blank=True, null=True, verbose_name='Advantages > Text 4'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_5',
            field=models.TextField(blank=True, verbose_name='Advantages > Text 5'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_5_de',
            field=models.TextField(blank=True, null=True, verbose_name='Advantages > Text 5'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_text_5_en',
            field=models.TextField(blank=True, null=True, verbose_name='Advantages > Text 5'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Advantages > Title'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_1',
            field=models.CharField(blank=True, max_length=200, verbose_name='Advantages > Title 1'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_1_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title 1'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_1_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title 1'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_2',
            field=models.CharField(blank=True, max_length=200, verbose_name='Advantages > Title 2'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_2_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title 2'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_2_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title 2'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_3',
            field=models.CharField(blank=True, max_length=200, verbose_name='Advantages > Title 3'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_3_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title 3'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_3_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title 3'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_4',
            field=models.CharField(blank=True, max_length=200, verbose_name='Advantages > Title 4'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_4_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title 4'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_4_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title 4'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_5',
            field=models.CharField(blank=True, max_length=200, verbose_name='Advantages > Title 5'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_5_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title 5'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_5_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title 5'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_de',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title'),
        ),
        migrations.AddField(
            model_name='videoresumepage',
            name='advantages_title_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Advantages > Title'),
        ),
    ]
