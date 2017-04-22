# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='description',
            field=models.TextField(blank=True, help_text='If your proposal is accepted this will be made public and printed in the program. Should be one paragraph, maximum 400 characters.', max_length=400, verbose_name='Brief Description'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='abstract',
            field=models.TextField(help_text="Detailed outline. Will be made public if your proposal is accepted. Edit using <a href='http://daringfireball.net/projects/markdown/basics' target='_blank'>Markdown</a>.", verbose_name='Detailed Abstract'),
        ),
    ]