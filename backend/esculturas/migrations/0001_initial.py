# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escultura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_api', models.CharField(max_length=60, blank=True)),
                ('imagen', models.ImageField(upload_to=b'360images')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
