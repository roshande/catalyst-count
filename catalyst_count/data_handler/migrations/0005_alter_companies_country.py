# Generated by Django 3.2.5 on 2021-07-17 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_handler', '0004_auto_20210717_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
