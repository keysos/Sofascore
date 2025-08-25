package main;

import javax.swing.*;
import java.awt.*;
import java.util.List;
import java.util.Map;
import java.util.ArrayList;

public class BarChartPanel extends JPanel {
    private Map<String, Integer> goalsMap;
    private final Color[] colors = {
        new Color(66, 135, 245),
        new Color(245, 66, 93),
        new Color(66, 245, 161),
        new Color(245, 209, 66),
        new Color(179, 66, 245),
        new Color(255, 140, 0)
    };

    public BarChartPanel(Map<String, Integer> goalsMap) {
        this.goalsMap = goalsMap;
        setPreferredSize(new Dimension(800, 400)); 
        setBackground(Color.WHITE);
    }

    public void setGoalsMap(Map<String, Integer> goalsMap) {
        this.goalsMap = goalsMap;
        repaint(); 
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (goalsMap == null || goalsMap.isEmpty()) return;

        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        int panelWidth = getWidth();
        int panelHeight = getHeight();
        int padding = 60;
        int labelPadding = 40;

        int maxGoals = goalsMap.values().stream().max(Integer::compareTo).orElse(1);

        int numberOfTeams = goalsMap.size();
        int barWidth = (panelWidth - 2 * padding) / numberOfTeams;

        // ---- Desenhar linhas de grade e labels do eixo Y ----
        int numYDivisions = 10;
        for (int i = 0; i <= numYDivisions; i++) {
            int y = panelHeight - padding - (i * (panelHeight - padding * 2) / numYDivisions);
            g2.setColor(new Color(220, 220, 220));
            g2.drawLine(padding, y, panelWidth - padding, y);
            g2.setColor(Color.BLACK);
            String yLabel = String.valueOf((int) ((maxGoals * i) / numYDivisions));
            int labelWidth = g2.getFontMetrics().stringWidth(yLabel);
            g2.drawString(yLabel, padding - labelWidth - 5, y + (g2.getFontMetrics().getHeight() / 2) - 3);
        }

        // ---- Desenhar barras ----
        List<Map.Entry<String, Integer>> entries = new ArrayList<>(goalsMap.entrySet());
        for (int i = 0; i < entries.size(); i++) {
            Map.Entry<String, Integer> entry = entries.get(i);

            int x = padding + i * barWidth + 5; 
            int barHeight = (int) ((panelHeight - 2 * padding) * ((double) entry.getValue() / maxGoals));
            int y = panelHeight - padding - barHeight;

            // cor alternada
            g2.setColor(colors[i % colors.length]);
            g2.fillRoundRect(x, y, barWidth - 10, barHeight, 10, 10);

            // contorno
            g2.setColor(Color.DARK_GRAY);
            g2.drawRoundRect(x, y, barWidth - 10, barHeight, 10, 10);

            // valor acima da barra
            g2.setColor(Color.BLACK);
            String goalStr = String.valueOf(entry.getValue());
            g2.drawString(goalStr, x + (barWidth - 10) / 2 - g2.getFontMetrics().stringWidth(goalStr) / 2, y - 5);

            // nome do time
            String teamName = entry.getKey();
            int nameWidth = g2.getFontMetrics().stringWidth(teamName);
            g2.drawString(teamName, x + (barWidth - 10) / 2 - nameWidth / 2, panelHeight - padding + labelPadding - 10);
        }

        // ---- Eixos ----
        g2.setColor(Color.BLACK);
        g2.drawLine(padding, panelHeight - padding, panelWidth - padding, panelHeight - padding); // eixo X
        g2.drawLine(padding, panelHeight - padding, padding, padding); // eixo Y

        // ---- Título ----
        g2.setFont(g2.getFont().deriveFont(Font.BOLD, 16f));
        String title = "Gols por Time";
        int titleWidth = g2.getFontMetrics().stringWidth(title);
        g2.drawString(title, (panelWidth - titleWidth) / 2, padding - 20);
    }
}
