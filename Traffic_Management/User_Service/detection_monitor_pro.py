import json
import random
from faker import Faker
from datetime import datetime, timedelta
from fake_plate import generate_fake_plates, read_fake_plates

fake = Faker()

def generate_junction_logs():
    current_year = datetime.now().year
    start_date = datetime(current_year, 1, 1)
    end_date = datetime(current_year, 12, 31)
    random_date = fake.date_time_between(start_date=start_date, end_date=end_date)

    formatted_date = random_date.date().isoformat()

    road = fake.street_name()
    random_location = f"{road}, {fake.city()}"

    junctions_log = []

    morning_peak_hours = [6, 7, 8, 9, 10]
    evening_peak_hours = [16, 17, 18, 19, 20]

    plates_random = generate_fake_plates()
    plates_from_file = read_fake_plates('fake_plates_20240205_161657.json')

    for hour in range(24):

        if hour in morning_peak_hours or hour in evening_peak_hours:
            number_records = random.randint(20, 30)
        else:
            number_records = random.randint(5, 10)

            for _ in range (number_records):
                if random.random() <= 0.8:
                    number_plate = random.choice(plates_from_file)['number_plate']
                else:
                    number_plate = random.choice(plates_random)['number_plate']

                log = {
                    'numberPlate': number_plate,
                    'dateTime': formatted_date,
                    'period': f"{hour}:00 - {hour+1}:00",
                    'location': random_location,
                    'speed': random.randint(0, 200),
                    'hitSuspicion': random.choice([True, False]),
                    'redlightSuspicion': random.choice([True, False]),
                    'beltStatus': random.choice([True, False]),
                    'phoneStatus': random.choice([True, False])
                }
                junctions_log.append(log)

    return junctions_log, formatted_date

def print_junction_logs(junctions_log, formatted_date):
    file_name = f"junctions_log_{formatted_date}.json"
    with open(file_name, 'w') as json_file:
        json.dump(junctions_log, json_file, indent=4)

    print(f"JSON data generated and saved to '{file_name}'")

logs, date = generate_junction_logs()

print_junction_logs(logs, date)
