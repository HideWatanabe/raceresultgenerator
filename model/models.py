class Lap:
    def __init__(self, log):
        self._hour = log[0]
        self._pilot = Pilot(log[1],log[3])
        self._lap_number = log[4]
        self._lap_time = log[5]
        self._speed_average = log[6]
    
    @property
    def pilot(self):
        return self._pilot

    @property
    def speed_average(self):
        return self._speed_average

    @property
    def lap_time(self):
        return self._lap_time

    def __repr__(self):
        return str(self.__dict__)

class Pilot:
    def __init__(self, code, name):
        self._code = code
        self._name = name
    
    @property
    def code(self):
        return self._code
        
    @property
    def name(self):
        return self._name

    def __repr__(self):
        return str(self.__dict__)

class Race:
    def __init__(self, pilot):
        self._pilot = pilot
        self._laps = []

    @property
    def pilot(self):
        return self._pilot

    @property
    def laps(self):
        return self._laps

    @property
    def race_time(self):
        return self._race_time

    @race_time.setter
    def race_time(self, race_time):
        self._race_time = race_time

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def winner_difference(self):
        return self._winner_difference

    @winner_difference.setter
    def winner_difference(self, winner_difference):
        self._winner_difference = winner_difference
    
    @property
    def best_lap(self):
        return self._best_lap

    @best_lap.setter
    def best_lap(self, best_lap):
        self._best_lap = best_lap

    @property
    def race_speed_average(self):
        return self._race_speed_average

    @race_speed_average.setter
    def race_speed_average(self, race_speed_average):
        self._race_speed_average = race_speed_average

    def extend_lap(self, lap):
        self._laps.extend(lap)  
    
    def __repr__(self):
        return str(self.__dict__)

class RaceResults:
    def __init__(self,races,best_lap):
        self._races = races
        self._best_lap = best_lap

    @property
    def races(self):
        return self._races
    
    @property
    def best_lap(self):
        return self._best_lap

