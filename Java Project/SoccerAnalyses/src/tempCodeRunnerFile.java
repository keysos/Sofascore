public class Main {
    public static void main(String[] args) {
        Campeonato br = new Campeonato();

        // Lê o CSV e atualiza jogos e times
        LeitorCSV.carregarJogos("campeonato.csv", br);

        System.out.println("=== Classificação do Campeonato ===");
        for (Time t : br.getTimes()) {
            System.out.println(t.getNome() + " | Pontos: " + t.GetPontos() + " | Saldo: " + t.GetSaldoGols());
        }

     
    }
}
