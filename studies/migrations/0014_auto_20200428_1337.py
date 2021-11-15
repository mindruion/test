# Generated by Django 2.2.12 on 2020-04-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0013_auto_20190401_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='has_traits',
            field=models.BooleanField(blank=True, null=True, verbose_name='Deelnemers kunnen geïncludeerd worden op bepaalde bijzondere kenmerken. Is dit in uw studie bij (een deel van) de deelnemers het geval?'),
        ),
        migrations.AlterField(
            model_name='study',
            name='passive_consent',
            field=models.BooleanField(blank=True, help_text='Wanneer u kinderen via een instelling (dus ook school) werft en u de ouders niet laat ondertekenen, maar in plaats daarvan de leiding van die instelling, dan maakt u gebruik van passieve informed consent. U kunt de templates vinden op <a href="https://Deelkracht.wp.hum.uu.nl/toestemmingsverklaringen/" target="_blank">Deelkracht-website</a>.', null=True, verbose_name='Maakt u gebruik van passieve informed consent?'),
        ),
    ]
