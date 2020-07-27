# Generated by Django 3.0.8 on 2020-07-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_comment_user_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Ip_log',
            field=models.GenericIPAddressField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='User_agent',
            field=models.CharField(max_length=200),
        ),
    ]
