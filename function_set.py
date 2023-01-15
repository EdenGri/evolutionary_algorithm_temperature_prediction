import numpy as np
from eckity.genetic_encodings.gp.tree.functions import f_add, f_mul, f_sub, f_div, f_sqrt, f_log, f_abs, f_max, f_min, f_inv, f_neg, f_sin, f_cos, f_tan


def f_mod(x, y):
    """x%y"""
    """protected modulo: if abs(y) > 0.001 return x%y else return 0"""
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(np.abs(y) > 0.001, np.mod(x, y), 0.)

function_set = [f_add, f_sub, f_mul, f_div, f_sqrt, f_log, f_abs, f_neg, f_inv, f_max, f_min, f_sin, f_cos, f_tan, f_mod]