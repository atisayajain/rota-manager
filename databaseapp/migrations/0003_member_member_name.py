# Generated by Django 2.2.3 on 2019-08-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseapp', '0002_auto_20190721_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_name',
            field=models.CharField(default='', editable=False, max_length=20),
        ),
    ]
