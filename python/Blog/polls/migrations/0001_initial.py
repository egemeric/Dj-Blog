# Generated by Django 3.0.8 on 2020-07-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('Emb_html', models.CharField(blank=True, max_length=2024, null=True)),
                ('Content', models.TextField(default='Empty')),
                ('File', models.FileField(blank=True, default='media/None/', null=True, upload_to='media/uploads/')),
                ('Image', models.ImageField(default='media/None/no-img.jpg', upload_to='media/pic_folder')),
                ('Ip_log', models.GenericIPAddressField(null=True)),
                ('User_agent', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
