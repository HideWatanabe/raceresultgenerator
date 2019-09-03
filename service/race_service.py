from repository import file_repository
from model.models import *
import datetime

def generate_result():
    race_results,pilots, best_lap = parse_file("logs/karts.log")
    final_race = []

    for pilot_code in race_results:
        pilot_race = race_results[pilot_code]
        race = Race(pilots[pilot_code])
        race.extend_lap(pilot_race)
        race.race_time = get_race_time(pilot_race)
        race.best_lap = get_pilot_best_lap(pilot_race)
        final_race.append(race)

    final_race.sort(key=lambda x: x.race_time)
    count = 1
    best_total_time = None
    for race in final_race:
        race.position = count
        # getting time between winner and another pilots
        if count == 1:
            best_total_time = race.race_time
            race.winner_difference = datetime.timedelta(seconds = 0)
        else:
            race.winner_difference = race.race_time - best_total_time
        race.race_speed_average = get_pilot_average_speed(race.laps)
        count += 1
        
    result = RaceResults(final_race, best_lap)

    return result

def get_pilot_best_lap(laps):
    laps.sort(key=lambda x: x.lap_time)
    return laps[0]

def get_winner_difference(winner_time, pilot_time):
    return pilot_time - winner_time

def get_pilot_average_speed(laps):
    sum = 0
    for lap in laps:
        sum += float(lap.speed_average.replace(",","."))
    return sum / len(laps)

def parse_file(file_name):
    race_results = {}
    pilots = {}
    laps = file_repository.read_file(file_name)
    # print(laps)
    first_line = True
    
    best_lap = {}

    for lap in laps:
        if first_line:
            first_line = False
            continue
        pilot_code = lap.pilot.code
        pilot_laps = []
        # putting the lap in a correct key (pilot)
        if len(race_results) == 0 or pilot_code not in race_results:
            pilot_laps = [lap]
            pilots[pilot_code] = lap.pilot
        else:
            pilot_laps = race_results[pilot_code]
            pilot_laps.append(lap)
        race_results[pilot_code] = pilot_laps
        # getting the race best lap
        if len(best_lap) == 0 or best_lap.get('Time') > lap.lap_time:
            best_lap['Pilot'] = lap.pilot
            best_lap['Time'] = lap.lap_time
    return race_results, pilots, best_lap


def get_race_time(laps):
    sum = datetime.timedelta()
    for lap in laps:
        (m,s) = lap.lap_time.split(":")
        (sec, milisec) = s.split(".")
        d = datetime.timedelta(minutes = int(m), seconds = int(sec), milliseconds = int(milisec))
        sum += d
    return sum

def extra_required_data():
    pass