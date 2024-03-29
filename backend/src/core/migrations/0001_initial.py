# Generated by Django 5.0.1 on 2024-01-20 17:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('guid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(help_text='Nombre del Customer', max_length=32, unique=True, verbose_name='Nombre del Customer')),
            ],
            options={
                'verbose_name': 'Customers',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
