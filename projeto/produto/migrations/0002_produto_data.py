# Generated by Django 2.2.5 on 2019-09-06 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
    ]
