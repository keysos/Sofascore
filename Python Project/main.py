import tkinter as tk
from tkinter import filedialog, messagebox, ttk, simpledialog
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
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0
        self.gols_pro = 0
        self.gols_contra = 0

    @property
    def saldo_gols(self):
        return self.gols_pro - self.gols_contra

    def registrar_partida(self, gols_pro, gols_contra):
        self.gols_pro += gols_pro
        self.gols_contra += gols_contra

        if gols_pro > gols_contra:
            self.vitorias += 1
            self.pontos += 3
        elif gols_pro == gols_contra:
            self.empates += 1
            self.pontos += 1
        else:
            self.derrotas += 1


# ------------------------
# Classe Campeonato
# ------------------------
class CampeonatoBrasileiro:
    def __init__(self):
        self.times = {}

    def carregar_dados(self, caminho_csv):
        try:
            with open(caminho_csv, newline='', encoding='utf-8') as csvfile:
                leitor = csv.DictReader(csvfile)
                for linha in leitor:
                    id_casa = linha['IdCasa']
                    nome_casa = linha['TimeCasa']
                    gols_casa = int(linha['GolsCasa'])

                    id_fora = linha['IdFora']
                    nome_fora = linha['TimeFora']
                    gols_fora = int(linha['GolsFora'])

                    if id_casa not in self.times:
                        self.times[id_casa] = Time(id_casa, nome_casa)
                    if id_fora not in self.times:
                        self.times[id_fora] = Time(id_fora, nome_fora)

                    self.times[id_casa].registrar_partida(gols_casa, gols_fora)
                    self.times[id_fora].registrar_partida(gols_fora, gols_casa)
        except Exception as e:
            messagebox.showerror("Erro", f"Não foi possível carregar o arquivo: {e}")

    def classificacao(self):
        return sorted(
            self.times.values(),
            key=lambda t: (t.pontos, t.saldo_gols, t.gols_pro),
            reverse=True
        )


# ------------------------
# Classe Interface
# ------------------------
class CampeonatoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Campeonato Brasileiro - Análise")
        self.campeonato = CampeonatoBrasileiro()

        self.frame_botoes = tk.Frame(self.root)
        self.frame_botoes.pack(pady=10)

        self.btn_carregar = tk.Button(self.frame_botoes, text="Carregar CSV", command=self.carregar_csv)
        self.btn_carregar.pack(side=tk.LEFT, padx=5)

        self.btn_classificacao = tk.Button(self.frame_botoes, text="Mostrar Classificação", command=self.mostrar_classificacao)
        self.btn_classificacao.pack(side=tk.LEFT, padx=5)

        self.btn_grafico_gols = tk.Button(self.frame_botoes, text="Gráfico de Gols", command=self.grafico_gols)
        self.btn_grafico_gols.pack(side=tk.LEFT, padx=5)

        self.btn_grafico_resultados = tk.Button(self.frame_botoes, text="Gráfico de Resultados", command=self.grafico_resultados)
        self.btn_grafico_resultados.pack(side=tk.LEFT, padx=5)

        self.tree = ttk.Treeview(
            self.root,
            columns=("ID", "Nome", "P", "V", "E", "D", "GP", "GC", "SG"),
            show="headings"
        )

        for col in ("ID", "Nome", "P", "V", "E", "D", "GP", "GC", "SG"):
            self.tree.heading(col, text=col)

        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def carregar_csv(self):
        caminho = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
        if caminho:
            self.campeonato.carregar_dados(caminho)
            messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")

    def mostrar_classificacao(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for time in self.campeonato.classificacao():
            self.tree.insert("", tk.END, values=(
                time.id_time,
                time.nome,
                time.pontos,
                time.vitorias,
                time.empates,
                time.derrotas,
                time.gols_pro,
                time.gols_contra,
                time.saldo_gols
            ))

    def grafico_gols(self):
        if not self.campeonato.times:
            messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
            return

        janela = tk.Toplevel(self.root)
        janela.title("Gráfico de Gols")

        frame_canvas = tk.Frame(janela)
        frame_canvas.pack(fill=tk.BOTH, expand=True)

        h_scroll = tk.Scrollbar(frame_canvas, orient=tk.HORIZONTAL)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        canvas = tk.Canvas(frame_canvas, width=600, height=400, bg="white", xscrollcommand=h_scroll.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        h_scroll.config(command=canvas.xview)

        times = self.campeonato.classificacao()
        max_gols = max(t.gols_pro for t in times) if times else 1

        largura_barra = 30
        espacamento = 10
        largura_total = (largura_barra + espacamento) * len(times) + 50  # margem

        canvas.config(scrollregion=(0, 0, largura_total, 400))

        x = 50
        for time in times:
            altura = (time.gols_pro / max_gols) * 300 if max_gols > 0 else 0
            canvas.create_rectangle(x, 350 - altura, x + largura_barra, 350, fill="blue")
            canvas.create_text(x + largura_barra / 2, 360, text=time.id_time, angle=90)
            x += largura_barra + espacamento

    def grafico_resultados(self):
        if not self.campeonato.times:
            messagebox.showwarning("Aviso", "Carregue os dados primeiro!")
            return

        codigo = simpledialog.askstring("Time", "Digite o código do time (ex: FLA):")
        if codigo is None or codigo.upper() not in self.campeonato.times:
            messagebox.showerror("Erro", "Time não encontrado!")
            return

        time = self.campeonato.times[codigo.upper()]
        total = time.vitorias + time.empates + time.derrotas

        dados = [
            ("Vitórias", time.vitorias, "green"),
            ("Empates", time.empates, "yellow"),
            ("Derrotas", time.derrotas, "red")
        ]

        janela = tk.Toplevel(self.root)
        janela.title(f"Resultados - {time.nome}")
        canvas = tk.Canvas(janela, width=400, height=400, bg="white")
        canvas.pack()

        angulo_inicial = 0
        for nome, valor, cor in dados:
            if valor > 0:
                angulo_fim = angulo_inicial + (valor / total) * 360
                canvas.create_arc(
                    50, 50, 350, 350,
                    start=angulo_inicial,
                    extent=(valor / total) * 360,
                    fill=cor
                )
                angulo_inicial = angulo_fim


# ------------------------
# Programa Principal
# ------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = CampeonatoGUI(root)
    root.mainloop()
