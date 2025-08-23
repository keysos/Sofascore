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
# Campeonato
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
# Interface
# ------------------------
class CampeonatoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Campeonato Brasileiro - Análise")
        self.campeonato = CampeonatoBrasileiro()

        # Frames
        frame_botoes = tk.Frame(root)
        frame_botoes.pack(pady=10)

        self.btn_carregar = tk.Button(frame_botoes, text="Carregar CSV", command=self.carregar_csv)
        self.btn_carregar.pack(side=tk.LEFT, padx=5)

        self.btn_classificacao = tk.Button(frame_botoes, text="Mostrar Classificação", command=self.mostrar_classificacao)
        self.btn_classificacao.pack(side=tk.LEFT, padx=5)

        self.btn_grafico_resultados = tk.Button(frame_botoes, text="Gráfico de Resultados", command=self.grafico_resultados)
        self.btn_grafico_resultados.pack(side=tk.LEFT, padx=5)

        # Tabela
        self.tree = ttk.Treeview(
            root,
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

    def grafico_resultados(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um time na tabela")
            return

        item = self.tree.item(selected[0])
        id_time = item['values'][0]
        time = self.campeonato.times[id_time]

        dados = [
            ("Vitórias", time.vitorias, "green"),
            ("Empates", time.empates, "yellow"),
            ("Derrotas", time.derrotas, "red")
        ]

        total = sum(valor for _, valor, _ in dados)
        if total == 0:
            messagebox.showinfo("Info", "Nenhum jogo registrado para este time.")
            return

        janela = tk.Toplevel(self.root)
        janela.title(f"Resultados - {time.nome}")
        canvas = tk.Canvas(janela, width=500, height=500, bg="white")
        canvas.pack()

        # Desenhar pizza
        angulo_inicial = 0
        cx, cy, r = 200, 200, 150
        for nome, valor, cor in dados:
            if valor > 0:
                angulo = (valor / total) * 360
                canvas.create_arc(cx-r, cy-r, cx+r, cy+r,
                                  start=angulo_inicial,
                                  extent=angulo,
                                  fill=cor)
                # Label
                meio_angulo = math.radians(angulo_inicial + angulo/2)
                lx = cx + (r/1.5) * math.cos(meio_angulo)
                ly = cy - (r/1.5) * math.sin(meio_angulo)
                porcentagem = round((valor/total)*100, 1)
                canvas.create_text(lx, ly, text=f"{nome}\n{porcentagem}%", fill="black")
                angulo_inicial += angulo

        # Legenda
        y_legend = 20
        for nome, _, cor in dados:
            canvas.create_rectangle(380, y_legend, 400, y_legend+20, fill=cor)
            canvas.create_text(410, y_legend+10, text=nome, anchor="w")
            y_legend += 30

        # Aproveitamento
        canvas.create_text(250, 430, text=f"Aproveitamento: {time.aproveitamento}%",
                           font=("Arial", 12, "bold"), fill="blue")

# ------------------------
# Programa Principal
# ------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = CampeonatoGUI(root)
    root.mainloop()
