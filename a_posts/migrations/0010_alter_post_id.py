# Generated by Django 5.1.2 on 2024-10-31 13:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_posts', '0009_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
