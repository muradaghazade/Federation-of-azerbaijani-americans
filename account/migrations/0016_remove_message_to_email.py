# Generated by Django 3.1.5 on 2021-02-07 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='to_email',
        ),
    ]