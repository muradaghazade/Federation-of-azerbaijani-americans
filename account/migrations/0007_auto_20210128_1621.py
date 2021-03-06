# Generated by Django 3.1.5 on 2021-01-28 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20210128_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80, verbose_name='full name')),
                ('membership_id', models.CharField(max_length=15, unique=True, verbose_name='Membership id')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('birthday', models.DateField(verbose_name='Birthday')),
                ('phone_number', models.CharField(max_length=30, verbose_name='phone number')),
                ('citizenship', models.CharField(max_length=225, verbose_name='citizenship')),
                ('education', models.CharField(max_length=225, verbose_name='education')),
                ('current', models.CharField(max_length=225, verbose_name='current')),
                ('permoment', models.CharField(max_length=225, verbose_name='permoment')),
                ('member_of_ngo', models.CharField(max_length=225, verbose_name='member of ngo')),
                ('usa_year', models.IntegerField(null=True, verbose_name='usa year')),
                ('reasons', models.TextField(verbose_name='reasons')),
                ('mention', models.TextField(verbose_name='mention')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Donation User',
                'verbose_name_plural': 'Donation Users',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
