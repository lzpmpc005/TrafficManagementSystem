import random
import string
from datetime import datetime
import json

def generate_fake_plates():
    plates = []

    for i in range(500):
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=2))
        random_letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        number_plate = f"{letters}{numbers}{random_letters}"
        plates.append({"number_plate": number_plate})

    return plates

def save_fake_plates(plates):
    file_name = f"fake_plates_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(file_name, 'w') as json_file:
        json.dump(plates, json_file, indent=4)

    print(f"Fake number plates saved to {file_name}")

def read_fake_plates(file_name):
    with open(file_name, 'r') as json_file:
        plate_data = json.load(json_file)
    return plate_data