# Generated by Django 4.1.5 on 2023-02-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GYMapp', '0004_rename_update_at_gymusers_updated_at_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='_to',
            field=models.DateTimeField(null=True),
        ),
    ]
