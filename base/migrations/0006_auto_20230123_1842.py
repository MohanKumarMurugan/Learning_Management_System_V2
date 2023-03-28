# Generated by Django 3.2.4 on 2023-01-23 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20230122_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_image', models.CharField(max_length=200)),
                ('class_name', models.CharField(max_length=200)),
                ('subject_code', models.CharField(max_length=200, unique=True)),
                ('semester', models.IntegerField()),
                ('department', models.CharField(max_length=200)),
                ('discription', models.CharField(default='No Discription yet.', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='details',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 1, 23, 13, 11, 59, 703873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='faculty_details',
            name='date_of_join',
            field=models.DateField(default=datetime.datetime(2023, 1, 23, 13, 11, 59, 703873, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 23, 13, 11, 59, 703873, tzinfo=utc)),
        ),
    ]