# Generated by Django 4.1.7 on 2023-06-07 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppDownloadLogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.TextField(blank=True, null=True)),
                ('start_date', models.TextField(blank=True, null=True)),
                ('end_date', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('reg_dtm', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'app_download_log',
            },
        ),
        migrations.CreateModel(
            name='AppInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('save_dir', models.TextField(blank=True, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('start_date', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'app_info',
            },
        ),
    ]
