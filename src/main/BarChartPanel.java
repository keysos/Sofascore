package main;

import javax.swing.*;
import java.awt.*;
import java.util.Map;

public class BarChartPanel extends JPanel {
    private Map<String, Integer> goalsMap;

    public BarChartPanel(Map<String, Integer> goalsMap) {
        this.goalsMap = goalsMap;
        setPreferredSize(new Dimension(800, 300)); // adjust width/height as needed
    }

    public void setGoalsMap(Map<String, Integer> goalsMap) {
        this.goalsMap = goalsMap;
        repaint(); // redraw chart when map changes
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (goalsMap == null || goalsMap.isEmpty()) return;

        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        int panelWidth = getWidth();
        int panelHeight = getHeight();
        int padding = 50;
        int labelPadding = 25;

        int maxGoals = goalsMap.values().stream().max(Integer::compareTo).orElse(1);

        int numberOfTeams = goalsMap.size();
        int barWidth = (panelWidth - 2 * padding) / numberOfTeams;

        int i = 0;
        for (Map.Entry<String, Integer> entry : goalsMap.entrySet()) {
            int x = padding + i * barWidth;
            int barHeight = (int) ((panelHeight - 2 * padding) * ((double) entry.getValue() / maxGoals));
            int y = panelHeight - padding - barHeight;

            // draw bar
            g2.setColor(Color.BLUE);
            g2.fillRect(x, y, barWidth - 5, barHeight);

            // draw goals on top
            g2.setColor(Color.BLACK);
            String goalStr = String.valueOf(entry.getValue());
            g2.drawString(goalStr, x + (barWidth - 5) / 2 - g2.getFontMetrics().stringWidth(goalStr) / 2, y - 5);

            // draw team name below
            String teamName = entry.getKey();
            int nameWidth = g2.getFontMetrics().stringWidth(teamName);
            g2.drawString(teamName, x + (barWidth - 5) / 2 - nameWidth / 2, panelHeight - padding + labelPadding);

            i++;
        }

        // draw axes
        g2.drawLine(padding, panelHeight - padding, panelWidth - padding, panelHeight - padding); // x-axis
        g2.drawLine(padding, panelHeight - padding, padding, padding); // y-axis
    }
}
