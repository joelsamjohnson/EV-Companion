# Generated by Django 4.2.7 on 2024-03-25 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCenters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.RemoveField(
            model_name='servicecenter',
            name='services_offered',
        ),
        migrations.AddField(
            model_name='service',
            name='service_center',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='ServiceCenters.servicecenter'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicecenter',
            name='need_delivery_boy',
            field=models.BooleanField(default=False),
        ),
    ]
