# Generated by Django 2.2.3 on 2019-08-07 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseapp', '0003_member_member_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_name',
            field=models.CharField(max_length=20),
        ),
    ]