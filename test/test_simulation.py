import pytest
from musguito.simulation import Plant, distance, growth_factor

def test_plant_grow():
    plant = Plant(0, 0, 10, 5)
    initial_height = plant.current_height
    initial_diameter = plant.current_diameter
    plant.grow(1)  # Growth factor of 1
    assert plant.current_height > initial_height, "Plant height did not increase."
    assert plant.current_diameter > initial_diameter, "Plant diameter did not increase."

def test_distance():
    plant1 = Plant(0, 0, 10, 5)
    plant2 = Plant(3, 4, 10, 5)
    assert distance(plant1, plant2) == 5, "Distance calculation is incorrect."

def test_growth_factor_no_neighbors():
    plant = Plant(0, 0, 10, 5)
    plants = [plant]
    assert growth_factor(plant, plants) == 1, "Growth factor should be 1 when there are no neighbors."

def test_growth_factor_with_neighbors():
    plant1 = Plant(0, 0, 10, 5)
    plant2 = Plant(1, 1, 10, 5)
    plant3 = Plant(2, 2, 10, 5)
    plants = [plant1, plant2, plant3]
    assert growth_factor(plant1, plants) == 11, "Growth factor is incorrect when there are neighbors."

if __name__ == "__main__":
    pytest.main()
