import json
from collections import Counter
import matplotlib.pyplot as plt
from predict_traffictime_nextday_v2 import predict_next_day_traffic

def visualize_flow(folder_name):
   
    flow_data = predict_next_day_traffic(folder_name).result
    
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
    plt.xticks(rotation=25)
    plt.grid(True)
    plt.show()

folder_name = '2024-02-06_London_junction_logs'
function = visualize_flow(folder_name)