# Generated by Django 5.0.4 on 2024-05-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0009_alter_submissions_d_id_alter_submissions_sub_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissions',
            name='sub_id',
            field=models.IntegerField(unique=True),
        ),
    ]