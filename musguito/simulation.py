import random
import matplotlib.pyplot as plt
import numpy as np


class Plant:
    def __init__(self, x, y, max_height, max_diameter):
        self.x = x
        self.y = y
        self.current_height = 0.1  # initial height in meters
        self.max_height = max_height
        self.current_diameter = 0.1  # initial diameter in meters
        self.max_diameter = max_diameter

    def grow(self, growth_factor):
        self.current_height += growth_factor * (self.max_height - self.current_height) * 0.01
        self.current_diameter += growth_factor * (self.max_diameter - self.current_diameter) * 0.01

def distance(plant1, plant2):
    return np.sqrt((plant1.x - plant2.x)**2 + (plant1.y - plant2.y)**2)

def growth_factor(plant, plants, influence_radius=3):
    neighbors = [p for p in plants if p != plant and distance(plant, p) < influence_radius]
    return 1 + 10 * len(neighbors)

def simulate_growth(initial_population, repetitions, max_height, max_diameter):
    plants = [Plant(random.uniform(0, 100), random.uniform(0, 100), max_height, max_diameter) for _ in range(initial_population)]

    for _ in range(repetitions):
        for plant in plants:
            factor = growth_factor(plant, plants)
            plant.grow(factor)

    return plants

def plot_plants(plants):
    fig, ax = plt.subplots()
    for plant in plants:
        circle = plt.Circle((plant.x, plant.y), plant.current_diameter / 2 * 5, color='green', fill=True, alpha=0.5)
        ax.add_patch(circle)
    
    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.xlabel('X position (meters)')
    plt.ylabel('Y position (meters)')
    plt.title('Plant Growth Simulation')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

def print_plants_info(plants):
    for i, plant in enumerate(plants, 1):
        print(f"Plant {i}: Position: ({plant.x:.2f}, {plant.y:.2f}), Diameter: {plant.current_diameter:.2f} meters")

if __name__ == "__main__":
    initial_population = int(input("Enter the initial population size: "))
    repetitions = int(input("Enter the number of repetitions: "))
    max_height = float(input("Enter the maximum height of plants in meters: "))
    max_diameter = float(input("Enter the maximum diameter of plants in meters: "))
    
    plants = simulate_growth(initial_population, repetitions, max_height, max_diameter)

    print_plants_info(plants)
    plot_plants(plants)
