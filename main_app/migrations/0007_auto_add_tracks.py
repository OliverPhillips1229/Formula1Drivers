from django.db import migrations

def add_tracks(apps, schema_editor):
    Track = apps.get_model('main_app', 'Track')
    tracks = [
        {"name": "Albert Park Grand Prix Circuit", "country": "Australia", "length_km": 5.278},
        {"name": "Jeddah Corniche Circuit", "country": "Saudi Arabia", "length_km": 6.174},
        {"name": "Bahrain International Circuit", "country": "Bahrain", "length_km": 5.412},
        {"name": "Shanghai International Circuit", "country": "China", "length_km": 5.451},
        {"name": "Miami International Autodrome", "country": "USA", "length_km": 5.412},
        {"name": "Imola (Autodromo Internazionale Enzo e Dino Ferrari)", "country": "Italy", "length_km": 4.909},
        {"name": "Circuit de Monaco", "country": "Monaco", "length_km": 3.337},
        {"name": "Circuit de Barcelona-Catalunya", "country": "Spain", "length_km": 4.657},
        {"name": "Circuit Gilles Villeneuve", "country": "Canada", "length_km": 4.361},
        {"name": "Red Bull Ring", "country": "Austria", "length_km": 4.318},
        {"name": "Silverstone Circuit", "country": "UK", "length_km": 5.891},
        {"name": "Hungaroring", "country": "Hungary", "length_km": 4.381},
        {"name": "Circuit de Spa-Francorchamps", "country": "Belgium", "length_km": 7.004},
        {"name": "Zandvoort", "country": "Netherlands", "length_km": 4.259},
        {"name": "Monza (Autodromo Nazionale Monza)", "country": "Italy", "length_km": 5.793},
        {"name": "Marina Bay Street Circuit", "country": "Singapore", "length_km": 4.940},
        {"name": "Suzuka International Racing Course", "country": "Japan", "length_km": 5.807},
        {"name": "Circuit of the Americas", "country": "USA", "length_km": 5.513},
        {"name": "Autódromo Hermanos Rodríguez", "country": "Mexico", "length_km": 4.304},
        {"name": "Interlagos (Autódromo José Carlos Pace)", "country": "Brazil", "length_km": 4.309},
        {"name": "Las Vegas Strip Circuit", "country": "USA", "length_km": 6.201},
        {"name": "Lusail International Circuit", "country": "Qatar", "length_km": 5.419},
        {"name": "Yas Marina Circuit", "country": "UAE", "length_km": 5.281},
    ]
    for track in tracks:
        Track.objects.create(**track)

class Migration(migrations.Migration):
    dependencies = [
        ('main_app', '0006_track_result_track'),
    ]
    operations = [
        migrations.RunPython(add_tracks),
    ]
