
import java.util.ArrayList;
import java.util.List;

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