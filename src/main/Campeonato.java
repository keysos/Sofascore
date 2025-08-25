package main;


import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Campeonato {

    private List<Time> times;
    private List<Jogo> jogos;

    public Campeonato() {
        times = new ArrayList<>();
        jogos = new ArrayList<>();
    }

    void adicionarTime(Time time) throws TimeJaExisteException {
        for (Time t : times) {
            if (t.getNome().equalsIgnoreCase(time.getNome())) {
                throw new TimeJaExisteException("O time " + time.getNome() + " já está no campeonato.");
            }            
        }
        times.add(time);
    }
    
    public List<Jogo> getJogosByRodada(int rodada) {
        return jogos.stream()
                    .filter(j -> j.getRodada() == rodada)
                    .collect(Collectors.toList());
    }

    public void adicionarJogo(Jogo jogo) {
        jogos.add(jogo);
    }

    public List<Time> getTimes() {
        return times;
    }

    public List<Jogo> getJogos() {
        return jogos;
    }
    
}