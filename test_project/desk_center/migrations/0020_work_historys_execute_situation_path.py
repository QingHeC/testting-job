# Generated by Django 2.1.1 on 2019-06-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk_center', '0019_auto_20190616_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_historys',
            name='execute_situation_path',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
