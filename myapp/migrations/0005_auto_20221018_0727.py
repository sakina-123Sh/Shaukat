# Generated by Django 3.2.12 on 2022-10-18 07:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20221018_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetable',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('72289b62-58e3-4fe5-b1a3-3c03a3e0d8c9'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='timingcreatetable',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('72289b62-58e3-4fe5-b1a3-3c03a3e0d8c9'), editable=False, primary_key=True, serialize=False),
        ),
    ]
