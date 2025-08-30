package main;

import java.util.ArrayList;
import java.util.List;

/**
 * Representa um time de futebol em um campeonato.
 * Armazena estatísticas como vitórias, derrotas, empates, gols
 * e evolução de pontos rodada a rodada.
 */
public class Time {

    // Nome do time
    private final String nome;

    // Estatísticas do time
    private int vitorias;
    private int derrotas;
    private int empates;
    private int golsPro; // gols marcados
    private int golsCon; // gols sofridos

    // Lista com pontos acumulados a cada rodada
    private List<Integer> pontosPorRodada = new ArrayList<>();

    /**
     * Construtor: cria um time com nome e estatísticas zeradas
     * @param nome Nome do time
     */
    public Time(String nome) {
        this.nome = nome;
        this.vitorias = 0;
        this.empates = 0;
        this.derrotas = 0;
        this.golsPro = 0;
        this.golsCon = 0;
    }

    /**
     * Registra o resultado de um jogo e atualiza estatísticas do time.
     * @param golsFeitos Gols marcados pelo time
     * @param golsSofridos Gols sofridos pelo time
     */
    public void registrarJogo(int golsFeitos, int golsSofridos){
        // Atualiza gols pró e contra
        golsPro += golsFeitos;
        golsCon += golsSofridos;

        // Atualiza vitórias, empates e derrotas
        if (golsFeitos > golsSofridos){
            vitorias++;
        } else if (golsFeitos == golsSofridos){
            empates++;
        } else {
            derrotas++;
        }
        
        // Registra os pontos acumulados até esta rodada
        pontosPorRodada.add((vitorias * 3) + empates);
    }
    
    /**
     * Retorna um array com a evolução de pontos por rodada
     * @return array de pontos acumulados
     */
    public int[] getPontosPorRodada() {
        int[] array = new int[pontosPorRodada.size()];
        for (int i = 0; i < pontosPorRodada.size(); i++) {
            array[i] = pontosPorRodada.get(i);
        }
        return array;
    }
    
    /**
     * Retorna os pontos totais do time
     * @return pontos (3 por vitória + 1 por empate)
     */
    public int GetPontos(){
        return (vitorias * 3) + empates;
    }

    /**
     * Calcula o saldo de gols do time
     * @return gols pró - gols contra
     */
    public int GetSaldoGols(){
        return golsPro - golsCon;
    }

    // --------------------- Getters ---------------------

    public String getNome() {
        return nome;
    }
    
    public int getVitorias() {
        return vitorias;
    }

    public int getDerrotas() {
        return derrotas;
    }

    public int getEmpates() {
        return empates;
    }

    public int getGolsPro() {
        return golsPro;
    }

    public int getGolsCon() {
        return golsCon;
    }
}
