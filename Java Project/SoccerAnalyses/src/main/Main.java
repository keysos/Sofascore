package main;

import javax.swing.SwingUtilities;

public class Main {
    public static void main(String[] args) {
        // Sempre bom usar SwingUtilities para criar GUI na EDT
        SwingUtilities.invokeLater(() -> {
            CampeonatoUI frame = new CampeonatoUI();
            frame.setTitle("Brasileirão 2025");
            frame.setLocationRelativeTo(null); // centraliza
            frame.setVisible(true);
        });
    }
}
