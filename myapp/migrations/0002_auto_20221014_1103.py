# Generated by Django 3.2.12 on 2022-10-14 11:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeetable',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employeetable',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('45c97490-5b3d-4327-a719-ef17879858b6'), editable=False, primary_key=True, serialize=False),
        ),
    ]
