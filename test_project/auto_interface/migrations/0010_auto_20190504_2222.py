# Generated by Django 2.1.1 on 2019-05-04 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_interface', '0009_auto_20190504_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='req_list_data',
            name='agreement',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='req_list_data',
            name='assert_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
