### Algoritmo Genético

O problema proposto é maximizar a função *f(x) = x * x - 3x + 4* utilizando algoritmo genético. O valor de *x* é considerado número inteiro entre -10 e 10.


#### Implementação e Execução

O código foi implementado em python (versão 3.5.2). A represetanço binária utilizada é do primeiro bit indicar se o número é positivo ou negativo (1 se negativo, 0 se positivo), os bits da sequência são a representação do número em sua forma normal (positiva). Para rodar o código, basta dar o comando *python main.py* no terminal. Os valores considerados para parâmetro estão na função *main()* no arquivo *main.py*.

#### Pseudo código:

```
GA()
    initialize population
    find fitness of population
   
    while (termination criteria is reached) do
        parent selection
        crossover with probability pc
        mutation with probability pm
        decode and fitness calculation
        survivor selection
        find best
    return best
```

#### Resultados

Nos resultados, tem-se a população inicial e a população final (após a execução do algoritmo genético), em cada uma dessas, há um decimal, o binário e o valor fitness (de acordo com a função) do decimal. A última linha apresenta a melhor solução encontrada, composta pelo decimal e o valor de *x* em binário.

Copyright (c) 2019 Lorena Kerollen Botelho Tavares
