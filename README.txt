# Campeonato Brasileiro de Futebol ⚽

Este projeto é uma aplicação em Java Swing e Python para gerenciamento e visualização de estatísticas de campeonatos de futebol.  
Ele permite carregar arquivos CSV contendo os resultados das partidas, gerar classificações automaticamente e visualizar gráficos interativos sobre o desempenho dos times.

---

## 📌 Funcionalidades

Em java e python.

- **Carregar Arquivo CSV**  
  - O usuário pode importar um arquivo CSV com os resultados das partidas.  
  - O sistema processa os dados e atualiza a tabela de classificação.

- **Tabela de Classificação estilo Brasileirão**  
  - Mostra posição, pontos, vitórias, empates, derrotas, gols pró, gols contra e saldo de gols.  
  - Ordenação automática conforme regras tradicionais de classificação.

- **Visualizações Gráficas**  
  - **Gráfico de Barras**: mostra gols marcados por cada time.  
  - **Gráfico de Pizza**: vitórias, empates e derrotas de um time selecionado.  
  - **Jogos por Rodada**: exibe os resultados de uma rodada específica.  
  - **Apenas em java: Gráfico de Linha**: evolução de desempenho de um time ao longo do campeonato.

- **Interface Amigável (Java Swing e Tkinter)**  
  - Botões para fácil acesso às funções.  
  - Janelas adicionais para exibição dos gráficos e resultados.

---

## 📂 Estrutura Esperada do CSV

O arquivo CSV deve conter os seguintes campos (com cabeçalho na primeira linha):

Rodada,Data,IdCasa,NomeCasa,GolsCasa,IdFora,NomeFora,GolsFora
1,2024-05-01,1,Time A,2,2,Time B,1
1,2024-05-02,3,Time C,0,4,Time D,0

- **Rodada**: número da rodada (inteiro)  
- **Data**: data do jogo (string)  
- **IdCasa / IdFora**: identificadores dos times  
- **NomeCasa / NomeFora**: nomes dos times  
- **GolsCasa / GolsFora**: placar da partida  

---

## 🚀 Como Executar

Em java:

1. Clone o repositório:

   git clone https://github.com/seu-usuario/Sofascore.git

2. Abra o projeto em uma IDE compatível (NetBeans, IntelliJ ou Eclipse).

3. Compile e execute a classe principal:

- **src/main/CampeonatoUI.java

4. Clique em "Adicionar Arquivo" e selecione o CSV com os resultados.

Em python:

1. Clone o repositório:

   git clone https://github.com/seu-usuario/Sofascore.git

2. Abra o projeto em uma IDE compatível (Vscode ou IntelliJ).

3. Deixar o arquivo do campeonato no mesmo diretório que a classe principal já importa o campeonato automaticamente.

4. Compile e execute a classe principal:

- **Python Project/main.py

5. Caso o arquivo não esteja no mesmo diretório, clice no botão importar e o selecione no gerenciador de arquivos.


