# Generated by Django 5.1 on 2024-09-03 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]
