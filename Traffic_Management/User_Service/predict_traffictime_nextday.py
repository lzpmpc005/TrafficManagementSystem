from datetime import datetime
from collections import defaultdict
import json
import os

# Instruction: 
#you should take data for several days 
#(for example from December 1 to December 5) 
#and ONLY for 1 road section 
#(for example "London Bridge, London"), 
#and the function will predict 
#what will be the busiest time of this road.

days = {}

folder_name='2024-02-06_London_junction_logs'

for i in range(5):
    formatted_date = f'2024-02-0{i+1}'
    days[formatted_date] = []
    for street in range(5):
        with open(os.path.join(folder_name, f'junctions_log_2024-02-0{i+1}_{street+1}.json'), 'r') as f:
            days[formatted_date].append(json.load(f))

def predict_traffic_time_next_day(days):
    junctions = defaultdict(lambda: defaultdict(int))
    for day in days:
        for junction in days[day]:
            for log in junction:
                junctions[log['dateTime']+'_'+log['location']][log['period']] += 1

    avg_periods = {}

    for day in junctions:
        for period in junctions[day]:
            if period not in avg_periods:
                avg_periods[period] = 0
            avg_periods[period] += junctions[day][period]


    avg_periods = {k: v/len(days) for k, v in avg_periods.items()}


    return avg_periods

if __name__ == '__main__':
    predict_next_day = predict_traffic_time_next_day(days)
    max_traffic_time = max(predict_next_day, key=predict_next_day.get)

    for period in predict_next_day:
        print(f"{period}: {predict_next_day[period]:.2f}")

    print(f"Max traffic period in next day at : {max_traffic_time}")
