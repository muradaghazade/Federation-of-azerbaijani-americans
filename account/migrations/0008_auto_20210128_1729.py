# Generated by Django 3.1.5 on 2021-01-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20210128_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donationuser',
            name='membership_id',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Membership id'),
        ),
    ]
