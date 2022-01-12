# Generated by Django 3.2 on 2021-12-26 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_auto_20211226_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='fills',
        ),
        migrations.AddField(
            model_name='prescription',
            name='fills',
            field=models.ManyToManyField(blank=True, to='patients.Filled'),
        ),
    ]