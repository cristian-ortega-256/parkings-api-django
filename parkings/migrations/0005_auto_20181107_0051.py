# Generated by Django 2.1.2 on 2018-11-07 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkings', '0004_configuration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuration',
            name='id',
        ),
        migrations.AlterField(
            model_name='configuration',
            name='key',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
