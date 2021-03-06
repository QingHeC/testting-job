# Generated by Django 2.1.1 on 2019-03-31 20:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auto_interface', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interface_asserts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('assert_name', models.CharField(max_length=255)),
                ('lef_NO_num', models.IntegerField()),
                ('left_contrast', models.CharField(max_length=255)),
                ('right_NO_num', models.IntegerField()),
                ('right_contrast', models.CharField(max_length=255)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
