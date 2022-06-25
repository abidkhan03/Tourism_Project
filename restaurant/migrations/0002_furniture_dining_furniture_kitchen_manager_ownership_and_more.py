# Generated by Django 4.0.5 on 2022-06-04 08:06

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='furniture_dining',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('furniture_type', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='furniture_kitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('furniture_type', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_manager', models.CharField(max_length=20, null=True)),
                ('manager_percent', models.IntegerField(null=True)),
                ('manager_address', models.TextField(max_length=100, null=True)),
                ('manager_telephone', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_owner', models.CharField(max_length=100, null=True)),
                ('owner_percent', models.IntegerField(null=True)),
                ('owner_address', models.TextField(max_length=100, null=True)),
                ('telegraphic_address', models.TextField(max_length=100, null=True)),
                ('owner_telephone', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='restraunt',
            name='annual_rent',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='apprentices',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='area_of_dining',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='area_of_kitchen',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='available_facilities',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('reception', 'RECEPTION'), ('bill counter', 'BILL COUNTER'), ('telephone', 'TELEPHONE'), ('air-condition', 'AIR-CONDITION'), ('heating', 'HEATING'), ('cloak room', 'CLOAK ROOM'), ('toilet', 'TOILET'), ('car park', 'CAR PARK'), ('entertainment', 'ENTERTAINMENT')], max_length=95, null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='cost_of_equipment',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='cost_of_furniture',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='english_knowing',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='name_of_designation',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='nature_of_room',
            field=models.CharField(choices=[('single bed room', 'SINGLE BED ROOM'), ('double bed room', 'DOUBLE BED ROOM'), ('suite room', 'SUITE ROOM')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='not_professionally',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='number_of_floors',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='number_of_room',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='ownership',
            field=models.CharField(choices=[('proprietary', 'Proprietary'), ('partnership', 'Partnership'), ('private company', 'Private Company'), ('limited', 'Limited'), ('unlimited', 'Unlimited')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='professionally_trained',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='rates',
            field=models.CharField(choices=[('immeidiatly', 'IMMEIDIATLY'), ('after dinner', 'AFTER DINNER')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='seating_area',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='total_area',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='total_investment',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='total_number_bearers',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='total_number_billers',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='total_number_cooks',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='total_number_mangers',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='total_number_receptionists',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='type_of_cuisine',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='restraunt',
            name='working_capital',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='restraunt',
            name='province',
            field=models.CharField(choices=[('balochistan', 'BALOCHISTAN'), ('punjab', 'PUNJAB'), ('sindh', 'SINDH'), ('kpk', 'KPK'), ('fata', 'FATA')], default='green', max_length=100),
        ),
    ]