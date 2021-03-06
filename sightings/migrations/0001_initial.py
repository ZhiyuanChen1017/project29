# Generated by Django 3.0 on 2019-12-06 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='squirrel',
            fields=[
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('unique_squirrel_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('shift', models.CharField(choices=[('AM', 'am'), ('PM', 'pm')], max_length=2)),
                ('date', models.CharField(blank=True, max_length=10)),
                ('age', models.CharField(blank=True, max_length=20, null=True)),
                ('primary_fur_color', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('specific_location', models.CharField(blank=True, max_length=50, null=True)),
                ('running', models.BooleanField(default=False)),
                ('chasing', models.BooleanField(default=False)),
                ('climbing', models.BooleanField(default=False)),
                ('eating', models.BooleanField(default=False)),
                ('foraging', models.BooleanField(default=False)),
                ('other_activities', models.CharField(blank=True, max_length=100, null=True)),
                ('kuks', models.BooleanField(default=False)),
                ('quaas', models.BooleanField(default=False)),
                ('moans', models.BooleanField(default=False)),
                ('tail_flags', models.BooleanField(default=False)),
                ('tail_twitches', models.BooleanField(default=False)),
                ('approaches', models.BooleanField(default=False)),
                ('indifferent', models.BooleanField(default=False)),
                ('runs_from', models.BooleanField(default=False)),
            ],
        ),
    ]
