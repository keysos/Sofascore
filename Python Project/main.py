import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import csv
import math

# ------------------------
# Classe Time
# ------------------------
class Time:
    def __init__(self, id_time, nome):
        self.id_time = id_time
        self.nome = nome
        self.pontos = 0
        self.jogos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_pro = 0
        self.gols_contra = 0

    @property
    def saldo_gols(self):
        return self.gols_pro - self.gols_contra

    @property
    def aproveitamento(self):
        total_pontos = (self.vitorias + self.empates + self.derrotas) * 3
        if total_pontos == 0:
            return 0
        return round(((self.vitorias*3 + self.empates)/total_pontos)*100, 1)

    def registrar_partida(self, gols_marcados, gols_sofridos):
        self.gols_pro += gols_marcados
        self.gols_contra += gols_sofridos
        self.jogos += 1

        if gols_marcados > gols_sofridos:
            self.vitorias += 1
            self.pontos += 3
        elif gols_marcados == gols_sofridos:
            self.empates += 1
            self.pontos += 1
        else:
            self.derrotas += 1

# ------------------------
# Campeonato
# ------------------------
class CampeonatoBrasileiro:
    def __init__(self):
        self.times = {}
        self.rodadas = []
        self.rodada_atual = 0

    def carregar_dados(self, caminho_csv):
        self.times = {}
        self.rodadas = []
        with open(caminho_csv, mode='r', encoding='utf-8-sig', newline='') as csvfile:
            leitor = csv.DictReader(csvfile, delimiter=',')

            rodada = []
            numero_atual = None
            for linha in leitor:
                self.rodada_atual = int(linha["Rodada"])

                if numero_atual is not None and numero_atual != self.rodada_atual:
                    self.rodadas.append(rodada)
                    rodada = []

                rodada.append(linha)

                id_casa = linha["IdCasa"]
                id_fora = linha["IdFora"]
                    
                if id_casa not in self.times:
                    self.times[id_casa] = Time(id_casa, linha["TimeCasa"])
                if id_fora not in self.times:
                    self.times[id_fora] = Time(id_fora, linha["TimeFora"])

                self.times[id_casa].registrar_partida(int(linha["GolsCasa"]), int(linha["GolsFora"]))
                self.times[id_fora].registrar_partida(int(linha["GolsFora"]), int(linha["GolsCasa"]))
                    
                numero_atual = self.rodada_atual                
        

    def classificacao(self):
        return sorted(
                self.times.values(),
                key=lambda t: (t.pontos, t.vitorias, t.saldo_gols, t.gols_pro),
                reverse=True
            )

# ------------------------
# Interface
# ------------------------
import tkinter as tk
from tkinter import filedialog, messagebox
import csv

# ------------------------
# Classe Time
# ------------------------
class Time:
    def __init__(self, id_time, nome):
        self.id_time = id_time
        self.nome = nome
        self.pontos = 0
        self.jogos = 0
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_pro = 0
        self.gols_contra = 0

    @property
    def saldo_gols(self):
        return self.gols_pro - self.gols_contra

    @property
    def aproveitamento(self):
        total_pontos = (self.vitorias + self.empates + self.derrotas) * 3
        if total_pontos == 0:
            return 0
        return round(((self.vitorias*3 + self.empates)/total_pontos)*100, 1)

    def registrar_partida(self, gols_marcados, gols_sofridos):
        self.gols_pro += gols_marcados
        self.gols_contra += gols_sofridos
        self.jogos += 1
        if gols_marcados > gols_sofridos:
            self.vitorias += 1
            self.pontos += 3
        elif gols_marcados == gols_sofridos:
            self.empates += 1
            self.pontos += 1
        else:
            self.derrotas += 1

# ------------------------
# Campeonato
# ------------------------
class CampeonatoBrasileiro:
    def __init__(self):
        self.times = {}
        self.rodadas = []
        self.rodada_atual = 1  

    def carregar_dados(self, caminho_csv):
        self.times = {}
        self.rodadas = []
        with open(caminho_csv, mode='r', encoding='utf-8-sig', newline='') as csvfile:
            leitor = csv.DictReader(csvfile, delimiter=',')
            rodada = []
            numero_atual = None
            for linha in leitor:
                rodada_atual = int(linha["Rodada"])
                if numero_atual is not None and numero_atual != rodada_atual:
                    self.rodadas.append(rodada)
                    rodada = []
                rodada.append(linha)

                id_casa = linha["IdCasa"]
                id_fora = linha["IdFora"]
                if id_casa not in self.times:
                    self.times[id_casa] = Time(id_casa, linha["TimeCasa"])
                if id_fora not in self.times:
                    self.times[id_fora] = Time(id_fora, linha["TimeFora"])

                self.times[id_casa].registrar_partida(int(linha["GolsCasa"]), int(linha["GolsFora"]))
                self.times[id_fora].registrar_partida(int(linha["GolsFora"]), int(linha["GolsCasa"]))

                numero_atual = rodada_atual
            if rodada:
                self.rodadas.append(rodada)

        # Última rodada ao abrir
        if self.rodadas:
            self.rodada_atual = len(self.rodadas)
        else:
            self.rodada_atual = 1

    def classificacao(self):
        return sorted(
            self.times.values(),
            key=lambda t: (t.pontos, t.vitorias, t.saldo_gols, t.gols_pro),
            reverse=True
        )

# ------------------------
# GUI
# ------------------------
class CampeonatoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Campeonato Brasileiro")
        self.root.config(bg="#1E1E1E", cursor="arrow")
        self.root.attributes("-zoomed", True)

        self.campeonato = CampeonatoBrasileiro()

        # Cima: Botões 
        topo_frame = tk.Frame(self.root, bg="#1E1E1E")
        topo_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        self.btn_carregar = tk.Button(topo_frame, text="Carregar CSV", command=self.carregar_csv)
        self.btn_carregar.pack(side=tk.LEFT, padx=5)

        # Baixo: Tabela e Rodadas
       
        central_frame = tk.Frame(self.root, bg="#1E1E1E")
        central_frame.pack(anchor="center")  

        # Esquerda->Baixo

        #Tabela frane
        
        esquerda_frame = tk.Frame(central_frame, bg="#1E1E1E")
        esquerda_frame.pack(side=tk.LEFT, padx=20, pady=10)

        #Titulo Tabela

        esquerda_label = tk.Label(esquerda_frame, text="TABELA", bg="#1E1E1E", fg="white",
                          font=("Arial", 12, "bold"), anchor="w")
        esquerda_label.pack(fill=tk.X, padx=0, pady=(0,5))

        #Canvas da tabela

        self.tabela = tk.Canvas(esquerda_frame, width=680, height=620,
                                bg="white", highlightthickness=0)
        self.tabela.pack()

        # Meio->Baixo - Linha vertical
        linha_sep = tk.Frame(central_frame, width=2, bg="#444444")
        linha_sep.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=10)

        # Direita->Baixo: 
        
        # Frame rodadas 
        
        direita_frame = tk.Frame(central_frame, bg="#1E1E1E")
        direita_frame.pack(side=tk.LEFT, padx=20, pady=0)

        # Titulo

        direita_label = tk.Label(direita_frame, text="JOGOS", bg="#1E1E1E", fg="white",
                                font=("Arial", 12, "bold"), anchor="w")
        direita_label.pack(fill=tk.X, padx=20, pady=(0,5))

        # Frame das setas 

        self.rodada_frame = tk.Frame(direita_frame, bg="#1E1E1E")
        self.rodada_frame.pack(pady=0)

        # Seta esquerda

        self.btn_prev = tk.Button(self.rodada_frame, text="<", width=3, command=self.rodada_anterior,
                                activebackground="#1E1E1E", bg="#1E1E1E", fg="white", highlightthickness=0, bd=0)
        self.btn_prev.pack(side=tk.LEFT, padx=5)

        # Numero da rodada

        self.rodada_label = tk.Label(self.rodada_frame, text="", bg="#1E1E1E", fg="white",
                                    font=("Arial", 12, "bold"))
        self.rodada_label.pack(side=tk.LEFT, padx=5)

        # Seta direita

        self.btn_next = tk.Button(self.rodada_frame, text=">", width=3, command=self.rodada_proxima,
                                activebackground="#1E1E1E", bg="#1E1E1E", fg="white",
                                highlightthickness=0, bd=0)
        self.btn_next.pack(side=tk.LEFT, padx=5)

        # Canvas dos jogos
        self.rodada_canvas = tk.Canvas(direita_frame, bg="#1E1E1E", width=200, height=620,
                                    highlightthickness=0)
        self.rodada_canvas.pack(pady=0)

        # Atualiza centralização ao redimensionar
        self.rodada_canvas.bind("<Configure>", lambda e: self.mostrar_rodada())

        # Carregar arquivo inicial automaticamente sem ter que inserir manualmente, porém essa opção ainda fica disponível nos botões
        try:
            self.campeonato.carregar_dados("campeonato.csv")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o arquivo inicial: {e}")
            self.carregar_csv()

        # Após carregar mostra tabela e ultima rodada em seus respectivos canvas
        self.criar_tabela_canvas(self.tabela, self.campeonato)
        self.mostrar_rodada()


    def carregar_csv(self):
        try:
            caminho = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
            if caminho:
                self.campeonato.carregar_dados(caminho)
                self.criar_tabela_canvas(self.tabela, self.campeonato)
                self.mostrar_rodada()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")

    # Rodadas
    def rodada_anterior(self):
        if self.campeonato.rodada_atual > 1:
            self.campeonato.rodada_atual -= 1
            self.mostrar_rodada()

    def rodada_proxima(self):
        if self.campeonato.rodada_atual < len(self.campeonato.rodadas):
            self.campeonato.rodada_atual += 1
            self.mostrar_rodada()

    def mostrar_rodada(self):
        self.rodada_canvas.delete("all")
        if not self.campeonato.rodadas:
            return

        self.rodada_label.config(
            text=f"{self.campeonato.rodada_atual}ª RODADA",
            font=("Arial", 10, "bold")
        )

        self.rodada_canvas.update_idletasks()
        canvas_largura = self.rodada_canvas.winfo_width()

        y = 15
        altura_texto = 20

        rodada = self.campeonato.rodadas[self.campeonato.rodada_atual - 1]

        for i, jogo in enumerate(rodada):

            #Data a cima
            self.rodada_canvas.create_text(canvas_largura // 2, y, text=jogo['Data'], fill="white", font=("Arial", 10, "bold"), anchor="center")
            y += altura_texto + 2

            #Placar 
            placar_texto = f"{jogo['TimeCasa']} {jogo['GolsCasa']} x {jogo['GolsFora']} {jogo['TimeFora']}"
            self.rodada_canvas.create_text(canvas_largura // 2, y, text=placar_texto, fill="white", font=("Arial", 10), anchor="center")
            y += altura_texto + 5  

            # Linha que divide cada jogo
            linha_largura = canvas_largura 
            x_inicio = (canvas_largura - linha_largura) / 2
            x_fim = x_inicio + linha_largura
            if i < len(rodada) - 1:
                self.rodada_canvas.create_line(
                    x_inicio, y, x_fim, y, fill="#555555", width=1
                )
            y += 15

    def criar_tabela_canvas(self, canvas, campeonato):
        canvas.delete("all")
        largura_colunas = [280, 50, 50, 50, 50, 50, 50, 50, 50]
        colunas = ["Time", "P", "J", "V", "E", "D", "GP", "GC", "SG"]
        altura_linha = 30

        # Cabeçalho
        x = 0
        for i, texto in enumerate(colunas):
            canvas.create_rectangle(x, 0, x + largura_colunas[i], altura_linha, fill="#1E1E1E", outline="")
            if i == 0:
                canvas.create_text(x + 5, altura_linha//2, text=texto, fill="white", font=("Arial", 10, "bold"), anchor="w")
            else:
                canvas.create_text(x + largura_colunas[i]//2, altura_linha//2, text=texto, fill="white", font=("Arial", 10, "bold"))
            x += largura_colunas[i]

        canvas.create_line(0, altura_linha, sum(largura_colunas), altura_linha, fill="#444444", width=2)

        # Linhas da tabela
        lista_times = campeonato.classificacao()
        y = altura_linha
        for i, time in enumerate(lista_times, start=1):
            x = 0
            valores = [
                f"{i} {time.nome}", time.pontos, time.jogos, time.vitorias,
                time.empates, time.derrotas, time.gols_pro, time.gols_contra, time.saldo_gols
            ]
            for j, valor in enumerate(valores):
                canvas.create_rectangle(x, y, x + largura_colunas[j], y + altura_linha, fill="#1E1E1E", outline="")
                if j == 0: 
                    numero_texto = str(i)
                    nome_texto = time.nome
                    if 1 <= i <= 4:
                        cor_numero = "#0070BB"
                    elif 5 <= i <= 6:
                        cor_numero = "#00C8FF"
                    elif 7 <= i <= 12:
                        cor_numero = "#007D0A"
                    elif 17 <= i <= 20:
                        cor_numero = "#FF0000"
                    else:
                        cor_numero = "white"
                    canvas.create_text(x + 5, y + altura_linha//2, text=numero_texto, fill=cor_numero, font=("Arial", 10, "bold"), anchor="w")
                    canvas.create_text(x + 30, y + altura_linha//2, text=nome_texto, fill="white", font=("Arial", 10), anchor="w")
                else:
                    canvas.create_text(x + largura_colunas[j]//2, y + altura_linha//2, text=str(valor), fill="white", font=("Arial", 10))
                x += largura_colunas[j]
            if i < len(lista_times):
                canvas.create_line(0, y + altura_linha, sum(largura_colunas), y + altura_linha, fill="#444444", width=2)
            y += altura_linha
# ------------------------
# Programa Principal
# ------------------------

root = tk.Tk()
app = CampeonatoGUI(root)
root.mainloop()