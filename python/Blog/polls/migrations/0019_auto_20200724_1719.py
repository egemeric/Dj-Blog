# Generated by Django 3.0.8 on 2020-07-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20200724_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Ip_log',
            field=models.GenericIPAddressField(null=True),
        ),
    ]