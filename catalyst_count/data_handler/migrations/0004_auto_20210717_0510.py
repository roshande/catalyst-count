# Generated by Django 3.2.5 on 2021-07-17 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_handler', '0003_auto_20210717_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='linkedin_url',
            field=models.URLField(max_length=255),
        ),
        migrations.AlterField(
            model_name='companies',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
