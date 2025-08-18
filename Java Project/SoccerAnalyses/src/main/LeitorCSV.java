package main;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

public class LeitorCSV {

    public static void carregarJogos(String arquivo, Campeonato campeonato) {
        try (BufferedReader br = new BufferedReader(
                new InputStreamReader(
                LeitorCSV.class.getResourceAsStream("/resources/campeonato.csv"),
                StandardCharsets.UTF_8))) {

            String linha = br.readLine(); // descarta cabeçalho
            Map<String, Time> timesMap = new HashMap<>();

            while ((linha = br.readLine()) != null) {
                String[] dados = linha.split(",");

                int rodada = Integer.parseInt(dados[0]);
                String data = dados[1];
                String idCasa = dados[2];
                String timeCasa = dados[3];
                int golsCasa = Integer.parseInt(dados[4]);
                String idFora = dados[5];
                String timeFora = dados[6];
                int golsFora = Integer.parseInt(dados[7]);

                // Adiciona time da casa se não existir
                if (!timesMap.containsKey(timeCasa)) {
                    Time t = new Time(timeCasa);
                    timesMap.put(timeCasa, t);
                    campeonato.adicionarTime(t);
                }

                // Adiciona time de fora se não existir
                if (!timesMap.containsKey(timeFora)) {
                    Time t = new Time(timeFora);
                    timesMap.put(timeFora, t);
                    campeonato.adicionarTime(t);
                }

                // Atualiza estatísticas
                timesMap.get(timeCasa).registrarJogo(golsCasa, golsFora);
                timesMap.get(timeFora).registrarJogo(golsFora, golsCasa);

                // Registra jogo no campeonato
                campeonato.adicionarJogo(new Jogo(
                        data, golsCasa, golsFora, idCasa, idFora, rodada, timeCasa, timeFora
                ));
            }

        } catch (TimeJaExisteException e) {
            System.out.println("Erro: " + e.getMessage());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
