# Generated by Django 3.2 on 2021-04-25 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210424_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timeseriescasesregional',
            name='new_cases',
        ),
        migrations.RemoveField(
            model_name='timeseriescasesregional',
            name='phu',
        ),
        migrations.RemoveField(
            model_name='timeseriescasesregional',
            name='total_cases',
        ),
    ]
