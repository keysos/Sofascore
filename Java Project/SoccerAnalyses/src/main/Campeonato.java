package main;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/*
 * Representa um campeonato de futebol, contendo os times e os jogos disputados.
 */
public class Campeonato {

    // Lista de times que participam do campeonato
    private List<Time> times;

    // Lista de jogos já realizados ou cadastrados
    private List<Jogo> jogos;

    // Construtor: inicializa as listas
    public Campeonato() {
        times = new ArrayList<>();
        jogos = new ArrayList<>();
    }

    /*
     * Adiciona um time ao campeonato.
    */
    void adicionarTime(Time time) throws TimeJaExisteException {
        for (Time t : times) {
            if (t.getNome().equalsIgnoreCase(time.getNome())) {
                throw new TimeJaExisteException("O time " + time.getNome() + " já está no campeonato.");
            }            
        }
        times.add(time);
    }
    
    /*
     * Retorna a lista de jogos de uma determinada rodada.
     */
    public List<Jogo> getJogosByRodada(int rodada) {
        return jogos.stream()
                    .filter(j -> j.getRodada() == rodada)
                    .collect(Collectors.toList());
    }

    /*
     * Adiciona um jogo à lista de jogos do campeonato
     * @param jogo Jogo a ser adicionado
     */
    public void adicionarJogo(Jogo jogo) {
        jogos.add(jogo);
    }

    // Getters
    public List<Time> getTimes() {
        return times;
    }

    public List<Jogo> getJogos() {
        return jogos;
    }
}
