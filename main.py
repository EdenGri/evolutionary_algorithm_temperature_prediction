import numpy as np
import pandas as pd
import time
import datetime
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
from examples.treegp.non_sklearn_mode.symbolic_regression.sym_reg_evaluator import SymbolicRegressionEvaluator


def _target_func(x, y, z):
    """
    True regression function, the individuals
    Parameters
    ----------
    x, y, z: float
        Values to the parameters of the function.
    """
    return x + 2 * y + 3 * z


def f_mod(x, y):
    """x%y"""
    """protected division: if abs(y) > 0.001 return x/y else return 0"""
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(np.abs(y) > 0.001, np.mod(x, y), 0.)


class SymbolicRegressionEvaluator(SimpleIndividualEvaluator):
    """
    Compute the fitness of an individual.
    """

    def __init__(self):
        super().__init__()

        # np.random.seed(0)
        #data = np.random.uniform(-100, 100, size=(200, 3))
        #data = pd.read_csv("data.csv")
        data = pd.read_csv("temperature_data.csv")
        self.df = pd.DataFrame(data.values, columns=['x', 'y', 'z', 'target'])
        #self.df = pd.DataFrame(data, columns=['x', 'y', 'z'])
        #self.df['target'] = _target_func(self.df['x'], self.df['y'], self.df['z'])

    def _evaluate_individual(self, individual):
        x, y, z = self.df['x'], self.df['y'], self.df['z']
        return np.mean(np.abs(individual.execute(x=x, y=y, z=z) - self.df['target']))


if __name__ == '__main__':
    # each node of the GP tree is either a terminal or a function
    # function nodes, each has two children (which are its operands)

    function_set = [f_add, f_mul, f_sub, f_div, f_sqrt, f_log, f_abs, f_max, f_min, f_inv, f_neg]

    my_full_function_set = [f_add, f_sub, f_mul, f_div, f_sqrt, f_log, f_abs, f_neg, f_inv, f_max, f_min, f_sin, f_cos,
                         f_tan, f_mod]
    # terminal set, consisted of variables and constants
    terminal_set = ['x', 'y', 'z', 0, 1, -1, 5, 10]
    algo = SimpleEvolution(
        Subpopulation(creators=RampedHalfAndHalfCreator(init_depth=(2, 7),
                                                        terminal_set=terminal_set,
                                                        function_set=my_full_function_set,
                                                        bloat_weight=0.0001),
                      population_size=300,
                      # user-defined fitness evaluation method
                      evaluator=SymbolicRegressionEvaluator(),
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
        max_generation=500,
        # random_seed=0,
        termination_checker=ThresholdFromTargetTerminationChecker(optimal=0, threshold=0.001),
        statistics=BestAverageWorstStatistics()
    )
    #algo = SimpleEvolution(Subpopulation(SymbolicRegressionEvaluator()))
    algo.evolve()
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=1, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=2, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=3, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=4, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=5, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=6, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=7, y=1, z=2013)}')
    print(f'algo.execute(x=2,y=3,z=4): {algo.execute(x=8, y=1, z=2013)}')