package main;

/*
 * Classe principal que inicia a aplicação do Campeonato.
 */
public class Main {

    public static void main(String[] args) {

        CampeonatoUI frame = new CampeonatoUI(); // cria a janela principal
        frame.setTitle("Brasileirão 2025");     // define o título da janela
        frame.setLocationRelativeTo(null);      // centraliza a janela na tela
        frame.setVisible(true);                 // torna a janela visível

    }
}
