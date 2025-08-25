package main;

import java.util.ArrayList;
import java.util.List;

public class Time {

    private final String nome;
    private int vitorias;
    private int derrotas;
    private int empates;
    private int golsPro;
    private int golsCon;
    
    private List<Integer> pontosPorRodada = new ArrayList<>();

    public Time(String nome) {
        this.nome = nome;
        this.vitorias = 0;
        this.empates = 0;
        this.derrotas = 0;
        this.golsPro = 0;
        this.golsCon = 0;
    }

    public void registrarJogo(int golsFeitos, int golsSofridos){
        golsPro += golsFeitos;
        golsCon += golsSofridos;

        if (golsFeitos > golsSofridos){
            vitorias++;
        }
        else if (golsFeitos == golsSofridos){
            empates++;
        }
        else {
            derrotas++;
        }
        
        pontosPorRodada.add((vitorias * 3) + empates);
    }
    
     public int[] getPontosPorRodada() {
        int[] array = new int[pontosPorRodada.size()];
        for (int i = 0; i < pontosPorRodada.size(); i++) {
            array[i] = pontosPorRodada.get(i);
        }
        return array;
    }
    
    public int GetPontos(){
        return (vitorias * 3) + (empates);
    }

    public int GetSaldoGols(){
        return golsPro - golsCon;
    }

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