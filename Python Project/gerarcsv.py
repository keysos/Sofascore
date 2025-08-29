import csv
import random
from datetime import datetime, timedelta
import os

# Lista de times
times = [
    ("FLA", "Flamengo"),
    ("PAL", "Palmeiras"),
    ("SAO", "São Paulo"),
    ("COR", "Corinthians"),
    ("GRE", "Grêmio"),
    ("INT", "Internacional"),
    ("CAM", "Atlético-MG"),
    ("BGT", "Bragantino"),
    ("FLU", "Fluminense"),
    ("VAS", "Vasco"),
    ("BAH", "Bahia"),
    ("CEA", "Ceará"),
    ("FOR", "Fortaleza"),
    ("MIR", "Mirassol"),
    ("CRU", "Cruzeiro"),
    ("VIT", "Vitória"),
    ("SAN", "Santos"),
    ("SPO", "Sport Recife"),
    ("BOT", "Botafogo"),
    ("JUV", "Juventude")
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

# Caminho onde o código esta sendo executado
diretorio = os.path.dirname(os.path.abspath(__file__))
arquivo_csv = os.path.join(diretorio, "campeonato.csv")

# Gerar CSV completo
data_inicio = datetime(2025, 3, 3)

with open(arquivo_csv, "w", newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Rodada","Data","IdCasa","TimeCasa","GolsCasa","IdFora","TimeFora","GolsFora"])
    for rodada in range(1, 39):
        partidas = gerar_partidas_rodada(rodada, data_inicio)
        for partida in partidas:
            writer.writerow(partida)

print(f"Arquivo gerado com sucesso em: {arquivo_csv}")