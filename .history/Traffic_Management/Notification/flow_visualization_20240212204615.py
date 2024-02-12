import json
from collections import Counter
import matplotlib.pyplot as plt
from User_Service.predict_traffictime_nextday_v2 import predict_next_day_traffic

def visualize_flow(folder_name):
   
    flow_data = 

    periods = [entry['period'] for entry in flow_data]
    flow_counts = Counter(periods)

    periods = list(flow_counts.keys())
    car_numbers = list(flow_counts.values())

    plt.bar(periods, car_numbers, color='skyblue')
    plt.xlabel('Period')
    plt.ylabel('Number of Cars')
    plt.title('Number of Cars in Each Period')
    plt.xticks(rotation=25)
    plt.grid(True)
    plt.show()

