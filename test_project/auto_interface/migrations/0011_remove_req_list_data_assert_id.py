# Generated by Django 2.1.1 on 2019-05-12 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto_interface', '0010_auto_20190504_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='req_list_data',
            name='assert_id',
        ),
    ]
