from model.models import Lap

def read_file(file_name):
    logs = get_file(file_name)
    laps = []
    first_line = True
    if logs:
        while True:
            log = logs.readline()
            if not log or len(log) == 0:
                break
            # Ignoring the log header
            if first_line:
                first_line = False
                continue
            lap = Lap(log.split())
            laps.append(lap)
    return laps

def get_file(file_path):
    return open(file_path)