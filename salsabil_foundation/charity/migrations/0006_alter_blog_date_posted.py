# Generated by Django 5.0.7 on 2024-08-03 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0005_alter_blog_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
