from datetime import datetime
from collections import defaultdict
import json
import os

def predict_next_day_traffic(folder_name):
    days = {}
    
    for i in range(5):
        formatted_date = f'2024-02-0{i+1}'
        folder_path = f'/Users/charton/Git/TrafficManagementSystem/{folder_name}'
        days[formatted_date] = []
        for street in range(5):
            with open(os.path.join(folder_path, f'junctions_log_2024-02-0{i+1}_{street+1}.json'), 'r') as f:
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

    predict_next_day = predict_traffic_time_next_day(days)
    max_traffic_time = max(predict_next_day, key=predict_next_day.get)
    
    result = []
    for period in predict_next_day:
        result.append(f"{period}: {predict_next_day[period]:.2f}")
    
    conclusion = f"Max traffic period in next day at : {max_traffic_time}"

    return '\n'.join(result), conclusion
