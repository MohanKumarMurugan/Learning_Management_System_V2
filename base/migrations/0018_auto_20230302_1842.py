# Generated by Django 3.0.5 on 2023-03-02 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20230302_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('G_id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(default='images/user_image.png', upload_to='Gallery/%Y/%m/%d')),
                ('categories', models.CharField(max_length=200)),
                ('date', models.DateField(default=datetime.datetime(2023, 3, 2, 13, 12, 54, 286210, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='updated_date',
            field=models.DateField(default=datetime.datetime(2023, 3, 2, 13, 12, 54, 286210, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='classrooms',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 3, 2, 13, 12, 54, 286210, tzinfo=utc)),
        ),
    ]