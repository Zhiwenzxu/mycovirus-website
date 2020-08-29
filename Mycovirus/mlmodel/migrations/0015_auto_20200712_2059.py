# Generated by Django 2.1.5 on 2020-07-12 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlmodel', '0014_filelistinfo_alignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictinfo',
            name='mlmodels',
            field=models.CharField(choices=[('kmeans', (('kmeansPCA', 'PCA'), ('kmeansTSNE', 'TSNE'), ('kmeansMeanshiftPCA', 'Meanshift PCA'), ('kmeansMeanshiftTSNE', 'Meanshift TSNE'))), ('unknown', (('Unknown', 'Unknown'), ('Unknown2', 'Unknown2')))], default='kmeansPCA', max_length=30),
        ),
    ]