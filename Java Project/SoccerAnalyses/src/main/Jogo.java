package main;

/**
 * Representa um jogo de futebol entre dois times em uma rodada específica.
 * Armazena informações como gols, nomes dos times, data e IDs.
 */
public class Jogo {

    // Número da rodada do campeonato
    private int rodada;

    // Data do jogo (como String, ex: "01/08/2025")
    private String data;

    // IDs dos times (podem ser usados para referência ou banco de dados)
    private String idCasa;
    private String idFora;

    // Nomes dos times
    private String timeCasa;
    private String timeFora;

    // Gols marcados por cada time
    private int golsCasa;
    private int golsFora;

    public Jogo(String data, int golsCasa, int golsFora, String idCasa, String idFora, int rodada, String timeCasa, String timeFora) {
        this.data = data;
        this.golsCasa = golsCasa;
        this.golsFora = golsFora;
        this.idCasa = idCasa;
        this.idFora = idFora;
        this.rodada = rodada;
        this.timeCasa = timeCasa;
        this.timeFora = timeFora;
    }
    
    // --------------------- Getters ---------------------


    public String getTimeCasa() {
        return timeCasa;
    }

    public int getGolsCasa() {
        return golsCasa;
    }

    public String getTimeFora() {
        return timeFora;
    }

    public int getGolsFora() {
        return golsFora;
    }

    public int getRodada() {
        return rodada;
    }

    String getNomeFora() {
        return timeFora;
    }

    String getNomeCasa() {
        return timeCasa;
    }
}
