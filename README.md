### Genetic Algorithm

The proposed problem is to maximize the function *f(x) = x * x - 3x + 4* using a genetic algorithm. The value of *x* is considered an integer between -10 and 10.

---

#### Implementation and Execution

The code was implemented in Python (version 3.5.2). The binary representation used is that the first bit indicates whether the number is positive or negative (1 if negative, 0 if positive), and the remaining bits represent the number in its normal (positive) form. To run the code, execute the command *python main.py* in the terminal. The parameter values are set in the *main()* function in the *main.py* file.

---

#### Pseudocode:

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

---

#### Results

The results show the initial population and the final population (after running the genetic algorithm). For each, there is a decimal value, the binary representation, and the fitness value (according to the function) of the decimal. The last line shows the best solution found, consisting of the decimal and the binary value of *x*.

Copyright (c) 2019 Lorena Kerollen Botelho Tavares
