# Generated by Django 3.1.4 on 2020-12-11 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweetsnax', '0003_auto_20201211_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.date(2020, 12, 11), null=True),
        ),
    ]
