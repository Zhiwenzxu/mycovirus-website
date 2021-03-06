# Generated by Django 3.0.3 on 2020-02-26 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlmodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileinfo',
            name='kmer',
            field=models.CharField(blank=True, help_text='Enter one or more kmers here if you want to analyze certain kmers. Please separate each kmer by a comma.', max_length=200, null=True, verbose_name='Kmer (optional)'),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='kmer_size',
            field=models.IntegerField(blank=True, help_text='If you have kmers with different length, please keep this box blank.', max_length=200, null=True, verbose_name='Kmer size (optional)'),
        ),
    ]
