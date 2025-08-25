package main;

import javax.swing.SwingUtilities;

public class Main {
    public static void main(String[] args) {
        // Sempre bom usar SwingUtilities para criar GUI na EDT
        SwingUtilities.invokeLater(() -> {
            CampeonatoUI frame = new CampeonatoUI();
            frame.setTitle("Campeonato");
            frame.setLocationRelativeTo(null); // centraliza
            frame.setVisible(true);
        });
    }
}
