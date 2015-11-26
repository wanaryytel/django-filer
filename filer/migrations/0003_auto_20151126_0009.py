# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language_code', models.CharField(verbose_name='Language', choices=[('lt', 'Lithuanian'), ('en', 'English')], max_length=15, db_index=True)),
                ('name', models.CharField(verbose_name='name', blank=True, default='', max_length=255)),
                ('description', models.TextField(verbose_name='description', null=True, blank=True)),
                ('master', models.ForeignKey(null=True, related_name='translations', editable=False, to='filer.File')),
            ],
            options={
                'verbose_name': 'file Translation',
                'default_permissions': (),
                'db_table': 'filer_file_translation',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='filetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.RemoveField(
            model_name='file',
            name='description',
        ),
        migrations.RemoveField(
            model_name='file',
            name='name',
        ),
    ]
