# Generated by Django 2.0.7 on 2018-07-18 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapi',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userapi',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]