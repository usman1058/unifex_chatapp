# Generated by Django 5.1.2 on 2024-11-01 12:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0015_alter_comment_options_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='parent_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='a_posts.comment'),
        ),
    ]
