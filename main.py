import numpy as np
import pandas as pd
from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.gp_creators.ramped_hh import RampedHalfAndHalfCreator
from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
from eckity.genetic_encodings.gp.tree.functions import full_function_set, f_add, f_mul, f_sub, f_div, f_sqrt, f_log, f_abs, f_max, f_min, f_inv, f_neg, f_sin, f_cos, f_tan
from eckity.genetic_operators.crossovers.subtree_crossover import SubtreeCrossover
from eckity.genetic_operators.mutations.erc_mutation import ERCMutation
from eckity.genetic_operators.mutations.subtree_mutation import SubtreeMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.termination_checkers.threshold_from_target_termination_checker import ThresholdFromTargetTerminationChecker


def f_mod(x, y):
    """x%y"""
    """protected modulo: if abs(y) > 0.001 return x%y else return 0"""
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(np.abs(y) > 0.001, np.mod(x, y), 0.)


def user_interface():
    print("Hi, I'm going to evaluate using evolutionary algorithm the tempature. You can decide to enter your own data or to use our default ones")
    user_input = input("Would you like to enter your own data? yes/no")
    if user_input.__eq__("yes"):
        return False
    return True


def get_init_depth(use_default_data):
    if use_default_data:
        return 2, 7
    min_depth = int(input("choose minimum of initial depth"))
    max_depth = int(input("choose maximum of initial depth"))
    return min_depth, max_depth


def get_bloat_weight(use_default_data):
    if use_default_data:
        return 0.0001
    return float(input("choose bloat weight"))


def get_population_size(use_default_data):
    if use_default_data:
        return 300
    return int(input("choose population size"))


def get_max_generation(use_default_data):
    if use_default_data:
        return 500
    return int(input("choose max generation"))


def check_temperature_of_dates_from_user():
    print("Enter a date you want to check in this format DD.MM.YYYY, when you want to enter stop")
    while True:
        user_input = input("Enter your input: ")
        if user_input == "stop":
            break
        else:
            date = user_input.split(".")
            print(f'The temperature Expected is: {algo.execute(x=date[0], y=date[1], z=date[2])}')


class TemperatureEvaluator(SimpleIndividualEvaluator):
    """
    Compute the fitness of an individual.
    """

    def __init__(self):
        super().__init__()
        data = pd.read_csv("temperature_data.csv")
        self.df = pd.DataFrame(data.values, columns=['month', 'day', 'year', 'target'])

    def _evaluate_individual(self, individual):
        month, day, year = self.df['month'], self.df['day'], self.df['year']
        return np.mean(np.abs(individual.execute(month=month, day=day, year=year) - self.df['target']))


if __name__ == '__main__':
    # each node of the GP tree is either a terminal or a function
    # function nodes, each has two children (which are its operands)

    function_set = [f_add, f_sub, f_mul, f_div, f_sqrt, f_log, f_abs, f_neg, f_inv, f_max, f_min, f_sin, f_cos, f_tan, f_mod]
    # terminal set, consisted of variables and constants
    terminal_set = ['month', 'day', 'year', 0, 1, -1, 5, 10]

    useDefaultData = user_interface()

    algo = SimpleEvolution(
        Subpopulation(creators=RampedHalfAndHalfCreator(init_depth=get_init_depth(useDefaultData),
                                                        terminal_set=terminal_set,
                                                        function_set=function_set,
                                                        bloat_weight=get_bloat_weight(useDefaultData)),
                      population_size=get_population_size(useDefaultData),
                      # user-defined fitness evaluation method
                      evaluator=TemperatureEvaluator(),
                      # minimization problem (fitness is MAE), so higher fitness is worse
                      higher_is_better=False,
                      elitism_rate=0.05,
                      # genetic operators sequence to be applied in each generation
                      operators_sequence=[
                          SubtreeCrossover(probability=0.9, arity=2),
                          SubtreeMutation(probability=0.2, arity=1),
                          ERCMutation(probability=0.05, arity=1)
                      ],
                      selection_methods=[
                          # (selection method, selection probability) tuple
                          (TournamentSelection(tournament_size=4, higher_is_better=False), 1)
                      ]
                      ),
        breeder=SimpleBreeder(),
        max_workers=4,
        max_generation=get_max_generation(useDefaultData),
        termination_checker=ThresholdFromTargetTerminationChecker(optimal=0, threshold=0.001),
        statistics=BestAverageWorstStatistics()
    )
    algo.evolve()

    check_temperature_of_dates_from_user()
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=1, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=2, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=3, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=4, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=5, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=6, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=7, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=8, y=1, z=2013)}')
