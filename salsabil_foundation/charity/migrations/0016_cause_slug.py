# Generated by Django 5.0.7 on 2024-08-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0015_alter_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True),
        ),
    ]
