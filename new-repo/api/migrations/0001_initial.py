# Generated by Django 4.1 on 2023-06-01 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('email', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=10)),
                ('LastName', models.CharField(max_length=10)),
                ('Mobno', models.CharField(max_length=10)),
            ],
        ),
    ]
