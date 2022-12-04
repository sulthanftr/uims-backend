# Generated by Django 3.2.9 on 2022-11-05 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='division',
            field=models.CharField(blank=True, choices=[('OTHERS', 'Lainnya (Team Principal, Finance, Advisor, dll.)'), ('GOKART', 'Gokart'), ('EV', 'Electric Vehicle'), ('MARKETING', 'Marketing')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='jabatan',
            field=models.CharField(blank=True, choices=[('TEAM_PRINCIPAL', 'Team Principal'), ('FINANCE', 'Finance'), ('ADVISOR', 'Advisor'), ('SECRETARY', 'Secretary'), ('DRIVER', 'Driver'), ('CTO', 'Chief Technical Officer'), ('MANAGER', 'Manager'), ('STAFF', 'Staff'), ('MECHANIC', 'Mechanic')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='sub_division',
            field=models.CharField(blank=True, choices=[('OTHERS', 'Lainnya (Team Principal, Finance, Advisor, dll.)'), ('GOKART_550', 'Gokart 550'), ('GOKART_551', 'Gokart 551'), ('E_POWERTRAIN', 'E-Powertrain'), ('VEHICLE', 'Vehicle'), ('AERODYNAMICS', 'Aerodynamics'), ('MEDIA', 'Media'), ('RELATION', 'Relation'), ('SPONSORSHIP', 'Sponsorship')], max_length=200, null=True),
        ),
    ]