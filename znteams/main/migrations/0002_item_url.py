# Generated by Django 4.2.6 on 2023-10-31 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='URL',
            field=models.URLField(blank=True, null=True),
        ),
    ]
