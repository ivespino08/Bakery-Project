# Generated by Django 3.2.3 on 2021-05-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210522_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oquantity', models.IntegerField(db_column='OQuantity')),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
    ]