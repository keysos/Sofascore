package main;

public class Time {

    private final String nome;
    private int vitorias;
    private int derrotas;
    private int empates;
    private int golsPro;
    private int golsCon;

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