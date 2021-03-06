# Generated by Django 3.1.5 on 2021-02-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20210207_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=80, verbose_name='Subject')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('to_email', models.CharField(blank=True, max_length=80, verbose_name='to email')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
    ]
