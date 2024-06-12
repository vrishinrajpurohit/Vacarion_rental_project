# Generated by Django 5.0.3 on 2024-06-10 16:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='hostlists',
            name='listing_host',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hostlists',
            name='listing_price',
            field=models.IntegerField(default=0),
        ),
    ]