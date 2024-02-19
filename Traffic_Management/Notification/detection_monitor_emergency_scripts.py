import json
import random
import os
from .fake_plate import generate_fake_plates, read_fake_plates

def generate_junction_logs(date, city, junction_name):

    formatted_date = date
    fake_city = city
    fake_junction = junction_name

    folder_name = f"{fake_city}_{fake_junction}_{formatted_date}_logs"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    morning_peak_hours = [6, 7, 8, 9, 10]
    evening_peak_hours = [16, 17, 18, 19, 20]

    plates_random = generate_fake_plates()
    plates_from_file = read_fake_plates("/Users/charton/Git/TrafficManagementSystem/fake_plates_20240217_132316.json")
    plates_of_emergency = read_fake_plates("/Users/charton/Git/TrafficManagementSystem/fake_plates_emergency.json")

    junctions_log = []
    for hour in range(24):

        if hour in morning_peak_hours or hour in evening_peak_hours:
            number_records = random.randint(1, 3)
        else:
            number_records = random.randint(1, 2)

        for _ in range(number_records):
                    
            if _ == 2:
                number_plate = random.choice(plates_of_emergency)["number_plate"]
                given_speed = random.choice([0, 200])
            else:
                number_plate = random.choice(plates_from_file)["number_plate"]
                given_speed = 50

            log = {
                'numberPlate': number_plate,
                'dateTime': formatted_date,
                'period': f'{hour}:00 - {hour+1}:00',
                'location': fake_junction,
                'speed': given_speed,
                'hitSuspicion': random.choice([True, False]),
                'redlightSuspicion': random.choice([True, False]),
                'beltStatus': random.choice([True, False]),
                'phoneStatus': random.choice([True, False]),
            }
            junctions_log.append(log)

    file_name = os.path.join(folder_name, f"junctions_log_{formatted_date}.json")
    with open(file_name, 'w') as json_file: 
        json.dump(junctions_log, json_file, indent=4)
    
    return 0

if __name__ == "__main__":
    date = '2024-02-19'
    city = 'London'
    junction_name = 'London_Bridge'
    all_junctions = generate_junction_logs(date, city, junction_name)
