# Generated by Django 4.1.7 on 2023-05-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_test', '0002_alter_statusmodel_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusmodel',
            name='last_value',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
