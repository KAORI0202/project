# Generated by Django 2.2.7 on 2019-12-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(help_text='Latitude of squirrel sighting point')),
                ('longitude', models.FloatField(help_text='Longitude of squirrel sighting point')),
                ('unique_squirrel_ID', models.CharField(help_text='ID for each squirrel sighting', max_length=20)),
                ('shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='Shift of the day', max_length=5)),
                ('date', models.DateField(help_text='Date of sighting')),
                ('age', models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('', '')], default='', help_text='Age of the squirrel', max_length=10)),
                ('primary_fur_color', models.CharField(choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black'), ('', '')], default='', help_text='Primary fur color of the squirrel', max_length=10)),
                ('location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), ('', '')], default='', help_text='Location of the squirrel', max_length=20)),
                ('specific_location', models.CharField(help_text='Specific location of the squirrel', max_length=200)),
                ('running', models.BooleanField(help_text='Whether the squirrel was seen running')),
                ('chasing', models.BooleanField(help_text='Whether the squirrel was seen chasing another squirrel')),
                ('climbing', models.BooleanField(help_text='Whether the squirrel was seen climbing')),
                ('eating', models.BooleanField(help_text='Whether the squirrel was seen eating')),
                ('foraging', models.BooleanField(help_text='Whether the squirrel was seen foraging for food')),
                ('other_activities', models.CharField(help_text='Other activities of the squirrel', max_length=200)),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='other', help_text='Sex of pet', max_length=16)),
            ],
        ),
        migrations.DeleteModel(
            name='Pet',
        ),
    ]
