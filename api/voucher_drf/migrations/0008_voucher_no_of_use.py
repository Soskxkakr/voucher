# Generated by Django 3.1.1 on 2020-09-19 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voucher_drf', '0007_voucher_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucher',
            name='no_of_use',
            field=models.PositiveIntegerField(default=0),
        ),
    ]