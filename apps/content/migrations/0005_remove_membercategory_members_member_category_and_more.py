# Generated by Django 4.0.3 on 2022-04-07 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_member_created_member_updated_membercategory_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membercategory',
            name='members',
        ),
        migrations.AddField(
            model_name='member',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='content.membercategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='role',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='MemberCategoryConnection',
        ),
    ]
