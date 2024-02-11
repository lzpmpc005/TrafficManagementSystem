import json
from collections import Counter
import matplotlib.pyplot as plt

def visualize_car_counts_from_file(file_path):
    with open(file_path, 'r') as f:
        car_data = json.load(f)

    periods = [entry['period'] for entry in car_data]
    car_counts = Counter(periods)

    periods = list(car_counts.keys())
    car_numbers = list(car_counts.values())

    plt.bar(periods, car_numbers, color='skyblue')
    plt.xlabel('Period')
    plt.ylabel('Number of Cars')
    plt.title('Number of Cars in Each Period')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

file_path = '/Users/charton/Git/TrafficManagementSystem/junctions_log_2024-03-25.json'
visualize_car_counts_from_file(file_path)
