# Generated by Django 2.1 on 2018-08-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='price',
            field=models.IntegerField(default=10, verbose_name='商品价格'),
        ),
    ]
