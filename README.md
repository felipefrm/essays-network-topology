# Avaliação de redação com base em propriedades topológicas de redes complexas. 

### Resumo: 

Este trabalho teve como objetivo descrever e discutir os resultados de experimentos de análise de redações quando estes são modelados como redes complexas. Os
experimentos não indicaram uma correlação tão expressiva quanto se esperava entre os parâmetros topográficos das redes complexas e as avaliações das redações dadas por especialistas. Contudo, acredita-se um boa calibragem de parâmetros e com métodos de processamento de linguagem natural mais adequados, esta proposta pode ser tornar útil para avaliar a qualidade de redações. A modelagem em redes complexas é independente de língua e simplifica o trabalho de análise automática de textos, mostrando-se uma alternativa promissora aos métodos linguisticamente motivados. 

### Passo-a-passo para executar o código:
```
# execute a extração das propriedades de redes das redações
$ python3 networks.py               

# obtenha as médias das métricas obtidas para cada intervalo de nota de redações
$ python3 means.py

# gere os gráficos baseado nas propriedades extraidas na execução do networks.py e nas médias calculadas em means.py
$ python3 visualization.py          

# rode o algoritmo de regressão linear baseado nas propriedades extraiadas na execução do networks.py
$ python3 linear_regression.py      
```

- OBS1: O arquivo network_data.csv na pasta data é o resultado da execução do primero comando.
- OBS2: O arquivo means.py na pasta data é o resultado da execução do segundo comando.
- OBS3: As imagens na pasta vizualization é o resultado da execução do terceiro comando.
- OBS4: O arquivo prediction.csv na pasta data é o resultado da execução do quarto comando.
