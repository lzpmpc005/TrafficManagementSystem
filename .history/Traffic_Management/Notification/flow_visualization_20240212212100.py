import json
from collections import Counter
import matplotlib.pyplot as plt
from predict_traffictime_nextday_v2 import predict_next_day_traffic

def visualize_flow(folder_name):
   
    result = predict_next_day_traffic(folder_name)
    flow_data=result[0]
    
    periods = []
    flows = []

    for f in flow_data:
        period, flow = f.split(': ')
        periods.append(period)
        flows.append(float(flow))

    plt.bar(periods, flows, color='skyblue')
    plt.xlabel('Period')
    plt.ylabel('Number of Cars')
    plt.title('Number of Cars in Each Period')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

    image_path = '/Users/charton/Git/TrafficManagementSystem/Graphics'
    image_file = f'{image_path}{folder_name}'

    plt.savefig(image_file)
    
    plt.clf()