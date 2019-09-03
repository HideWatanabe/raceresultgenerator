# coding=utf-8
from repository import file_repository
from service import race_service
from utils import utils

lap_limit = 4

"""
    Resultado esperado:
    - Montar resultado da corrida com as seguintes informações:
        - Posição Chegada
        - [OK] Código Piloto
        - [OK] Nome Piloto
        - [OK] Qtde. Voltas Completadas
        - [OK] Tempo Total de Prova
"""

def main():
    result = race_service.generate_result()
    generate_race_result(result)

def generate_race_result(result):
    columns = ["POSITION","COD","PILOTO         ","VOLTAS","TEMPO DE PROVA","MELHOR VOLTA","VELOCIDADE MEDIA","DIFERENÇA PARA O GANHADOR"]
    print(" - ".join(columns))
    for race in result.races:
        print("{:<8d} - {} - {:<15s} - {:>6} - {:>14} - {:>12} - {:>16} - {:>25}".format(
                race.position, 
                race.pilot.code, 
                race.pilot.name,
                len(race.laps),
                utils.format_time(race.race_time),
                race.best_lap.lap_time,
                utils.format_decimal(race.race_speed_average),
                utils.format_time(race.winner_difference)
                ))
    print("Melhor volta da corrida: {} - {}: {}".format(result.best_lap.get("Pilot").code,result.best_lap.get("Pilot").name,result.best_lap.get("Time")))

if __name__ == "__main__":
    main()