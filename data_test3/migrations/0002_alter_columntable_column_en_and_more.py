# Generated by Django 4.1.7 on 2023-05-09 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_test3', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='columntable',
            name='column_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='columntable',
            name='column_kr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='columntable',
            name='table_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
