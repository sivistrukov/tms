# Generated by Django 4.1.4 on 2022-12-17 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0003_alter_assignment_customers_alter_payload_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payload',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payloads', to='assignments.assignment'),
        ),
    ]
