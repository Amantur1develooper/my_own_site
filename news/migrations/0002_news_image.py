# Generated by Django 5.0.2 on 2024-02-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to='news_images/', verbose_name='изображение'),
        ),
    ]
