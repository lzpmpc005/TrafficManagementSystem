import json
import random
from faker import Faker
from datetime import datetime, timedelta
from fake_plate import generate_fake_plates, save_fake_plates, read_fake_plates


fake = Faker()

fake_street_names = [
    # "Baker Street",
    # "King's Cross",
    # "Euston",
    "Farringdon",
    "Vauxhall",
    "Green_Park",
    "London_Bridge",
    "Tottenham_Court_Road",
]

fake_cities = [
    "London",
]

def generate_junction_logs():
    current_year = datetime.now().year

    all_days = []

    for j in range(5):
        for street in fake_street_names:
            file_date = f'2024-02-0{j+1}_{street}'
            formatted_date = f'2024-02-0{j+1}'

            random_location = f"{street}, {random.choice(fake_cities)}"

            junctions_log = []

            morning_peak_hours = [6, 7, 8, 9, 10]
            evening_peak_hours = [16, 17, 18, 19, 20]

            plates_random = generate_fake_plates()
            plates_from_file = read_fake_plates("fake_plates_20240217_132316.json")

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
                            "numberPlate": number_plate,
                            "dateTime": formatted_date,
                            "period": f"{hour}:00 - {hour+1}:00",
                            "location": random_location,
                            "speed": random.randint(0, 200),
                            "hitSuspicion": random.choice([True, False]),
                            "redlightSuspicion": random.choice([True, False]),
                            "beltStatus": random.choice([True, False]),
                            "phoneStatus": random.choice([True, False]),
                        }
                        
                        junctions_log.append(log)
                        file_name = f"junctions_log_{file_date}.json"
                        with open(file_name, "w") as json_file:
                            json.dump(junctions_log, json_file)



if __name__ == "__main__":
    all_junctions = generate_junction_logs()

