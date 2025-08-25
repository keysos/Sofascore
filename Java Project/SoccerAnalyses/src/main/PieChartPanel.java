package main;

import javax.swing.*;
import java.awt.*;

public class PieChartPanel extends JPanel {
    private int vitorias;
    private int empates;
    private int derrotas;

    public PieChartPanel(int vitorias, int empates, int derrotas) {
        this.vitorias = vitorias;
        this.empates = empates;
        this.derrotas = derrotas;
        setPreferredSize(new Dimension(400, 300));
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        int total = vitorias + empates + derrotas;
        if (total == 0) return;

        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        int diametro = Math.min(getWidth(), getHeight()) - 50;
        int x = (getWidth() - diametro) / 2;
        int y = (getHeight() - diametro) / 2;

        int anguloInicial = 0;

        // Vitórias
        int anguloVitorias = (int) Math.round((double) vitorias / total * 360);
        g2.setColor(Color.GREEN);
        g2.fillArc(x, y, diametro, diametro, anguloInicial, anguloVitorias);
        anguloInicial += anguloVitorias;

        // Empates
        int anguloEmpates = (int) Math.round((double) empates / total * 360);
        g2.setColor(Color.YELLOW);
        g2.fillArc(x, y, diametro, diametro, anguloInicial, anguloEmpates);
        anguloInicial += anguloEmpates;

        // Derrotas
        int anguloDerrotas = 360 - anguloInicial; // restante
        g2.setColor(Color.RED);
        g2.fillArc(x, y, diametro, diametro, anguloInicial, anguloDerrotas);

        // --- Estatísticas ---
        int pontos = vitorias * 3 + empates;
        double aproveitamento = (total > 0) ? (pontos / (total * 3.0)) * 100 : 0.0;

        g2.setColor(Color.BLACK);
        g2.drawString("Vitórias: " + vitorias, 10, 20);
        g2.drawString("Empates: " + empates, 10, 35);
        g2.drawString("Derrotas: " + derrotas, 10, 50);
        g2.drawString("Pontos: " + pontos, 10, 70);
        g2.drawString(String.format("Aproveitamento: %.2f%%", aproveitamento), 10, 85);
    }
}