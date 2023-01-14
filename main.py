from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.creators.gp_creators.ramped_hh import RampedHalfAndHalfCreator
from eckity.genetic_operators.crossovers.subtree_crossover import SubtreeCrossover
from eckity.genetic_operators.mutations.erc_mutation import ERCMutation
from eckity.genetic_operators.mutations.subtree_mutation import SubtreeMutation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics
from eckity.subpopulation import Subpopulation
from eckity.termination_checkers.threshold_from_target_termination_checker import ThresholdFromTargetTerminationChecker

from temperature_evaluator import TemperatureEvaluator

from user_interface import get_bloat_weight, get_init_depth, get_population_size, should_use_recommended_settings, \
    check_temperature_of_dates_from_user, get_max_generation, print_predicted_temperatures_for_year
from function_set import function_set
from terminal_set import terminal_set


if __name__ == '__main__':

    use_default_settings = should_use_recommended_settings()

    algo = SimpleEvolution(
        Subpopulation(creators=RampedHalfAndHalfCreator(init_depth=get_init_depth(use_default_settings),
                                                        terminal_set=terminal_set,
                                                        function_set=function_set,
                                                        bloat_weight=get_bloat_weight(use_default_settings)),
                      population_size=get_population_size(use_default_settings),
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
        max_generation=get_max_generation(use_default_settings),
        termination_checker=ThresholdFromTargetTerminationChecker(optimal=0, threshold=0.001),
        statistics=BestAverageWorstStatistics()
    )
    algo.evolve()

    print_predicted_temperatures_for_year(algo, 2013)
    check_temperature_of_dates_from_user(algo)
