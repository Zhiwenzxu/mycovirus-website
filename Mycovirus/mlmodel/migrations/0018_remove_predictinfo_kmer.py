# Generated by Django 2.1.5 on 2020-08-27 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mlmodel', '0017_auto_20200724_0502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='predictinfo',
            name='kmer',
        ),
    ]