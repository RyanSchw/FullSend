# Generated by Django 2.2.3 on 2019-07-26 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverauthentication',
            name='token_expires',
            field=models.IntegerField(),
        ),
    ]