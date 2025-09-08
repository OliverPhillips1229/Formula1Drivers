from django.shortcuts import render

# Define the home view function
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def driver_index(request):
    # Render the drivers/index.html template with the drivers data
    return render(request, 'drivers/index.html', {'drivers': drivers})


class Driver:
    def __init__(self, name, current_team, description, age, drive_years):
        self.name = name
        self.current_team = current_team
        self.description = description
        self.age = age
        self.drive_years = drive_years


# Create a list of Driver instances
drivers = [
    Driver(
        'Max Verstappen',
        'Red Bull Racing-Honda RBPT',
        'Dutch-Belgian driver; four-time consecutive World Champion (2021 to 2024); holds numerous F1 records and has been dominant across 11 seasons.',
        27,
        '2015 to present → 11 years'
    ),
    Driver(
        'Lewis Hamilton',
        'Ferrari',
        'British driver with seven World Championships; holds records for most wins, poles, and podiums; recently moved from Mercedes to Ferrari for the 2025 season.',
        40,
        '2007 to present → 19 years'
    ),
    Driver(
        'Oscar Piastri',
        'McLaren-Mercedes',
        'Australian standout; won F2, F3, and Formula Renault in successive seasons; F1 debut in 2023 and now contending for the championship in 2025.',
        24,
        '2023 to present → 3 years'
    ),
    Driver(
        'Lando Norris',
        'McLaren-Mercedes',
        'British driver; multiple junior titles; runner-up in 2024 championship; winning driver with several Grand Prix victories.',
        25,
        '2019 to present → 7 years'
    ),
    Driver(
        'Charles Leclerc',
        'Ferrari',
        'Monégasque driver; F2 and GP3 champion; multiple Grand Prix winner; runner-up in F1 standings in 2022.',
        27,
        '2018 to present → 8 years'
    ),
    Driver(
        'George Russell',
        'Mercedes',
        'British driver; GP3 and F2 champion; joined Mercedes in 2022; race winner, continues to rise with seven seasons of wins.',
        27,
        '2019 to present → 7 years'
    )
]