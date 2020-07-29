# Generated by Django 3.0.8 on 2020-07-29 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('Owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
