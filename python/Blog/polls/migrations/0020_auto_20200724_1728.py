# Generated by Django 3.0.8 on 2020-07-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20200724_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='User_agent',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
