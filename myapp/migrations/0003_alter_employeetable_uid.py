# Generated by Django 3.2.12 on 2022-10-18 05:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20221014_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetable',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('4b41d034-bd97-40f5-a9bb-885df3ef19ec'), editable=False, primary_key=True, serialize=False),
        ),
    ]
