# Generated by Django 2.0.7 on 2018-07-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180718_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='userapi',
            name='api_key',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
