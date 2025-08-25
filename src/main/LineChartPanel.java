package main;

import javax.swing.*;
import java.awt.*;

public class LineChartPanel extends JPanel {
    private Time time;

    public LineChartPanel(Time time) {
        this.time = time;
        setPreferredSize(new Dimension(800, 600));
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (time == null) return;

        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        int padding = 50;
        int width = getWidth() - 2 * padding;
        int height = getHeight() - 2 * padding;

        // Obtém os pontos acumulados por rodada
        int[] pontosRodada = time.getPontosPorRodada();
        int numRodadas = pontosRodada.length;
        if (numRodadas == 0) return;

        // Descobre o valor máximo de pontos para escalar o eixo Y
        int maxPontos = pontosRodada[numRodadas - 1];

        // Desenha eixos
        g2.setColor(Color.BLACK);
        g2.drawLine(padding, padding, padding, padding + height); // eixo Y
        g2.drawLine(padding, padding + height, padding + width, padding + height); // eixo X

        // Desenha a linha do time
        g2.setColor(Color.BLUE);
        int[] xPoints = new int[numRodadas];
        int[] yPoints = new int[numRodadas];

        for (int r = 0; r < numRodadas; r++) {
            xPoints[r] = padding + (int) ((double) r / (numRodadas - 1) * width);
            yPoints[r] = padding + height - (int) ((double) pontosRodada[r] / maxPontos * height);
        }

        for (int i = 0; i < numRodadas - 1; i++) {
            g2.drawLine(xPoints[i], yPoints[i], xPoints[i + 1], yPoints[i + 1]);
        }

        // Opcional: desenhar pontos e valores
        g2.setColor(Color.RED);
        for (int i = 0; i < numRodadas; i++) {
            g2.fillOval(xPoints[i] - 3, yPoints[i] - 3, 6, 6);
            g2.drawString(String.valueOf(pontosRodada[i]), xPoints[i] - 10, yPoints[i] - 10);
        }

        // Título do time
        g2.setColor(Color.BLACK);
        g2.drawString("Evolução de Pontos - " + time.getNome(), padding, padding - 10);
    }
}
