package main;

import javax.swing.*;
import java.awt.*;

/*
 * Painel que desenha um gráfico de linha mostrando a evolução
 * dos pontos de um time ao longo das rodadas.
 */
public class LineChartPanel extends JPanel {

    // Time cujos pontos serão plotados
    private Time time;

    /*
     * Construtor do painels
     */
    public LineChartPanel(Time time) {
        this.time = time;
        setPreferredSize(new Dimension(800, 600)); // tamanho padrão do painel
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (time == null) return; // nada a desenhar se não há time

        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        int padding = 60; // margem do gráfico
        int width = getWidth() - 2 * padding;
        int height = getHeight() - 2 * padding;

        // Pontos acumulados por rodada
        int[] pontosRodada = time.getPontosPorRodada();
        int numRodadas = pontosRodada.length;
        if (numRodadas == 0) return;

        // Valor máximo do eixo Y (arredondado para múltiplo de 10)
        int maxPontos = pontosRodada[numRodadas - 1];
        int maxY = ((maxPontos + 9) / 10) * 10;

        // --- Grade horizontal (valores de pontos) ---
        g2.setColor(new Color(220, 220, 220)); // cor cinza clara
        for (int p = 0; p <= maxY; p += 10) {
            int y = padding + height - (int) ((double) p / maxY * height);
            g2.drawLine(padding, y, padding + width, y);
            g2.setColor(Color.BLACK);
            g2.drawString(String.valueOf(p), padding - 30, y + 5); // valor na lateral
            g2.setColor(new Color(220, 220, 220));
        }

        // --- Grade vertical (rodadas) ---
        for (int r = 0; r < numRodadas; r++) {
            int x = padding + (int) ((double) r / (numRodadas - 1) * width);
            g2.setColor(new Color(220, 220, 220));
            g2.drawLine(x, padding, x, padding + height);
            g2.setColor(Color.BLACK);
            g2.drawString(String.valueOf(r + 1), x - 5, padding + height + 20);
        }

        // --- Eixos X e Y ---
        g2.setColor(Color.BLACK);
        g2.drawLine(padding, padding, padding, padding + height); // eixo Y
        g2.drawLine(padding, padding + height, padding + width, padding + height); // eixo X

        // --- Linha do time ---
        g2.setColor(Color.BLUE);
        int[] xPoints = new int[numRodadas];
        int[] yPoints = new int[numRodadas];
        for (int r = 0; r < numRodadas; r++) {
            xPoints[r] = padding + (int) ((double) r / (numRodadas - 1) * width);
            yPoints[r] = padding + height - (int) ((double) pontosRodada[r] / maxY * height);
        }
        for (int i = 0; i < numRodadas - 1; i++) {
            g2.drawLine(xPoints[i], yPoints[i], xPoints[i + 1], yPoints[i + 1]); // conecta os pontos
        }

        // --- Pontos individuais ---
        g2.setColor(Color.RED);
        for (int i = 0; i < numRodadas; i++) {
            g2.fillOval(xPoints[i] - 3, yPoints[i] - 3, 6, 6); // ponto vermelho
            g2.drawString(String.valueOf(pontosRodada[i]), xPoints[i] - 10, yPoints[i] - 10); // valor acima do ponto
        }

        // --- Título do gráfico ---
        g2.setColor(Color.BLACK);
        g2.drawString("Evolução de Pontos - " + time.getNome(), padding, padding - 20);
    }
}
