# Generated by Django 3.1.7 on 2021-05-26 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplements',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='supplements',
            name='side_effects',
            field=models.CharField(max_length=500),
        ),
    ]
