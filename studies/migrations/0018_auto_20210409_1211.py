# Generated by Django 2.2.18 on 2021-04-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0017_auto_20210302_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='passive_consent',
            field=models.BooleanField(blank=True, help_text='Wanneer u kinderen via een instelling (dus ook school) werft en u de ouders niet laat ondertekenen, maar in plaats daarvan de leiding van die instelling, dan maakt u gebruik van passieve informed consent. U kunt de templates vinden op <a href="https://intranet.uu.nl/documenten-ethische-toetsingscommissie-gw" target="_blank">Deelkracht-website</a>.', null=True, verbose_name='Maakt u gebruik van passieve informed consent?'),
        ),
    ]
