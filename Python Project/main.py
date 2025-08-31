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
            
    def gols_na_rodada(self, rodada):
        gols_total = 0
        for jogo in rodada:
            gols_total += int(jogo["GolsCasa"]) + int(jogo["GolsFora"])
        return gols_total

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

        self.campeonato = CampeonatoBrasileiro()
        
        # Carregar arquivo inicial automaticamente sem ter que inserir manualmente, porém essa opção ainda fica disponível nos botões
        try:
            self.campeonato.carregar_dados("campeonato.csv")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o arquivo inicial: {e}")
            self.carregar_csv()

        self.mostrando_rodada = self.campeonato.rodada_atual

        # Cima: Botões e titulo
        topo_frame = tk.Frame(self.root, bg="#1E1E1E")
        topo_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        titulo_label = tk.Label(topo_frame, text="Brasileirão Série A", bg="#1E1E1E", fg="white", font=("Arial", 18, "bold"))
        titulo_label.pack(side=tk.LEFT, expand=True, padx=(70,0))

        botoes_frame = tk.Frame(topo_frame, bg="#1E1E1E")
        botoes_frame.pack(side=tk.LEFT, expand=True, padx=(0,60))

        #Botões

        #Visão geral
        geral_canvas = tk.Canvas(botoes_frame, width=120, height=40, bg="#1E1E1E", highlightthickness=0)
        geral_canvas.pack(side=tk.LEFT, padx=15)
        self.criar_botao(geral_canvas, 120, 35, 20, "Visão geral", self.tabela_rodadas, "#343434")

        #Estatisticas
        estatisticas_canvas = tk.Canvas(botoes_frame, width=120, height=40, bg="#1E1E1E", highlightthickness=0)
        estatisticas_canvas.pack(side=tk.LEFT, padx=15)
        self.criar_botao(estatisticas_canvas, 120, 35, 20, "Estatisticas", self.estatisticas, "#343434")

        #Importar arquivo
        csv_canvas = tk.Canvas(botoes_frame, width=120, height=40, bg="#1E1E1E", highlightthickness=0)
        csv_canvas.pack(side=tk.LEFT, padx=15)
        self.criar_botao(csv_canvas, 120, 35, 20, "Importar", self.carregar_csv, "#343434")

        #Linha que separa o cabeçalho do conteúdo

        linha_horizontal = tk.Frame(self.root, bg="#444444")  
        linha_horizontal.pack(side=tk.TOP, fill=tk.X)

        # Baixo: Tabela e Rodadas
       
        self.central_frame = tk.Frame(self.root, bg="#1E1E1E")
        self.central_frame.pack(pady=(15,0))  

        # Esquerda->Baixo - Visão geral

        #Tabela frame
        
        self.esquerda_frame = tk.Frame(self.central_frame, bg="#1E1E1E")
        self.esquerda_frame.pack(side=tk.LEFT,fill=tk.Y)

        #Titulo Tabela

        self.esquerda_label = tk.Label(self.esquerda_frame, text="TABELA", bg="#1E1E1E", fg="white", font=("Arial", 12, "bold"))
        self.esquerda_label.pack(anchor="w")

        #Canvas da tabela

        self.canvas_tabela = tk.Canvas(self.esquerda_frame, bg="#1E1E1E", highlightthickness=0, width=600, height=650)
        self.canvas_tabela.pack(side=tk.LEFT)

        # Meio->Baixo - Linha vertical
        self.linha_vertical = tk.Frame(self.central_frame, width=2, bg="#444444")
        self.linha_vertical.pack(side=tk.LEFT, fill=tk.Y, padx=50)

        # Direita->Baixo: 
        
        # Frame rodadas 
        
        self.direita_frame = tk.Frame(self.central_frame, bg="#1E1E1E")
        self.direita_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Titulo

        self.direita_label = tk.Label(self.direita_frame, text="JOGOS", bg="#1E1E1E", fg="white", font=("Arial", 12, "bold"), anchor="w")
        self.direita_label.pack(anchor="w", padx=(15,0), pady=(0,15))

        # Frame das setas 

        self.setas_frame = tk.Frame(self.direita_frame, bg="#1E1E1E")
        self.setas_frame.pack(pady=8)

        # Seta esquerda

        self.btn_prev = tk.Button(self.setas_frame, text="<", width=3, command=self.rodada_anterior,
                                activebackground="#1E1E1E", bg="#1E1E1E", fg="white", highlightthickness=0, bd=0)
        self.btn_prev.pack(side=tk.LEFT)

        # Numero da rodada

        self.rodada_label = tk.Label(self.setas_frame, text="", bg="#1E1E1E", fg="white",
                                    font=("Arial", 12, "bold"))
        self.rodada_label.pack(side=tk.LEFT, padx=5)

        # Seta direita

        self.btn_next = tk.Button(self.setas_frame, text=">", width=3, command=self.rodada_proxima,
                                activebackground="#1E1E1E", bg="#1E1E1E", fg="white", highlightthickness=0, bd=0)
        self.btn_next.pack(side=tk.LEFT)

        # Canvas dos jogos
        self.rodada_canvas = tk.Canvas(self.direita_frame, bg="#1E1E1E", width=200, height=600, highlightthickness=0)
        self.rodada_canvas.pack(side=tk.LEFT, padx=5)

        # Baixo - Estatisticas

        self.estatisticas_frame = tk.Frame(self.central_frame, bg="#1E1E1E", width=900, height=600)

        self.estatisticas_escolha = tk.Frame(self.estatisticas_frame, bg="#1E1E1E")
        self.estatisticas_escolha.pack(fill=tk.X)

        #Titulo e passar para o proximo
        self.nome_grafico = tk.Label(self.estatisticas_escolha, text="Gols por rodada", bg="#1E1E1E", fg="white", font=("Arial", 14, "bold"), anchor="w")
        self.nome_grafico.pack(side=tk.LEFT, pady=(0,10))

        self.escolha_estatistica = 0
        self.btn_prox = tk.Button(self.estatisticas_escolha, text=">", width=3, command=self.prox_estatistica,
                                activebackground="#1E1E1E", bg="#1E1E1E", fg="white", highlightthickness=0, bd=0)

        self.btn_prox.pack(side=tk.RIGHT)

        #Grafico de barras

        self.grafico_gols = tk.Canvas(self.estatisticas_frame, width=962, height=550, bg="#343434", highlightthickness=0)
        self.grafico_gols.pack(fill=tk.X)

        #Grafico de pizza

        self.pizza_frame = tk.Frame(self.estatisticas_frame, width=900, height=650, bg="#1E1E1E", highlightthickness=0)

        self.times_op = ttk.Combobox(self.pizza_frame, values=list(self.campeonato.times.keys()))
        self.times_op.bind("<<ComboboxSelected>>", self.grafico_pizza)
        self.times_op.pack(side=tk.TOP, anchor="w", padx=5)

        self.canvas_pizza = tk.Canvas(self.pizza_frame, width=615, height=450, bg="#1E1E1E", highlightthickness=0)
        self.canvas_pizza.pack(side=tk.TOP, anchor="center")

        # Pré-carrega tabela, rodadas e grafico de gols
        self.criar_canvas_tabela()
        self.mostrar_rodada()
        self.grafico__gols()

    #Metodos dos botões

    def tabela_rodadas(self):
        self.estatisticas_frame.pack_forget()
        self.esquerda_frame.pack(side=tk.LEFT)
        self.linha_vertical.pack(side=tk.LEFT, fill=tk.Y, padx=50)
        self.direita_frame.pack(side=tk.LEFT)

    def estatisticas(self):
        self.direita_frame.pack_forget()
        self.esquerda_frame.pack_forget()
        self.linha_vertical.pack_forget()
        self.estatisticas_frame.pack(fill=tk.X)
        self.estatisticas_frame.pack_propagate(False)
    
    def prox_estatistica(self):
        self.escolha_estatistica += 1
        if  self.escolha_estatistica == 1:
            self.pizza_frame.pack(fill=tk.X)
            self.grafico_gols.pack_forget()
            self.nome_grafico.config(text="Gráficos de aproveitamento")
        else:
            self.escolha_estatistica = 0
            self.grafico_gols.pack()
            self.pizza_frame.pack_forget()
            self.nome_grafico.config(text="Gols por rodada")


    #Gráficos

    def grafico_pizza(self, event=None):
        if self.times_op.get() == '':
            return
        time = self.campeonato.times[self.times_op.get()]
        self.canvas_pizza.delete("all")  

        largura = 400
        altura = 400
        raio = min(largura, altura) // 2 - 20
        cx, cy = largura // 2, altura // 2  

        # Cálculo dos ângulos
        ang_v = 360 * time.vitorias / time.jogos
        ang_e = 360 * time.empates / time.jogos
        ang_d = 360 * time.derrotas / time.jogos

        ang_inicial = 0

        # Vitória
        self.canvas_pizza.create_arc(cx - raio, cy - raio, cx + raio, cy + raio, start=ang_inicial, extent=ang_v, fill="#6db0ff", outline="", width=2)
        ang_inicial += ang_v

        # Empates
        self.canvas_pizza.create_arc(cx - raio, cy - raio, cx + raio, cy + raio, start=ang_inicial, extent=ang_e, fill="#ffc000", outline="", width=2)
        ang_inicial += ang_e

        # Derrotas
        self.canvas_pizza.create_arc(cx - raio, cy - raio, cx + raio, cy + raio, start=ang_inicial, extent=ang_d,fill="#ff5c5c", outline="", width=2)

        # Legenda
        self.canvas_pizza.create_text(400, 10, text=f"{time.nome} - {time.aproveitamento}%", anchor="nw", fill="white", font=("Arial", 14, "bold"))
        self.canvas_pizza.create_text(400, 40, text=f"Vitórias: {time.vitorias}", anchor="nw", fill="#6db0ff", font=("Arial", 10, "bold"))
        self.canvas_pizza.create_text(400, 60, text=f"Empates: {time.empates}", anchor="nw", fill="#ffc000", font=("Arial", 10, "bold"))
        self.canvas_pizza.create_text(400, 80, text=f"Derrotas: {time.derrotas}", anchor="nw", fill="#ff5c5c", font=("Arial", 10, "bold"))

    def grafico__gols(self):
        self.grafico_gols.delete("all")  
        altura = 520
        largura_barra = 18
        espacamento = 3
        x1 = 35

        # Linhas horizontais 
        for y_val in range(0, altura, 5):
            y = altura - y_val * 7.5
            self.grafico_gols.create_line(30, y, 962, y, fill="#AAAAAA", dash=(2, 2))
            self.grafico_gols.create_text(10, y, text=str(y_val), fill="#b4b4b4", font=("Arial", 8), anchor="w")

        for i, rodada in enumerate(self.campeonato.rodadas):
            x0 = x1 + espacamento
            x1 = x0 + largura_barra
            y0 = altura - self.campeonato.gols_na_rodada(rodada)*7.5  #quantos pixeis um gol representa, nesse caso 7.5
            y1 = altura

            # Desenha barra
            self.grafico_gols.create_rectangle(x0, y0, x1, y1, fill="#6db0ff", outline="")

            # Número da rodada abaixo da barra
            self.grafico_gols.create_text((x0+x1)//2, altura + 15, text=str(i+1), fill="#b4b4b4", font=("Arial", 8))

            x1 += espacamento

    # Rodadas

    def rodada_anterior(self):
        if self.mostrando_rodada > 1:
            self.mostrando_rodada -= 1
            self.mostrar_rodada()
        else:
            self.mostrando_rodada = self.campeonato.rodada_atual
            self.mostrar_rodada()

    def rodada_proxima(self):
        if self.mostrando_rodada < len(self.campeonato.rodadas):
            self.mostrando_rodada += 1
            self.mostrar_rodada()
        else:
            self.mostrando_rodada = 1
            self.mostrar_rodada()

    def mostrar_rodada(self):
        self.rodada_canvas.delete("all")
        self.rodada_label.config(text=f"{self.mostrando_rodada}ª RODADA", font=("Arial", 9, "bold"))
        self.rodada_canvas.update_idletasks()
        largura = self.rodada_canvas.winfo_width()
        y = 10

        rodada = self.campeonato.rodadas[self.mostrando_rodada - 1]

        for i, jogo in enumerate(rodada):
            #Data 
            self.rodada_canvas.create_text(largura // 2, y, text=jogo['Data'], fill="white", font=("Arial", 9, "bold"), anchor="center")
            y += 20
            #Placar 
            self.rodada_canvas.create_text(largura // 2, y, text=f"{jogo['TimeCasa']} {jogo['GolsCasa']} x {jogo['GolsFora']} {jogo['TimeFora']}", fill="white", font=("Arial", 9), anchor="center")
            y += 15
            # Linha
            if i < len(rodada) - 1:
                self.rodada_canvas.create_line(0, y, largura, y, fill="#555555", width=1)
            y += 15

    #Tabela

    def criar_canvas_tabela(self):
        self.canvas_tabela.delete("all")
        self.canvas_tabela.update_idletasks()
        largura = self.canvas_tabela.winfo_width()
        colunas = ["Time", "P", "J", "V", "E", "D", "GP", "GC", "SG"]
        altura = 28

        # Cabeçalho
        x = largura * 0.008
        for texto in colunas:
            if texto == "Time":
                self.canvas_tabela.create_text(x, altura//2, text=texto, fill="white", font=("Arial", 9, "bold"), anchor="w")
                x += largura * 0.4
            else:
                self.canvas_tabela.create_text(x, altura//2, text=texto, fill="white", font=("Arial", 9, "bold"), anchor="center")
                x += largura * 0.08

        self.canvas_tabela.create_line(0, altura, largura, altura, fill="#444444", width=2)

        # Times
        times = self.campeonato.classificacao()
        y = altura
        for i, time in enumerate(times, start=1):
            x = largura * 0.008
            valores = [f"{i} {time.nome}", time.pontos, time.jogos, time.vitorias, time.empates, time.derrotas, time.gols_pro, time.gols_contra, time.saldo_gols]
            for j, valor in enumerate(valores):
                if j == 0: 
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
                    
                    self.canvas_tabela.create_text(x, y + altura//2, text=str(i), fill=cor_numero, font=("Arial", 9, "bold"), anchor="w")
                    x += largura * 0.04
                    self.canvas_tabela.create_text(x, y + altura//2, text=time.nome, fill="white", font=("Arial", 9), anchor="w")
                    x += largura * 0.36
                else:
                    self.canvas_tabela.create_text(x, y + altura//2, text=str(valor), fill="white", font=("Arial", 9), anchor="center")
                    x += largura * 0.08
            if i < len(times): # Não desenhar a ultima linha
                self.canvas_tabela.create_line(0, y + altura, largura, y + altura, fill="#444444", width=2)
            y += altura

    def carregar_csv(self):
        try:
            caminho = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
            if caminho:
                self.campeonato.carregar_dados(caminho)
                self.criar_canvas_tabela()
                self.mostrar_rodada()
                self.grafico__gols()
                self.grafico_pizza()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")
    
    def criar_botao(self, canvas, largura, altura, raio, texto, comando, cor, texto_cor="white"):

        ret = canvas.create_rectangle(raio, 0, largura-raio, altura, fill=cor, outline="")
        arc_esq = canvas.create_arc(0, 0, 2*raio, altura, start=90, extent=180, fill=cor, outline="")
        arc_dir = canvas.create_arc(largura-2*raio, 0, largura, altura, start=270, extent=180, fill=cor, outline="")
        texto_id = canvas.create_text(largura//2, altura//2, text=texto, fill=texto_cor, font=("Arial", 9, "bold"))

        ids = [ret, arc_esq, arc_dir, texto_id]

        def clique(event):
            if comando:
                comando()

        for item in ids:
            canvas.tag_bind(item, "<Button-1>", clique)

# ------------------------
# Programa Principal
# ------------------------

root = tk.Tk()
root.geometry("1300x700")
app = CampeonatoGUI(root)
root.mainloop()