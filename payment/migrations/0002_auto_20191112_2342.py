# Generated by Django 2.2.1 on 2019-11-12 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='paytm',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='phone_pay',
        ),
    ]