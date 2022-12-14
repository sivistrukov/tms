# Generated by Django 4.1.4 on 2022-12-11 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('counterparties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loading_address', models.CharField(max_length=150)),
                ('unloading_address', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('Ожидает оплату', 'Ожидает оплату'), ('Оплачен', 'Оплачен'), ('Отменен', 'Отменен')], max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('representative', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='counterparties.counterparty')),
            ],
        ),
        migrations.CreateModel(
            name='Payload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('count', models.IntegerField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payloads', to='assignments.assignment')),
            ],
        ),
    ]
