# Generated by Django 5.0.4 on 2024-04-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=15)),
                ('d_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
