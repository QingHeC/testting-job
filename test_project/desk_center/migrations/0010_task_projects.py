# Generated by Django 2.1.1 on 2019-04-03 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desk_center', '0009_list_user_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='task_projects',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pro_name', models.CharField(max_length=255)),
                ('pro_text', models.TextField(null=True)),
            ],
        ),
    ]
