# Generated by Django 3.2 on 2021-12-26 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='businessProfile',
            field=models.ImageField(blank=True, default='home.png', null=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='provider',
            name='profilePic',
            field=models.ImageField(blank=True, default='logo2.png', null=None, upload_to=''),
        ),
    ]
