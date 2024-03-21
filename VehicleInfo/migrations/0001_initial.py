# Generated by Django 4.2.7 on 2023-11-06 09:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('make', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.PositiveBigIntegerField()),
                ('battery_capacity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('charging_time', models.PositiveBigIntegerField()),
                ('vehicle_image', models.ImageField(upload_to='vehicles')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]