import json
import os
import time

def read_from_file(date, city, junction_name):
    formatted_date = date
    fake_city = city
    fake_junction = junction_name

    folder_name = f"{fake_city}_{fake_junction}_{formatted_date}_logs"
    file_name = os.path.join(folder_name, f"junctions_log_{formatted_date}.json")

    realtime_flow = []

    with open(file_name, 'r') as f:
        data = json.load(f)
        for entry in data:
            number_plate = entry.get('numberPlate')
            speed = entry.get('speed')
            entry_json = json.dumps({'numberPlate': number_plate, 'speed': speed})
            realtime_flow.append(entry_json)

    return realtime_flow

def realtime_replay(date, city, junction_name):

    formatted_date = date
    fake_city = city
    fake_junction = junction_name

    folder_name = f"{fake_city}_{fake_junction}_{formatted_date}_logs"
    file_name = os.path.join(folder_name, f"junctions_log_{formatted_date}.json")

    realtime_flow = []

    with open(file_name, 'r') as f:
        data = json.load(f)
        for entry in data:
            number_plate = entry.get('numberPlate')
            speed = entry.get('speed')
            entry_json = json.dumps({'numberPlate': number_plate, 'speed': speed})
            realtime_flow.append(entry_json)

            message = f'{number_plate} has passed the junction at the speed {speed}'
            print(message)
            time.sleep(1)
    
    message = 'Junction replay accomplished'
    print (message)

if __name__ == "__main__":
    date = '2024-02-19'
    city = 'London'
    junction_name = 'London_Bridge'
    replay = realtime_replay(date, city, junction_name)
