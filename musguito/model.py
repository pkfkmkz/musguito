import pandas as pd
import numpy as np
import random

class BasicMusguito():
    """
    Simulates plants evolution.

    Args:
        param1: This is the first param.
        param2: This is a second param.

    Returns:
        A population of plants.

    Raises:
        KeyError: Raises an exception.
    """
    def __init__(self, **kwargs):
        self.t = 0
        self.population = self.generate_population()
    
    def generate_population(self, **kwargs):
        """
        Generates initial population.

        Args:
            param1: This is the first param.
            param2: This is a second param.

        Returns:
            A population of plants.

        Raises:
            KeyError: Raises an exception.
        """
        # columns = ['id', 'x', 'y', 'height', 'radius', 'green', 'light', 'food']
        initial_size = kwargs.get('initial_size', 100)
        id_list = np.array(list(range(0, initial_size)), dtype=np.uint32)
        x_list = np.array(np.random.choice(list(range(-100, 100)), initial_size), dtype=np.int16)
        y_list = np.array(np.random.choice(list(range(-100, 100)), initial_size), dtype=np.int16)
        height_list = np.array(np.random.choice(list(range(1, 10)), initial_size), dtype=np.uint64)
        radius_list = np.array(np.random.choice(list(range(1, 10)), initial_size), dtype=np.uint64)
        green_list = np.random.random(initial_size)
        light_list = np.array([1.0] * initial_size, dtype=np.float64)
        food_list = np.random.random(initial_size)

        data = {
            'id': id_list, 'x': x_list, 'y': y_list, 'height': height_list, 'radius': radius_list,
            'green': green_list, 'light': light_list, 'food': food_list,
        }

        population = pd.DataFrame(data=data)

        return population


