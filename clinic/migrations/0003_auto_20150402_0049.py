# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0002_auto_20150402_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='phone_numebr',
            new_name='phone_number',
        ),
    ]
