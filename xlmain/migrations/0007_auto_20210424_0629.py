# Generated by Django 3.0.5 on 2021-04-24 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xlmain', '0006_auto_20210424_0617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mme',
            old_name='Engineering_Chemistry_Laboratory',
            new_name='Engineering_Chemistry_Lab',
        ),
        migrations.RenameField(
            model_name='mme',
            old_name='Metallography_Laboratory',
            new_name='Metallography_Lab',
        ),
    ]
