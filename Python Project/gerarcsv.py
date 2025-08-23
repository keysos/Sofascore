import csv
import random
from datetime import datetime, timedelta
import os

# Lista de times
times = [
    ("FLAM", "Flamengo"),
    ("PALM", "Palmeiras"),
    ("SAO", "São Paulo"),
    ("CORI", "Corinthians"),
    ("GREM", "Grêmio"),
    ("INTE", "Internacional"),
    ("ATL", "Atlético-MG"),
    ("ATHL", "Athletico-PR"),
    ("FLU", "Fluminense"),
    ("VAS", "Vasco"),
    ("BAHI", "Bahia"),
    ("CEAR", "Ceará"),
    ("CHAP", "Chapecoense"),
    ("GOI", "Goiás"),
    ("CRU", "Cruzeiro"),
    ("VIT", "Vitória"),
    ("COR", "Coritiba"),
    ("SPORT", "Sport Recife"),
    ("ATLE", "Atlético-GO"),
    ("JUVE", "Juventude")
]

# Função para gerar partidas de uma rodada
def gerar_partidas_rodada(rodada, data_base):
    partidas = []
    times_disponiveis = times.copy()
    random.shuffle(times_disponiveis)

    while len(times_disponiveis) >= 2:
        casa = times_disponiveis.pop()
        fora = times_disponiveis.pop()
        gols_casa = random.randint(0, 4)
        gols_fora = random.randint(0, 4)
        data = (data_base + timedelta(days=(rodada - 1) * 7)).strftime("%d/%m/%Y")
        partidas.append([
            rodada, data,
            casa[0], casa[1], gols_casa,
            fora[0], fora[1], gols_fora
        ])
    return partidas

# Caminho do CSV na área de trabalho
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
arquivo_csv = os.path.join(desktop, "campeonato_32_rodadas.csv")

# Gerar CSV completo
data_inicio = datetime(2025, 5, 5)

with open(arquivo_csv, "w", newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Rodada","Data","IdCasa","TimeCasa","GolsCasa","IdFora","TimeFora","GolsFora"])
    for rodada in range(1, 33):  # 32 rodadas
        partidas = gerar_partidas_rodada(rodada, data_inicio)
        for partida in partidas:
            writer.writerow(partida)

print(f"Arquivo '{arquivo_csv}' gerado com sucesso em: {os.path.abspath(arquivo_csv)}")