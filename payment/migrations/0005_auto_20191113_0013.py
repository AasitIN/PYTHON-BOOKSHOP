# Generated by Django 2.2.1 on 2019-11-13 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20191113_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_holder_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='payment',
            name='card_no',
            field=models.CharField(max_length=21),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paytm',
            field=models.CharField(default=0, max_length=11),
        ),
        migrations.AlterField(
            model_name='payment',
            name='phone_pay',
            field=models.CharField(default=0, max_length=11),
        ),
    ]
