# Generated by Django 2.2.4 on 2019-09-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_auto_20190914_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='image',
            field=models.ImageField(default='', upload_to='business_posters/'),
        ),
    ]
