# Generated by Django 3.2 on 2021-12-19 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_auto_20211219_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='notes',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]