# Generated by Django 5.1.2 on 2024-10-31 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0008_delete_post2_post_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]