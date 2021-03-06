# Generated by Django 2.2.5 on 2019-10-19 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('time_stamp', models.CharField(max_length=100)),
                ('previous_hash', models.CharField(max_length=100)),
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('hash_num', models.CharField(max_length=500)),
                ('nonce', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Chain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('length', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_sensor', models.CharField(max_length=100)),
                ('humidity_sensor', models.CharField(max_length=100)),
                ('vibration_sensor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_sensor', models.CharField(max_length=100)),
                ('humidity_sensor', models.CharField(max_length=100)),
                ('vibration_sensor', models.CharField(max_length=100)),
                ('time_stamp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='b2t',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Block')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Transactions')),
            ],
        ),
        migrations.CreateModel(
            name='b2c',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Block')),
                ('chain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Chain')),
            ],
        ),
    ]
