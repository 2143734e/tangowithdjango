# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150126_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='student_name',
            field=models.IntegerField(default=2143734),
            preserve_default=True,
        ),
    ]
