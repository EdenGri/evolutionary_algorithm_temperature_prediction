<!-- Output copied to clipboard! -->

<!-- You have some errors, warnings, or alerts. If you are using reckless mode, turn it off to see inline alerts.
* ERRORs: 0
* WARNINGs: 0
* ALERTS: 11 -->
<h2>
<img src="images/image1.png" width="" alt="alt_text" title="image_tooltip">
</h2>
<h2>Mini – Project </h2>
<h2>on</h2>
<h2> Evolutionary Algorithm<br>Temperature Prediction</h2>
<p>
<span style="text-decoration:underline;">Submitted by: </span>
</p>
<p>
Yuval Beker 209026384<br> Gil Shmaya 209327303<br>Eden Grisaro
316440767
</p>
<p>
<span style="text-decoration:underline;">Course lecturer:</span>
</p>
<p>
Prof. Moshe Sipper
</p>
<p>
December 2022
</p>
<h2>Table of Contents</h2>
<h2>Introduction<br>Our project focuses on predicting the weather using
an evaluation algorithm. <br><br>Whether we have a school trip, go
on a vacation or even plan a picnic outside, the weather has a big influence on
how things will go. It meets us in many situations and the power of predicting
it can have a huge influence in our daily day time.</h2>
<p>
Weather is the state of the atmosphere, describing the degree to which it is hot
or cold, wet or dry, calm or stormy, clear or cloudy. The weather is measured by
temperature, wind, humidity, and atmospheric pressure. There are also properties
that affect it, such as altitude.Higher altitudes are cooler than lower
altitudes, as most atmospheric heating is due to contact with the Earth's
surface while radiative losses to space are mostly constant. The differences in
the weather occur due to the sun angle as well. For example, In June the
Northern Hemisphere is tilted towards the sun. This is what causes seasons. Also
there is evidence that human activities such as industry have modified weather
patterns.
</p>
<p>
Weather forecasting is the application of science and technology to predict the
state of the atmosphere for a future time and a given location. Weather
forecasts are made by collecting quantitative data about the current state of
the atmosphere and using scientific understanding of atmospheric processes to
project how the atmosphere will evolve.There are a variety of end users to
weather forecasts. Weather warnings are important forecasts because they are
used to protect life and property. Forecasts based on temperature and
precipitation are important to agriculture, and therefore to commodity traders
within stock markets. Temperature forecasts are used by utility companies to
estimate demand over coming days.
</p>
<p>
In some areas, people use weather forecasts to determine what to wear on a given
day. Since outdoor activities are severely curtailed by heavy rain, snow and the
wind chill, forecasts can be used to plan activities around these events and to
plan ahead to survive through them.
</p>
<p>
In this project we will explore the weather in X and try to forecast the
upcoming weather.
</p>
<p>
Problem Description
</p>
<p>
<br><strong><span style="text-decoration:underline;">The Problem:
</span></strong> Development of a function that predicts  the weather of a given
date.
</p>
<p>
<strong><span style="text-decoration:underline;">Our search space:</span>
</strong>We took data from ____ of the weather of ___. <br>
</p>
<p>
<strong><span style="text-decoration:underline;">Weather
characteristics:</span></strong> In general there are six main components, or
parts, of weather:<br>1. <span
style="text-decoration:underline;">temperature -</span> refers to how hot or
cold the atmosphere is.The coldest weather usually happens near the poles, while
the warmest weather usually happens near the Equator.
</p>
<p>
2. <span style="text-decoration:underline;">atmospheric pressure -</span> the
weight of the atmosphere overhead. Changes in atmospheric pressure signal shifts
in the weather. A high-pressure system usually brings cool temperatures and
clear skies. A low-pressure system can bring warmer weather, storms, and rain.
Atmospheric pressure changes with altitude. The atmospheric pressure is much
lower at high altitudes.
</p>
<p>
3. <span style="text-decoration:underline;">wind -</span> the movement of air.
Wind forms because of differences in temperature and atmospheric pressure
between nearby regions. Winds tend to blow from areas of high pressure, where
it’s colder, to areas of low pressure, where it’s warmer.
</p>
<p>
4. <span style="text-decoration:underline;">humidity -</span> Humidity refers to
the amount of water vapor in the air. Water vapor is a gas in the atmosphere
that helps make clouds, rain, or snow. Humidity is usually expressed as relative
humidity, or the percentage of the maximum amount of water air can hold at a
given temperature. Cool air holds less water than warm air.
</p>
<p>
5. <span style="text-decoration:underline;">cloudiness -</span> Clouds come in a
variety of forms. Some signal mild weather, and others can bring rain or snow.
Clouds can affect the amount of sunlight reaching the Earth’s surface. Cloudy
days are cooler than clear ones because clouds prevent more of the sun’s
radiation from reaching the Earth’s surface. <br><br> We decided
to use temperature as our measurement of the
weather.<br><br><strong><span
style="text-decoration:underline;">Our goal: </span></strong>We would like to
predict the weather of the same place using the function that was created.
</p>
<p>
<strong><span style="text-decoration:underline;"><br>Our
problems:</span></strong>
</p>
<ul>
<li>weather is unpredictable
<li>there are many characteristics that also affect the weather except
temperature
<li>human involvement can also affect the weather
<li>global warming has a large impact on the weather
</li>
</ul>
<p>
<strong><span style="text-decoration:underline;">assumptions: </span></strong>
</p>
<ul>
<li>Weather is a cyclical process - one of the reasons is that major changes are
initiated by changes in the earth’s orbit around the sun. The orbital changes
occur slowly over time influencing where solar radiation is received on earth’s
surface during different seasons. By themselves, these changes in the
distribution of solar radiation are not strong enough to cause large temperature
changes.
<li>We decided to predict the weather using the temperature because this is one
of the main factors we usually look at when deciding how the weather will be
</li>
</ul>
<p>
</p>
<p>
Genetic Programming
</p>
<p>
<strong><span style="text-decoration:underline;">Individual:</span></strong>
</p>
<p>
In the evolutionary algorithm, an individual is a single potential solution to a
given problem. In our case, the problem is by a given date to predicate the
temperature on this date. We want to solve this problem by generating a
mathematical function approximating the weather. So our single solution is a
mathematical function.
</p>
<p>
We represent the mathematical function as a “Function Tree” GP. In the “Function
Tree” the inner nodes will be from the “function set” and the leaves from the
“terminal set".
</p>
<p>
<strong><span style="text-decoration:underline;">Function set:</span></strong>
</p>
<p>
In the context of genetic programming, a “function set” is a set of functions
that can be used to build the solution to a given problem. The "function set" is
used to build the initial population of solutions, which evolved over time.
</p>
<p>
In our system, the "function set" is pre-defined and fixed and consists of a set
of basic mathematical functions that can be combined to build more complex
solutions.
</p>
<p>
Our “function set” includes the following basic arithmetic functions:
</p>
<ul>
<li>addition - “f_add”
<li>subtraction - “f_sub”
<li>multiplication- “f_mul”
<li>division - “f_div”
<li>log - “f_log”
<li>root - “f_sqrt”
<li>absolute value - “f_abs”
<li>inverseinverse - “f_inv”
<li>negative - “f_neg”
<li>maximum - “f_max”
<li>minimum - “f_min”
<li>sin - “f_sin”
<li>cos - “f_cos”
<li>tan - “f_tan”
<li>modulo - “f_mod”
</li>
</ul>
<p>
The "function set" is the set of all possible internal nodes of the tree.
</p>
<p>
Besides the arithmetic functions that we have in GP we add the "f_mod" function.
We wanted to add cyclic elements in our individuals since we know the weather
has cyclic elements.
</p>
<p>
……………………todo: mod function……………………
</p>
<p>
<strong><span style="text-decoration:underline;">Terminal set:</span></strong>
</p>
<p>
A “terminal set” is a set of values that do not change and are pre-oriented. The
"terminal set" can be used as inputs to the functions in the "function set", and
they are used to build the initial population of solutions, which developed.
</p>
<p>
In our case, the “terminal set” includes constants numbers [0, 1, -1, 5, 10] and
the variables [..........todo complete………………………].
</p>
<p>
……………………………..to add our terminal set……………….
</p>
<p>
At the beginning of the implementation, we considered only the [0, 1,-1]
constants, but we didn’t get good results. The cause was it was hard to generate
common temperatures such as 35 celsius since it requiere a high tree, and we got
limitations on the tree's height (7). After we added to [10, 5] constants, our
results improved.
</p>
<p>
The “terminal set”  is the leaves in the tree.
</p>
<p>
<img src="images/image2.png" width="" alt="alt_text" title="image_tooltip">
</p>
<p>
This diagram represents an example of an individual when the blue squares are
nodes from the function set, and the orange circles are leaves from the terminal
set.
</p>
<p>
<strong><span style="text-decoration:underline;">initialize
subpopulation:</span></strong>
</p>
<p>
A population is a group of individuals that are being evolved through the use of
genetic algorithms. The population as a whole represents a variety of possible
solutions to this problem. Our subpopulation is a collection of “Function Tree”
GPs.
</p>
<p>
<strong>Creating individuals</strong>
</p>
<p>
In creating the individuals, we have created ramped half and half trees with an
init depth of 2 to 7. We added bloat values to slow down the tree's growth, and
we chose our population to contain 300 individuals.
</p>
<p>
<strong>Initialization method:</strong> Ramped half and half trees are used to
generate the initial population of individuals (GA) for generating a function
that will predict temperature. We chose this function because it is a good
initialization method for symbolic regression problems that we can transform
into our problem.
</p>
<p>
The Ramped half and half method start by creating a set of "half and half"
trees, where each tree has a random number of nodes, with the restriction that
the number of terminal nodes must be less than or equal to the number of
non-terminal nodes. This is done to ensure that the initial population is
diverse and has a balance of simple and complex individuals. The method then
"ramps" the size of the trees by gradually increasing the maximum depth of the
trees until the desired size is reached. This gradually increases complexity in
the initial population, allowing the GA to explore a wide range of solutions and
avoid getting stuck in local optima.
</p>
<p>
<strong>Tree depth:</strong> During the implementation, we see that the height
of an individual's Function tree significantly impacts its performance. When the
tree was too deep, it prone to overfitting, while when it was too shallow, it
did not have enough complexity to solve the problem effectively. Ultimately, we
choose the initial depth of 2 to 7 after a few different runnings.
</p>
<p>
<img src="images/image3.png" width="" alt="alt_text" title="image_tooltip">
</p>
<p>
<strong><span style="text-decoration:underline;">The evolution:</span></strong>
</p>
<p>
<strong><span style="text-decoration:underline;">fitness</span></strong>:
</p>
<p>
The fitness function uses us to measure the quality or effectiveness of a
particular solution or individual in a population. The fitness function returns
a value representing how well an individual's genetically suited to solving a
given problem or achieving a specific goal.
</p>
<p>
In our case, the fitness function is used to evaluate the fitness of each
individual in the population. It is typically designed to be specific to solve
the problem of predicting the temperature when given a date.
</p>
<p>
Our fitness function is Mean Absolute Error (MAE). MAE is calculated as the
average absolute difference between predicted and actual temperature values
(predicted - self.df[target], actual -  individual.execute(x=x, y=y, z=z)). The
absolute difference between the predicted and real value is taken to handle the
negative values of difference.
</p>
<p>
todo—-------------------comlete
</p>
<p>
<img src="images/image4.png" width="" alt="alt_text" title="image_tooltip">
</p>
<p>
Since, in our case, the fitness function acts like a loss function, we want to
minimize our fitness function. <code>higher_is_better=False</code>
</p>
<p>
We implement the _evaluate_individual method, which evaluates a <strong>fitness
</strong>score for an individual:
</p>


<pre
class="prettyprint">def _evaluate_individual(self, individual):
   x, y, z = self.df['x'], self.df['y'], self.df['z']
   return np.mean(np.abs(individual.execute(x=x, y=y, z=z) - self.df['target']))
</pre>
<p>
<strong>selection:</strong>
</p>
<p>
Selection refers to the process of choosing which individuals from a population
will be selected to participate in the reproduction process to generate the next
generation. The individuals that are selected in our project  are those that
have lower fitness values, meaning they are better suited to solving the problem
at hand.
</p>
<p>
We choosed that our selection be done using tournament selection. We chosed the
tournament selection since it allows the algorithm to keep a diverse population
while still allowing the best individuals to reproduce.
</p>
<p>
In general Tournament selection involves selecting a small number of individuals
from the population at random and then comparing their fitness values. The
individual with the highest fitness value is then selected as the "winner" and
is given the opportunity to reproduce and pass on their genetic information to
the next generation. <br>In our case we defined that we prefer lower
fitness value, in our case the ‘“winner” will be with the lowest fitness value.
</p>
<p>
The number of individuals selected for the tournament is called the “tournament
size”, we chose a tournament size of 4. We found that the size 4 is a good
balance between exploration and exploitation. The size of 4 provide us a
stronger selection pressure, which helped to converge on an optimal solution
more quickly.
</p>
<p>
We didn’t increase the size more then 4 A larger tournament size will result in
stronger selection pressure, and therefore, the individuals that are selected
for the tournament will tend to have higher fitness values. A smaller tournament
size will result in weaker selection pressure, and therefore, the individuals
that are selected for the tournament will tend to have a more varied range of
fitness values.
</p>
<p>
A tournament size of 2 allows for a balance between exploration and
exploitation, as it allows the algorithm to keep a diverse population while
still allowing the best individuals to reproduce.
</p>
<p>
We configured the Tournament Selection with a probability of 1.
</p>
<p>
<img src="images/image5.png" width="" alt="alt_text" title="image_tooltip">
</p>
<p>
The selection process is a crucial step in the genetic algorithm as it
determines which individuals will pass on their genetic information to the next
generation.
</p>
<p>
<strong>Breeding process:</strong>
</p>
<p>
We set the hyperparameters for the breeding process:
</p>
<ul>
<li>We chose an elitism rate that determines that 5% of the population's top
individuals will be copied as-is to the next generation in each generation.
</li>
</ul>
<p>
We defined genetic operators to be applied in each generation:
</p>
<ul>
<li>Subtree Crossover with a probability of 90%
<li>Subtree Mutation with a probability of 20%
<li>ERC Mutation with a probability of 5%
</li>
</ul>
<p>
(The total of probabilities does not complete to 100% because the operators are
applied one after the other, in a linear sequence).
</p>
<p>
<img src="images/image6.png" width="" alt="alt_text" title="image_tooltip">
</p>
<p>
todo:
</p>
<p>
change x y z to date
</p>
<p>
remove not necessary functions
</p>
<p>
add function that get date from user and return temperuture
</p>
<p>
change the class to something for temperature , enter this part to the software
</p>
<h2>Experiments & Findings </h2>
<h2><strong><span style="text-decoration:underline;">Choosing the
fitness</span></strong> <br>In evolutionary algorithms, the fitness value
measures how well a particular solution performs in relation to a particular
problem. When selecting a fitness value for an evolutionary algorithm, it is
important to consider how well the value reflects the desired characteristics of
the solution. For example, in our case, the goal is to find a solution, the
weather measures for a requested month, that are as close as possible to a
particular target value, the average monthly weather graph in the last
years.</h2>
<p>
In the process of choosing the suitable fitness, we examined two different
options. The two options are MAE fitness that are differ in there calculation.
MAE stands for Mean Absolute Error. In the context of fitness, it may refer to
the error or difference between the predicted value of a fitness function and
the true value. <br>1. <span style="text-decoration:underline;">Using an
average operation in the fitness calculation</span> - we want to minimize the
<strong>average</strong> of the differences between the temperature predicted by
the algorithm and the real temperature. In other words, higher fitness means
high differences, so in that case we set the parameter<em> higher_is_better</em>
to be false.
</p>
<p>
2. <span style="text-decoration:underline;">Using an maximum operation in the
fitness calculation</span> - we want to minimize the <strong>maximum</strong>
difference between the temperature predicted by the algorithm and the real
temperature. In that case case we set the parameter<em> higher_is_better</em> to
be false as well.
</p>
<p>
For unsering that question, we ran experiment with 500 generations for each
fitness methos. We examined the results of each fitness by comparing them to the
real temperature occured in Paris on every month in 2013. As you can notice from
the below table, the average fitness was chosen as the best option.<br>
</p>
<p>
<img src="images/image7.png" width="" alt="alt_text" title="image_tooltip">
</p>
<p>
<br><strong><span style="text-decoration:underline;">Choosing the initial
depth </span></strong>
</p>
<p>
Similar to the way of examinding the fitness calculation, the algorithm was
tested by comparing the results to Paris monthly average weather in 2013. We ran
with 1000 generations. <br>At first, we performed evolutionary
experiments with parameters taken from the Symbolic Regression example in the
EC-KitY wiki. While running the experiments, we found that changing the
init_depth from (2, 4) to (2, 7) singnifintly improve on the performance and
accuracy of the model. The initial depth of a GP tree, also known as the tree
depth of the initial population, refers to the maximum depth of the trees in the
initial population of solutions generated by the GP algorithm. The initial depth
of the GP tree can affect the performance of the evolutionary algorithm in
several ways:
</p>
<ol>
<li>A deeper tree may be able to represent more complex solutions to the
problem, which may result in better performance.
<li>A deeper tree may require more computational resources to evaluate and may
result in slower convergence of the algorithm. On the other hand, a shallow tree
may be faster to evaluate but may be unable to represent complex solutions.
<li>The initial depth of the GP tree can also influence the diversity of the
initial population, which can affect the performance of the evolutionary
algorithm. A diverse initial population may result in a more efficient search of
the solution space, while a less diverse population may result in a less
efficient search.
</li>
</ol>
<p>
In the following graph you can see the difference between the findings of the
two experiments:
</p>
<p>
<img src="images/image8.png" width="" alt="alt_text" title="image_tooltip">
</p>
<p>
<strong><span style="text-decoration:underline;">Choosing the terminal
set</span></strong>
</p>
<p>
The terminal set is a set of values or variables that can be used as leaf nodes
in the tree which is a representation of a solution to a problem. We extend the
default constances list from (0, 1, -1) to (0, 1, -1, 5, 10). The choice of
constants in the terminal set can have a significant impact on the performance
of a GP evolutionary algorithm. Here are a few ways in which the constants in
the terminal set can affect the algorithm:
</p>
<ol>
<li>A terminal set with a wider range of constants may be able to represent more
complex solutions
<li>A larger number of constants may increase the diversity of the initial
population and may result in a more efficient search of the solution space.
</li>
</ol>
<p>
We can see in the following chart the chosen terminal set doesn’t bring a big
change. However, the change made the tree more readable and performanse is
better.
</p>
<p>
<img src="images/image9.png" width="" alt="alt_text" title="image_tooltip">
</p>
<p>
<strong><span style="text-decoration:underline;">Choosing the tournament
size</span></strong>
</p>
<p>
The tournament size in an evaluation algorithm refers to the number of
individuals that are selected to compete in a tournament to determine which
individual will be selected for reproduction. A larger tournament size will
result in a more thorough evaluation of the population, as more individuals will
be compared to one another. However, a larger tournament size will also increase
the computational cost of the algorithm. So, when choosing the tournament size,
it is a trade-off between the thoroughness of the evaluation and the
computational cost of the algorithm.
</p>
<p>
In our algorithm, we chose to use a tournament in size 4.
<img src="images/image10.png" width="" alt="alt_text" title="image_tooltip">
</p>
<p>
<strong><span style="text-decoration:underline;">Choosing the maximum generation
number</span></strong>
</p>
<p>
The maximum generation is a parameter that specifies the maximum number of
iterations or generations that the GP algorithm will run for. The maximum
generation determines the length of the evolutionary process and is an important
parameter in a GP evolutionary algorithm and can affect the performance,
convergence, and diversity of the solutions:
</p>
<ol>
<li>A larger maximum generation allows the GP algorithm to run for more
iterations and potentially discover better solutions to the problem.
<li>The maximum generation affects the convergence of the GP algorithm. If the
maximum generation is too small, the algorithm may not have enough time to fully
explore the solution space and may not converge to a good solution.
<li>The maximum generation influences the diversity of the population of
solutions. A larger maximum generation may allow the population to evolve and
explore a wider range of solutions, while a smaller maximum generation may
result in a less diverse population.
</li>
</ol>
<p>
We choose to set the max generation value to 1000. We are aware that increasing
this parameter might even get a better results, but we chose not to do this due
to resources and running time reasons.
</p>
<p>
Below you can see that there is a direct relationship between the number of
generations and the accuracy of the temperature that the algorithm found:
</p>
<p>
<img src="images/image11.png" width="" alt="alt_text" title="image_tooltip">
</p>
<p>
Conclusions<br>In conclusion, our project aimed to investigate the
possibility of predicting the weather using an evolution algorithm. Through our
research and experimentation, we found that it is indeed possible to predict the
weather using this approach. Furthermore, we see potential for extending our
algorithm to predict other weather aspects such as precipitation and wind. Our
results also highlighted the importance of properly selecting evolution
algorithm factors such as fitness, initial depth, terminal set, and maximum
generation number as they can have a significant impact on the algorithm's
results. Overall, this project has demonstrated the potential of evolution
algorithms in the field of weather prediction and opens up new possibilities for
further research and development in this area.
</p>
<p>
https://en.wikipedia.org/wiki/Weather#Forecasting
</p>
<p>
<a
href="https://education.nationalgeographic.org/resource/weather">https://education.nationalgeographic.org/resource/weather</a>
</p>
<p>
https://www.fs.usda.gov/ccrc/education/climate-primer/natural-climate-cycles
</p>
