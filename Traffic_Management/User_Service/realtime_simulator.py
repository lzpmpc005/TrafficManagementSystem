import json
import os
import time

def realtime_replay(folder_name):
    folder_path = f'/Users/charton/Git/TrafficManagementSystem/{folder_name}'
    realtime_flow = []

    for street in range(1):
        with open(os.path.join(folder_path, f'junctions_log_2024-02-01_{street+1}.json'), 'r') as f:
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
    folder_name = "2024-02-06_London_junction_logs"
    function = realtime_replay(folder_name)
    # print(flow)
