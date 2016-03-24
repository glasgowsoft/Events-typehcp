# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='e',
            name='attendees',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True, related_name='bookedin'),
        ),
    ]
