import json
import random
import os
from faker import Faker
from datetime import datetime
from fake_plate import generate_fake_plates, read_fake_plates



fake = Faker()

fake_street_names = [
    # "Baker Street",
    # "King's Cross",
    # "Euston",
    # "Farringdon",
    # "Vauxhall",
    # "Green Park",
    "London Bridge",
    # "Tottenham Court Road",
]

fake_cities = [
    "London",
]

def generate_junction_logs():
    current_year = datetime.now().year

    all_days = []

    formatted_date = '2024-02-06'
    folder_name = f"{formatted_date}_{fake_cities[0]}_junction_logs"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    junctions_log = []

    morning_peak_hours = [6, 7, 8, 9, 10]
    evening_peak_hours = [16, 17, 18, 19, 20]

    plates_random = generate_fake_plates()
    plates_from_file = read_fake_plates("fake_plates_20240205_161657.json")

    for j in range(5):
        for i in range(5):
            formatted_date = f'2024-02-0{j+1}_{i+1}'

            road = fake.street_name()
            random_location = f"{random.choice(fake_street_names)}, {random.choice(fake_cities)}"

            for hour in range(24):

                if hour in morning_peak_hours or hour in evening_peak_hours:
                    number_records = random.randint(20, 30)
                else:
                    number_records = random.randint(5, 10)

                for _ in range(number_records):
                    if random.random() <= 0.8:
                        number_plate = random.choice(plates_from_file)["number_plate"]
                    else:
                        number_plate = random.choice(plates_random)["number_plate"]

                    log = {
                        'numberPlate': number_plate,
                        'dateTime': formatted_date[:-2],
                        'period': f'{hour}:00 - {hour+1}:00',
                        'location': random_location,
                        'speed': random.randint(0, 200),
                        'hitSuspicion': random.choice([True, False]),
                        'redlightSuspicion': random.choice([True, False]),
                        'beltStatus': random.choice([True, False]),
                        'phoneStatus': random.choice([True, False]),
                    }
                    junctions_log.append(log)

                    file_name = os.path.join(folder_name, f"junctions_log_{formatted_date}.json")
                    with open(file_name, 'w') as json_file: 
                        json.dump(junctions_log, json_file, indent=4)
            
    return junctions_log, formatted_date, folder_name


# if __name__ == "__main__":
#     all_junctions = generate_junction_logs()
