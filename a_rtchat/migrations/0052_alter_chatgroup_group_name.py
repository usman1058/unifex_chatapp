# Generated by Django 5.1.2 on 2024-11-09 09:29

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_rtchat', '0051_groupmessage_file_alter_chatgroup_group_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatgroup',
            name='group_name',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=124, unique=True),
        ),
    ]
