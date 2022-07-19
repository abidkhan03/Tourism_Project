# Generated by Django 4.0.5 on 2022-07-01 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_alter_hotelregistration_owner_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelOwnerCombine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_id', models.ForeignKey(db_column='hotel_id', on_delete=django.db.models.deletion.DO_NOTHING, to='hotel.hotelregistration')),
                ('owner_id', models.ForeignKey(db_column='owner_id', on_delete=django.db.models.deletion.DO_NOTHING, to='hotel.hotelowner')),
            ],
            options={
                'db_table': 'Hotel_owner_combine',
                'unique_together': {('owner_id', 'hotel_id')},
            },
        ),
    ]
