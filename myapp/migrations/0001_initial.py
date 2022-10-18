# Generated by Django 3.2.12 on 2022-10-14 11:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeTable',
            fields=[
                ('created_at', models.DateField(auto_created=True)),
                ('uid', models.UUIDField(default=uuid.UUID('0d30b8a1-a3da-473f-85f2-baaf06b1c27f'), editable=False, primary_key=True, serialize=False)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('company_name', models.CharField(max_length=100)),
                ('emp_fname', models.CharField(max_length=200)),
                ('emp_lname', models.CharField(max_length=50)),
                ('emp_DOB', models.DateField()),
                ('emp_phone', models.IntegerField()),
                ('emp_id', models.IntegerField()),
                ('emp_email', models.EmailField(max_length=254)),
                ('aboutUS', models.TextField()),
                ('is_done', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]