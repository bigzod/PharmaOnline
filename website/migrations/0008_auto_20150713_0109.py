# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20150712_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacie',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
    ]
