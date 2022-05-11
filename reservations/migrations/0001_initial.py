# Generated by Django 4.0.4 on 2022-05-11 20:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.CharField(editable=False, max_length=255, primary_key=True, serialize=False)),
                ('date_check_in', models.DateField()),
                ('date_check_out', models.DateField()),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='reservations.rental')),
            ],
        ),
    ]
