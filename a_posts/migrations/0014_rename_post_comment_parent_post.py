# Generated by Django 5.1.2 on 2024-11-01 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0013_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='parent_post',
        ),
    ]
