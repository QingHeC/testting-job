# Generated by Django 2.1.1 on 2019-08-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_interface', '0015_auto_20190724_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='req_list_data',
            name='file',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='req_list_data',
            name='headers',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='req_list_data',
            name='params',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
