# Generated by Django 3.1.7 on 2021-03-06 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20210306_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='game_slug',
            new_name='slug',
        ),
    ]
