# Generated by Django 5.1.2 on 2024-10-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0006_rename_image_post2_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='a_posts.tag'),
        ),
    ]