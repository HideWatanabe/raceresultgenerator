import datetime

def format_time(time):
    minutes = int(time.seconds/60)
    seconds = time.seconds%60
    miliseconds = int(time.microseconds/1000)
    return "{}:{}.{}".format(minutes,format(seconds,'02'),format(miliseconds,'03'))

def format_decimal(decimal):
    return "%.5g"%decimal