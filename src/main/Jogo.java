package main;

public class Jogo {

    private int rodada;
    private String data;
    private String idCasa;
    private String timeCasa;
    private int golsCasa;
    private String idFora;
    private String timeFora;
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

    public int getRodada(){
        return rodada;
    }

    String getNomeFora() {
        return timeFora;
    }

    String getNomeCasa() {
        return timeCasa;
    }



}