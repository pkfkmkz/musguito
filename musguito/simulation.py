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
    return np.sqrt((plant1.x - plant2.x) ** 2 + (plant1.y - plant2.y) ** 2)


def growth_factor(plant, plants, influence_radius=3):
    neighbors = [p for p in plants if p != plant and distance(plant, p) < influence_radius]
    return 1 + 10 * len(neighbors)


def simulate_growth(initial_population, repetitions, max_height, max_diameter):
    plants = [
        Plant(random.uniform(0, 100), random.uniform(0, 100), max_height, max_diameter)
        for _ in range(initial_population)
    ]

    fig, ax = plt.subplots()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_xlabel("X position (meters)")
    ax.set_ylabel("Y position (meters)")
    ax.set_title("Plant Growth Simulation")
    ax.set_aspect("equal", adjustable="box")

    circles = []
    for plant in plants:
        circle = plt.Circle(
            (plant.x, plant.y),
            plant.current_diameter / 2 * 3,
            color="green",
            fill=True,
            alpha=0.5,
        )
        circles.append(circle)
        ax.add_patch(circle)

    plt.draw()
    plt.pause(0.1)  # Pause to see the initial plot

    for _ in range(repetitions):
        for plant, circle in zip(plants, circles):
            factor = growth_factor(plant, plants)
            plant.grow(factor)
            circle.set_center((plant.x, plant.y))
            circle.set_radius(plant.current_diameter / 2 * 2)
        plt.draw()
        plt.pause(0.1)  # Pause to see the update


if __name__ == "__main__":
    initial_population = int(input("Enter the initial population size: "))
    repetitions = int(input("Enter the number of repetitions: "))
    max_height = float(input("Enter the maximum height of plants in meters: "))
    max_diameter = float(input("Enter the maximum diameter of plants in meters: "))

    simulate_growth(initial_population, repetitions, max_height, max_diameter)
