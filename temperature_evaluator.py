from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
import pandas as pd
import numpy as np


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

