import json
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

current_year = datetime.now().year
start_date = datetime(current_year, 1, 1)
end_date = datetime(current_year, 12, 31)
random_date = fake.date_time_between(start_date=start_date, end_date=end_date)

formatted_date = random_date.date().isoformat()

random_hour = random_date.time().strftime('%H:%M')

road = fake.street_name()
random_location = f"{road}, {fake.city()}"

junctions_log = []

for hour in range(24):
    start_time = random_date.replace(hour=hour, minute=0, second=0)
    end_time = start_time + timedelta(hours=1)

    log = {
        'numberPlate': fake.license_plate(),
        'dateTime': formatted_date,
        'location': random_location,
        'event': random.choice(['Null', 'Overspeed']),
        'period': f"{hour}:00 - {hour+1}:00"
    }
    junctions_log.append(log)

file_name = f"junctions_log_{formatted_date}.json"
with open(file_name, 'w') as json_file:
    json.dump(junctions_log, json_file, indent=4)

print(f"JSON data generated and saved to '{file_name}'")
