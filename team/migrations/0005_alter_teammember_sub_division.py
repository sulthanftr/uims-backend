# Generated by Django 4.1.4 on 2022-12-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20221220_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='sub_division',
            field=models.CharField(blank=True, choices=[('OTHERS', 'Lainnya (Team Principal, Finance, Advisor, dll.)'), ('GOKART 550', 'Gokart 550'), ('GOKART 551', 'Gokart 551'), ('RESEARCH & DEVELOPMENT', 'Research & Development'), ('E-POWERTRAIN', 'E-Powertrain'), ('VEHICLE', 'Vehicle'), ('AERODYNAMICS', 'Aerodynamics'), ('MEDIA', 'Media'), ('RELATION', 'Relation'), ('SPONSORSHIP', 'Sponsorship')], max_length=200, null=True),
        ),
    ]
