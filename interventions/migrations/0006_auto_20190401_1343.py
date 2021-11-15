# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interventions', '0005_auto_20190206_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='leader_has_coc',
            field=models.NullBooleanField(help_text='Iedereen die op een school werkt moet in het bezit         zijn van een Verklaring Omtrent Gedrag (VOG, zie         <a href="https://www.justis.nl/producten/vog/"         target="_blank">https://www.justis.nl/producten/vog/</a>).         Het is de verantwoordelijkheid van de school om hierom te vragen.         Deelkracht neemt hierin een adviserende rol en wil de onderzoekers         waarschuwen dat de school om een VOG kan vragen.', verbose_name='Is de testleider in het bezit van een VOG?'),
        ),
    ]
