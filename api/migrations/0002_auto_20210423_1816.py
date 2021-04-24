# Generated by Django 3.2 on 2021-04-23 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publichealthunit',
            old_name='name',
            new_name='display_name',
        ),
        migrations.AddField(
            model_name='publichealthunit',
            name='ontario_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]