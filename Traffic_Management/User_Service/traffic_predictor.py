from collections import defaultdict
import json

# Instruction: 
#you should take data for several days 
#(for example from December 1 to December 5) 
#and ONLY for 1 road section 
#(for example "London Bridge, London"), 
#and the function will predict 
#what will be the busiest time of this road.

class TrafficPredictor:
    def __init__(self):
        self.days = {}

    def load_data(self, start_date, end_date, street):
        self.days = {}
        for i in range((end_date - start_date).days + 1):
            formatted_date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
            self.days[formatted_date] = []
            for _ in range(street):
                with open(f'junctions_log_{formatted_date}_{street}.json', 'r') as f:
                    self.days[formatted_date].append(json.load(f))

    def predict_traffic_time_next_day(self):
        junctions = defaultdict(lambda: defaultdict(int))
        for day in self.days:
            for junction in self.days[day]:
                for log in junction:
                    junctions[log['dateTime'] + '_' + log['location']][log['period']] += 1

        avg_periods = {}

        for day in junctions:
            for period in junctions[day]:
                if period not in avg_periods:
                    avg_periods[period] = 0
                avg_periods[period] += junctions[day][period]

        avg_periods = {k: v / len(self.days) for k, v in avg_periods.items()}

        return avg_periods

    def get_max_traffic_time(self):
        predict_next_day = self.predict_traffic_time_next_day()
        max_traffic_time = max(predict_next_day, key=predict_next_day.get)
        return max_traffic_time

if __name__ == '__main__':
    traffic_predictor = TrafficPredictor()
    traffic_predictor.load_data(datetime(2024, 2, 1), datetime(2024, 2, 5), 1)
    max_traffic_time = traffic_predictor.get_max_traffic_time()
    print(f"Max traffic period in next day at: {max_traffic_time}")
