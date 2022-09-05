# Generated by Django 4.0.6 on 2022-07-26 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_teamrole_teammember'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamrole',
            old_name='divisionName',
            new_name='division_name',
        ),
        migrations.AddField(
            model_name='teamrole',
            name='division_type',
            field=models.IntegerField(blank=True, choices=[(0, 'Director'), (1, 'Technical Division'), (2, 'Non-Technical Division')], null=True),
        ),
    ]