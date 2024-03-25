# Generated by Django 4.2.7 on 2024-03-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServiceCenters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.AddField(
            model_name='servicecenter',
            name='need_delivery_boy',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='servicecenter',
            name='services_offered',
            field=models.ManyToManyField(related_name='service', to='ServiceCenters.service'),
        ),
    ]