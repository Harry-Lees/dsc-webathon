# Generated by Django 2.2.5 on 2019-09-15 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_auto_20190916_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='teams.Team'),
        ),
    ]
