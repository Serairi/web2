from django.db import migrations

def create_initial_stations(apps, schema_editor):
    Station = apps.get_model('monitoring', 'Station')
    stations = [
        {
            'name': 'Mounting 1',
            'description': 'Primary mounting station for large components'
        },
        {
            'name': 'Mounting 2',
            'description': 'Secondary mounting station for medium components'
        },
        {
            'name': 'Mounting 3',
            'description': 'Auxiliary mounting station for small components'
        },
        {
            'name': 'Assembly Line A',
            'description': 'Main assembly line for product series A'
        },
        {
            'name': 'Assembly Line B',
            'description': 'Main assembly line for product series B'
        }
    ]
    
    for station_data in stations:
        Station.objects.create(**station_data)

def remove_initial_stations(apps, schema_editor):
    Station = apps.get_model('monitoring', 'Station')
    Station.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_stations, remove_initial_stations),
    ] 