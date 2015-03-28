# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('dni', models.CharField(help_text=b'Enter dni.', max_length=250, verbose_name=b'Address')),
                ('phone', models.CharField(default=b'', help_text=b'Enter phone.', max_length=250, verbose_name=b'Phone')),
                ('operador', models.CharField(default=b'', help_text=b'Enter operador.', max_length=250, verbose_name=b'Phone')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
    ]
