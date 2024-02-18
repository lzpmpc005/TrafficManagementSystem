from datetime import datetime, timedelta
from collections import defaultdict
import json


class Junction:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class TrafficPredator:
    def __init__(self):
        self.days = {}
        self.junctions = {}

    def get_days(self):
        return self.days

    def load_data(self, start_date, end_date, streets):
        self.days = {}
        for i in range((end_date - start_date).days + 1):
            formatted_date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
            self.days[formatted_date] = []
            for street in streets:
                with open(f'junctions_log_{formatted_date}_{street}.json', 'r') as f:
                    self.days[formatted_date].append(json.load(f))

    def predict_traffic_time_next_day(self):
        junctions_traffic = defaultdict(lambda: defaultdict(int))
        for day in self.days:
            for junction in self.days[day]:
                for log in junction:
                    junctions_traffic[log['dateTime']+'_'+log['location']][log['period']] += 1

        avg_periods = {}

        for junction_traffic in junctions_traffic.values():
            for period in junction_traffic:
                if period not in avg_periods:
                    avg_periods[period] = 0
                avg_periods[period] += junction_traffic[period]

        avg_periods = {k: v/len(self.days) for k, v in avg_periods.items()}

        return avg_periods

    def get_max_traffic_time(self):
        predict_next_day = self.predict_traffic_time_next_day()
        max_traffic_time = max(predict_next_day, key=predict_next_day.get)
        return max_traffic_time

    def add_junction(self, name, position):
        self.junctions[name] = Junction(name, position)

    def recommend_substitute(self, current_junction_name):
        current_position = self.junctions[current_junction_name].position
        recommendations = []

        for junction_name, junction in self.junctions.items():
            if junction.position != current_position:
                distance = ((current_position[0] - junction.position[0])**2 + (current_position[1] - junction.position[1])**2)**0.5
                recommendations.append((junction_name, distance))
        recommendations.sort(key=lambda x: x[1])
        return recommendations


if __name__ == '__main__':
    traffic_predictor = TrafficPredator()

    streets = [
        # "Farringdon",
        # "Vauxhall",
        # "Green_Park",
        "London_Bridge",
        # "Tottenham_Court_Road",
    ]

    traffic_predictor.add_junction('London Bridge', (12, 8))
    traffic_predictor.add_junction('Vauxhall', (8, 10))
    traffic_predictor.add_junction('Green_Park', (6, 4))
    traffic_predictor.add_junction('Farringdon', (4, 2))

    traffic_predictor.load_data(datetime(2024, 2, 1), datetime(2024, 2, 5), streets)

    max_traffic_time = traffic_predictor.get_max_traffic_time()
    print(f"Max traffic period in next day at : {max_traffic_time}")

    recommendations = traffic_predictor.recommend_substitute('London Bridge')
    print('Recomendations for substitute:')
    # print(recommendations)
    for recommndation in recommendations:
        print(recommndation[0], '(Distance: ',recommndation[1],')')

