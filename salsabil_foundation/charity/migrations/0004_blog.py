# Generated by Django 5.0.7 on 2024-08-03 11:25

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0003_event_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=150, null=True)),
                ('title', models.CharField(max_length=70)),
                ('message', models.TextField()),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=100, scale=None, size=[400, 300], upload_to='causes')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
