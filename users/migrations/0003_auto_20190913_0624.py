# Generated by Django 2.2.4 on 2019-09-13 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190912_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='hood.NeighbourHood'),
        ),
    ]
