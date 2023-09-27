# Generated by Django 4.1 on 2023-03-03 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.department'),
            preserve_default=False,
        ),
    ]
