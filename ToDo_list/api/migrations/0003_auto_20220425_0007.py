# Generated by Django 3.0.14 on 2022-04-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220420_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='list_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
