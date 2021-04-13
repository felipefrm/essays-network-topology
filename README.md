### Passo-a-passo:
```
# execute a extração das propriedades de redes das redações
$ python3 networks.py               

# gere os gráficos baseado nas propriedades extraidas na execução do networks.py
$ python3 visualization.py          

# rode o algoritmo de regressão linear para tentar predizer a nota baseado nas propriedades extraiadas na execução do networks.py
$ python3 linear_regression.py      
```

OBS1: O arquivo network_data.csv na pasta data é o resultado da execução do primero comando.
OBS2: As imagens na pasta vizualization é o resultado dae xecução do segundo comando.
OBS3: O arquivo prediction.csv na pasta data é o resultado da execução do segundo comando.