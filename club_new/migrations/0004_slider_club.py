# Generated by Django 5.1.1 on 2024-11-29 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_new', '0003_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sliders', to='club_new.club'),
        ),
    ]
