# Campeonato Brasileiro de Futebol ⚽

Integrantes: José Gustavo Abreu Alves e Anderson Soares de Santana Junior

https://github.com/keysos/Sofascore.git

Este projeto é uma aplicação em Java Swing e Python para gerenciamento e visualização de estatísticas de campeonatos de futebol.  
Ele permite carregar arquivos CSV contendo os resultados das partidas, gerar classificações automaticamente e visualizar gráficos interativos sobre o desempenho dos times.

Descrição do Trabalho:

O trabalho consistiu em desenvolver uma aplicação com interface gráfica para gerar diversos gráficos sobre o campeonato de futebol brasileiro, implementada em Java e Python. Em Java, utilizamos Java Swing e recursos nativos para criar a interface e os gráficos; em Python, usamos Tkinter. A aplicação permite visualizar estatísticas de equipes, desempenho de um time e sua evolução no campeonato, oferecendo interação simples e intuitiva para o usuário.

Na versão em Java, foram desenvolvidos:

Tabela de classificação;
Gráfico de pizza mostrando vitórias, derrotas e empates de um time selecionado;
Gráfico de barras com os gols;
Funcionalidade de busca por resultados a partir de rodadas;
Gráfico de linha demonstrando o desempenho de um time ao longo do campeonato.

Na versão em Python, foram desenvolvidos:

Tabela de classificação;
Gráfico de pizza mostrando vitórias, derrotas e empates de um time selecionado;
Gráfico de barras com os gols;
Funcionalidade de navegação por rodadas;

Descrição da implementação POO do projeto na segunda linguagem:

No código, a orientação a objetos foi implementada de forma clara e funcional, usando classes para representar entidades do campeonato.

Classe Time

Representa cada time do campeonato como um objet
Cada instância armazena atributos próprios, como:

nome, id_time, pontos, jogos, vitorias, empates, derrotas, gols_pro, gols_contra.

Métodos associados a cada time:

registrar_partida(): atualiza estatísticas após cada jogo.
Propriedades (saldo_gols e aproveitamento) calculam informações derivadas dinamicamente.

Benefício: cada time mantém seus dados de forma encapsulada, facilitando cálculos e exibições.

Classe CampeonatoBrasileiro

Representa o campeonato como um todo.
Contém todos os times (times) e as rodadas (rodadas).

Métodos importantes:

carregar_dados(): lê os jogos de um CSV e atualiza cada time.
classificacao(): retorna a lista de times ordenada pelos critérios de pontuação.
gols_na_rodada(): calcula gols totais em uma rodada.

Benefício: centraliza o gerenciamento do campeonato, separando lógica de negócio da interface.

Classe CampeonatoGUI

Responsável pela interface gráfica usando Tkinter.
Instancia um objeto CampeonatoBrasileiro e interage com seus métodos para
Mostrar a tabela de classificação.
Mostrar gráficos de pizza e barras.
Navegar entre rodadas.

Cada funcionalidade do GUI está organizada em métodos, mantendo a lógica do GUI separada da lógica do campeonato.

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

## Estrutura Esperada do CSV

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


