# Generated by Django 4.1 on 2023-10-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repodata',
            name='dataFile',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m'),
        ),
    ]
