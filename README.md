# Mini – Project on Evolutionary Algorithm

## Temperature Prediction

Submitted by:

Yuval Beker 209026384
 Gil Shmaya 209327303
 Eden Grisaro 316440767

Course lecturer:

Prof. Moshe Sipper

December 2022

## Table of Contents
- [Introduction](#introduction)
- [Problem Description](#problem-description)
- [Genetic Programming](#genetic-programming)
  - [Individual](#individual)
  - [Function set](#function-set)
  - [Terminal set](#terminal-set)
  - [Initialize population](#initialize-population)
  - [Creating individuals](#creating-individuals)
  - [The evolution](#the-evolution)
    - [Fitness](#fitness)
    - [Selection](#selection)
    - [Breeding process](#breeding-process)
- [Experiments & Findings](#experiments-&-findings)
  -[Choosing the fitness](#choosing-the-fitness)
  - [Choosing the initial depth](#choosing-the-initial-depth)
- [Conclusions](#conclusions)

## Introduction
Our project focuses on predicting the weather using an evaluation algorithm.

 Whether we have a school trip, go on a vacation or even plan a picnic outside, the weather has a big influence on how things will go. It meets us in many situations and the power of predicting it can have a huge influence in our daily day time.

Weather is the state of the atmosphere, describing the degree to which it is hot or cold, wet or dry, calm or stormy, clear or cloudy. The weather is measured by temperature, wind, humidity, and atmospheric pressure. There are also properties that affect it, such as altitude.Higher altitudes are cooler than lower altitudes, as most atmospheric heating is due to contact with the Earth's surface while radiative losses to space are mostly constant. The differences in the weather occur due to the sun angle as well. For example, In June the Northern Hemisphere is tilted towards the sun. This is what causes seasons. Also there is evidence that human activities such as industry have modified weather patterns.

Weather forecasting is the application of science and technology to predict the state of the atmosphere for a future time and a given location. Weather forecasts are made by collecting quantitative data about the current state of the atmosphere and using scientific understanding of atmospheric processes to project how the atmosphere will evolve.There are a variety of end users to weather forecasts. Weather warnings are important forecasts because they are used to protect life and property. Forecasts based on temperature and precipitation are important to agriculture, and therefore to commodity traders within stock markets. Temperature forecasts are used by utility companies to estimate demand over coming days.

In some areas, people use weather forecasts to determine what to wear on a given day. Since outdoor activities are severely curtailed by heavy rain, snow and the wind chill, forecasts can be used to plan activities around these events and to plan ahead to survive through them.

In this project we will explore the weather in X and try to forecast the upcoming weather.

## Problem Description

**The Problem:** Development of a function that predicts the weather of a given date.

**Our search space:** We took data from \_\_\_\_ of the weather of \_\_\_.

**Weather characteristics:** In general there are six main components, or parts, of weather:
 1. temperature - refers to how hot or cold the atmosphere is.The coldest weather usually happens near the poles, while the warmest weather usually happens near the Equator.

2. atmospheric pressure -the weight of the atmosphere overhead. Changes in atmospheric pressure signal shifts in the weather. A high-pressure system usually brings cool temperatures and clear skies. A low-pressure system can bring warmer weather, storms, and rain. Atmospheric pressure changes with altitude. The atmospheric pressure is much lower at high altitudes.

3. wind - the movement of air. Wind forms because of differences in temperature and atmospheric pressure between nearby regions. Winds tend to blow from areas of high pressure, where it's colder, to areas of low pressure, where it's warmer.

4. humidity -Humidity refers to the amount of water vapor in the air. Water vapor is a gas in the atmosphere that helps make clouds, rain, or snow. Humidity is usually expressed as relative humidity, or the percentage of the maximum amount of water air can hold at a given temperature. Cool air holds less water than warm air.

5. cloudiness -Clouds come in a variety of forms. Some signal mild weather, and others can bring rain or snow. Clouds can affect the amount of sunlight reaching the Earth's surface. Cloudy days are cooler than clear ones because clouds prevent more of the sun's radiation from reaching the Earth's surface.

 We decided to use temperature as our measurement of the weather.

**Our goal:** We would like to predict the weather of the same place using the function that was created.

**Our problems:**

- weather is unpredictable
- there are many characteristics that also affect the weather except temperature
- human involvement can also affect the weather
- global warming has a large impact on the weather

**assumptions:**

- Weather is a cyclical process - one of the reasons is that major changes are initiated by changes in the earth's orbit around the sun. The orbital changes occur slowly over time influencing where solar radiation is received on earth's surface during different seasons. By themselves, these changes in the distribution of solar radiation are not strong enough to cause large temperature changes.
- We decided to predict the weather using the temperature because this is one of the main factors we usually look at when deciding how the weather will be

## Genetic Programming

### Individual:

In the evolutionary algorithm, an individual is a single potential solution to a given problem. In our case, the problem 
is by a given date to predicate the temperature on this date. We want to solve this problem by generating a mathematical 
function approximating the weather. So our single solution is a mathematical function.
<br />We represent the mathematical function as a "Function Tree" GP. In the "Function Tree" the inner nodes will be from 
the "function set" and the leaves from the "terminal set".

### Function set:

In the context of genetic programming, a "function set" is a set of functions that can be used to build the solution to 
a given problem. The "function set" is used to build the initial population of solutions, which evolved over time.
<br />In our system, the "function set" is pre-defined and fixed and consists of a set of basic mathematical functions 
that can be combined to build more complex solutions.
<br />Our "function set" includes the following basic arithmetic functions:

- addition - "f\_add"
- subtraction - "f\_sub"
- multiplication- "f\_mul"
- division - "f\_div"
- log - "f\_log"
- root - "f\_sqrt"
- absolute value - "f\_abs"
- inverseinverse - "f\_inv"
- negative - "f\_neg"
- maximum - "f\_max"
- minimum - "f\_min"
- sin - "f\_sin"
- cos - "f\_cos"
- tan - "f\_tan"
- modulo - "f\_mod"

The "function set" is the set of all possible internal nodes of the tree.

Besides the arithmetic functions that we have in EC-Kity, we add the "f_mod" function. Since we wanted to add cyclic elements 
in our individuals since we know the weather has cyclic elements.

```python
def f_mod(x, y):
    """x%y"""
    """protected modulo: if abs(y) > 0.001 return x%y else return 0"""
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(np.abs(y) > 0.001, np.mod(x, y), 0.)
```

### Terminal set:

A "terminal set" is a set of values that do not change and are pre-oriented. The "terminal set" can be used as inputs to 
the functions in the "function set", and they are used to build the initial population of solutions, which developed.
<br /> In our case, the "terminal set" includes constants numbers [0, 1, -1, 5, 10] and the variables[..........todo complete………………………].

```python
terminal_set = ['month', 'day', 'year', 0, 1, -1, 5, 10]
```

At the beginning of the implementation, we considered only the [0, 1,-1] constants, but we didn't get good results. The 
cause was it was hard to generate common temperatures such as 35 celsius since it requiere a high tree, and we got limitations 
on the tree's height (7). After we added to [10, 5] constants, our results improved.

The "terminal set" is the leaves in the tree.

![](./photos/Function_Tree.png)
<br /> *This diagram represents an example of an individual when the blue squares are nodes from the function set, and 
the orange circles are leaves from the terminal set.*

### Initialize population:

A population is a group of individuals that are being evolved through the use of genetic algorithms. The population as a 
whole represents a variety of possible solutions to this problem. 
<br />Our subpopulation is a collection of "Function Tree" GPs.

#### Creating individuals:
In creating the individuals, we have created ramped half and half trees with an init depth of 2 to 7. We added bloat 
values to slow down the tree's growth, and we chose our population to contain 300 individuals.

**Initialization method:** Ramped half and half trees are used to generate the initial population of individuals (GA) for 
generating a function that will predict temperature. We chose this function because it is a good initialization method for 
symbolic regression problems that we can transform into our problem.
The Ramped half and half method start by creating a set of "half and half" trees, where each tree has a random number of 
nodes, with the restriction that the number of terminal nodes must be less than or equal to the number of non-terminal nodes. 
This is done to ensure that the initial population is diverse and has a balance of simple and complex individuals. The 
method then "ramps" the size of the trees by gradually increasing the maximum depth of the trees until the desired size 
is reached. This gradually increases complexity in the initial population, allowing the GA to explore a wide range of 
solutions and avoid getting stuck in local optima.
 
**Tree depth:** During the implementation, we see that the height of an individual's Function Tree significantly impacts 
its performance. When the tree was too deep, it prone to overfitting, while when it was too shallow, it did not have enough 
complexity to solve the problem effectively. Ultimately, we choose the initial depth of 2 to 7 after a few different runnings.

```python
        Subpopulation(creators=RampedHalfAndHalfCreator(init_depth=get_init_depth(useDefaultData),
                                                        terminal_set=terminal_set,
                                                        function_set=function_set,
                                                        bloat_weight=get_bloat_weight(useDefaultData)),
                      population_size=get_population_size(useDefaultData),
```
### The evolution:

#### Fitness:
The fitness function uses us to measure the quality or effectiveness of a particular solution or individual in a population. 
The fitness function returns a value representing how well an individual's genetically suited to solving a given problem 
or achieving a specific goal.
<br />In our case, the fitness function is used to evaluate the fitness of each individual in the population. It is typically 
designed to be specific to solve the problem of predicting the temperature when given a date. Our fitness function is Mean 
Absolute Error (MAE). MAE is calculated as the average absolute difference between predicted and actual temperature values 
(predicted - self.df[target], actual - individual.execute(x=x, y=y, z=z)). The absolute 
difference between the predicted and real value is taken to handle the negative values of difference.

![](photos/mean-absolute-error.png)

Since, in our case, the fitness function acts like a loss function, we want to minimize our fitness function. 
```python
higher_is_better=False
```

We implement the _evaluate_individual method, which evaluates a **fitness** score for an individual:
```python
    def _evaluate_individual(self, individual):
        month, day, year = self.df['month'], self.df['day'], self.df['year']
        return np.mean(np.abs(individual.execute(month=month, day=day, year=year) - self.df['target']))
```

#### Selection:

Selection refers to the process of choosing which individuals from a population will be selected to participate in the 
process to generate the next generation. The individuals that are selected in our project have better fitness values 
(in our case, lower fitness values), meaning they are better suited to solving the problem at hand.

We chose that our selection implemented by using tournament selection. We decided to use tournament selection since it 
allows the algorithm to keep a diverse population while allowing the best individuals to reproduce.
<br />Tournament selection involves selecting a small number of individuals from the population at random and then comparing 
their fitness values. The individual with the better fitness value is then selected as the "winner" and is given the 
opportunity to reproduce and pass on their genetic information to the next generation.

The number of individuals selected for the tournament is called the "tournament size". We chose a tournament size of 4 
since we found that the size 4 is a good balance between exploration and exploitation. The size of 4 provided us a stronger 
selection pressure, which helped to converge on an optimal solution more quickly.

We configured the Tournament Selection with a probability of 1.
```python
selection_methods=[
    # (selection method, selection probability) tuple
    (TournamentSelection(tournament_size=4, higher_is_better=False), 1)
]
```
The selection process is a crucial step in the genetic algorithm as it determines which individuals will pass on their 
genetic information to the next generation.

#### Breeding process:

We set the hyperparameters for the breeding process:

- We chose an elitism rate that determines that 5% of the population's top individuals will be copied as-is to the next 
generation in each generation.

We defined genetic operators to be applied in each generation:
- Subtree Crossover with a probability of 90%
- Subtree Mutation with a probability of 20%
- ERC Mutation with a probability of 5%

(The total of probabilities does not complete to 100% because the operators are applied one after the other, in a linear sequence).

```python
elitism_rate=0.05,
# genetic operators sequence to be applied in each generation
operators_sequence=[
    SubtreeCrossover(probability=0.9, arity=2),
    SubtreeMutation(probability=0.2, arity=1),
    ERCMutation(probability=0.05, arity=1)
],
```

## Experiments & Findings

### Choosing the fitness

In evolutionary algorithms, the fitness value measures how well a particular solution performs in relation to a particular problem. When selecting a fitness value for an evolutionary algorithm, it is important to consider how well the value reflects the desired characteristics of the solution. For example, in our case, the goal is to find a solution, the weather measures for a requested month, that are as close as possible to a particular target value, the average monthly weather graph in the last years.

In the process of choosing the suitable fitness, we examined two different options. The two options are MAE fitness that are differ in there calculation. MAE stands for Mean Absolute Error. In the context of fitness, it may refer to the error or difference between the predicted value of a fitness function and the true value.
 1. Using an **average** operation in the fitness calculation - we want to minimize the average of the differences between the temperature predicted by the algorithm and the real temperature. In other words, higher fitness means high differences, so in that case we set the parameter higher_is_better to be false.

2. Using an **maximum** operation in the fitness calculation - we want to minimize the maximum difference between the temperature predicted by the algorithm and the real temperature. In that case case we set the parameter higher_is_better to be false as well.

For answering that question, we ran experiment with 500 generations for each fitness methos. We examined the results of each fitness by comparing them to the real temperature occured in Paris on every month in 2013. As you can notice from the below table, the average fitness was chosen as the best option.

![](./photos/findings-Fitness.png)

### Choosing the initial depth

Similar to the way of examining the fitness calculation, in the question of choosing the proper initial depth, the algorithm was tested by comparing the results to Paris's monthly average weather in 2013. We ran with 1000 generations.
At first, we performed evolutionary experiments with parameters taken from the Symbolic Regression example in the EC-KitY wiki. While running the experiments, we found that changing the init_depth from (2, 4) to (2, 7) singnifintly improve on the performance and accuracy of the model. The initial depth of a GP tree, also known as the tree depth of the initial population, refers to the maximum depth of the trees in the initial population of solutions generated by the GP algorithm. The initial depth of the GP tree can affect the performance of the evolutionary algorithm in several ways:

1. A deeper tree may be able to represent more complex solutions to the problem, which may result in better performance.
2. A deeper tree may require more computational resources to evaluate and may result in slower convergence of the algorithm. On the other hand, a shallow tree may be faster to evaluate but may be unable to represent complex solutions.
3. The initial depth of the GP tree can also influence the diversity of the initial population, which can affect the performance of the evolutionary algorithm. A diverse initial population may result in a more efficient search of the solution space, while a less diverse population may result in a less efficient search.

In the following graph you can see the difference between the findings of the two experiments:

![](./photos/findings-initial-depth.png)

### Choosing the terminal set

The terminal set is a set of values or variables that can be used as leaf nodes in the tree which is a representation of a solution to a problem. We extend the default constances list from (0, 1, -1) to (0, 1, -1, 5, 10). The choice of constants in the terminal set can have a significant impact on the performance of a GP evolutionary algorithm. Here are a few ways in which the constants in the terminal set can affect the algorithm:

1. A terminal set with a wider range of constants may be able to represent more complex solutions
2. A larger number of constants may increase the diversity of the initial population and may result in a more efficient search of the solution space.

We can see in the following chart the chosen terminal set doesn't bring a big change. However, the change made the tree more readable and bring a better performance.

![](./photos/findings-terminal-set.png)

### Choosing the tournament size

The tournament size in an evaluation algorithm refers to the number of individuals that are selected to compete in a tournament to determine which individual will be selected for reproduction.

A larger tournament size will result in stronger selection pressure and a more thorough evaluation of the population, as more individuals will be compared to one another. Therefore, the individuals that are selected for the tournament will likely have better fitness values.

However, a larger tournament size will also increase the computational costof the algorithm.

A smaller tournament size will result in weaker selection pressure. Therefore, the individuals that are selected for the tournament likely have a more varied range of fitness values. The more heterogenic population makes it easier for the algorithm to find new solutions. And it is more likely for the algorithm to prevent stuck in a local optimum.

When choosing tournament size, it is a trade-off between exploration and exploitation.

In our algorithm, we chose to use a tournament in size 4. A tournament size of 4 allows for a balance between exploration and exploitation, as it allows the algorithm to keep a diverse population while still allowing the best individuals to reproduce.

![](./photos/findings-toutnamain-size.png)

### Choosing the maximum generation number

The maximum generation is a parameter that specifies the maximum number of iterations or generations that the GP algorithm will run for. The maximum generation determines the length of the evolutionary process and is an important parameter in a GP evolutionary algorithm and can affect the performance, convergence, and diversity of the solutions:

1. A larger maximum generation allows the GP algorithm to run for more iterations and potentially discover better solutions to the problem.
2. The maximum generation affects the convergence of the GP algorithm. If the maximum generation is too small, the algorithm may not have enough time to fully explore the solution space and may not converge to a good solution.
3. The maximum generation influences the diversity of the population of solutions. A larger maximum generation may allow the population to evolve and explore a wider range of solutions, while a smaller maximum generation may result in a less diverse population.

We choose to set the max generation value to 1000. We are aware that increasing this parameter might even get better results, but we chose not to do this due to resources and running time reasons.

Below you can see that there is a direct relationship between the number of generations and the accuracy of the temperature that the algorithm found:

![](./photos/findings-max-generation-number.png)

## Conclusions

 In conclusion, our project aimed to investigate the possibility of predicting the weather using an evolution algorithm. Through our research and experimentation, we found that it is indeed possible to predict the weather using this approach. Furthermore, we see potential for extending our algorithm to predict other weather aspects such as precipitation and wind. Our results also highlighted the importance of properly selecting evolution algorithm factors such as fitness, initial depth, terminal set, and maximum generation number as they can have a significant impact on the algorithm's results. Overall, this project has demonstrated the potential of evolution algorithms in the field of weather prediction and opens up new possibilities for further research and development in this area.



## Bibliography
https://en.wikipedia.org/wiki/Weather#Forecasting

[https://education.nationalgeographic.org/resource/weather](https://education.nationalgeographic.org/resource/weather)

https://www.fs.usda.gov/ccrc/education/climate-primer/natural-climate-cycles

https://www.sciencedirect.com/topics/computer-science/evolutionary-programming

https://link.springer.com/article/10.1007/s10710-021-09410-y

https://www.sciencedirect.com/science/article/abs/pii/S002002551930578X
