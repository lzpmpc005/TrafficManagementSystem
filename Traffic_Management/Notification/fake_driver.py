import json
from faker import Faker
from datetime import datetime
import random


fake = Faker()

fake_drivers = []

for _ in range(500):
    fake_driver = {
        "driverName": fake.name(),
        "driverEmail": fake.email(),
        "driverPhone": random.randint(1000000000, 9999999999)
    }
    fake_drivers.append(fake_driver)

file_name = f"fake_drivers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
with open(file_name, 'w') as json_file:
    json.dump(fake_drivers, json_file, indent=4)

print(f"Fake driver data for 500 drivers saved to {file_name}")