from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import send_email_with_smtp
import json
import os
import time

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from User_Service.models import Driver, Junction
from .predict_traffictime_nextday_v2 import predict_next_day_traffic
from .detection_monitor_emergency_scripts import generate_junction_logs
from .realtime_simulator import realtime_replay, read_from_file

# from .flow_visualization import visualize_flow

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        subject = json_data.get('subject')
        message = json_data.get('message')
        recipient = json_data.get('recipient')
        print(subject, message, recipient)

        send_email_with_smtp(subject, message, recipient)
            

        return JsonResponse({'message': 'Email sent successfully'})
    else:
        return JsonResponse({'message': 'Invalid request'})

@api_view(['GET'])
def send_congestion_warning(request, formatted_date, fake_city):
    if request.method == 'GET':
        try:

            folder_name = f"{formatted_date}_{fake_city}_junction_logs"

            #only send to myself
            drivers = Driver.objects.filter(driverName="Charton")
            
            subject = f"Congestion Warning on {formatted_date} of {fake_city}"

            result, conclusion = predict_next_day_traffic(folder_name)
            # image_file = visualize_flow(folder_name)
            message = f"{conclusion}\nPlease schedule your department."
            
            for driver in drivers:
                recipient = driver.driverEmail
                send_email_with_smtp(subject, message, recipient)
            return Response({'Email sent about:': message, 'Flows details:': result}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['GET'])
def send_emergency_warning(request, formatted_date, fake_city, fake_junction):
    if request.method == 'GET':
        try:

            date = formatted_date
            city = fake_city
            junction_name = fake_junction

            drivers = Driver.objects.filter(driverName="Charton")
            subject = f"Emergency Warning on {formatted_date} of {fake_city}"


            try:
                junction = Junction.objects.get(junctionName=junction_name)
                all_junctions = Junction.objects.all()
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            current_position_x = junction.latitude
            current_position_y = junction.longitude

            recommendations = []
            for entry in all_junctions:
                junction_position_x = entry.latitude
                junction_position_y = entry.longitude
                if junction.junctionID != entry.junctionID:
                    distance = ((current_position_x - junction_position_x)**2 + (current_position_y - junction_position_y)**2)**0.5
                    distance_with_units = f'{distance} km away from here'
                    recommendations.append((entry.junctionName, distance_with_units))
                recommendations.sort(key=lambda x: x[1]) 
            
            fake_script = generate_junction_logs(date, city, junction_name)

            replay_data = read_from_file(date, city, junction_name)

            for entry in replay_data:
                record = json.loads(entry)
                number_plate = record["numberPlate"]
                speed = record["speed"]
                
                message = f'{number_plate} has passed the junction at the speed {speed}'
                print(message)
                
                if speed == 200:
                    
                    emergency_event = f'On {junction_name} detected emergency events, boardcasting whole city'
                    emergency_message = f'On {junction_name} detected special vehicle {number_plate} passing, please give your way'
                    print(emergency_event)

                    for driver in drivers:
                        recipient = driver.driverEmail
                        send_email_with_smtp(subject, emergency_message, recipient)
                    
                    time.sleep(5)
                
                elif speed == 0:

                    emergency_event = f'On {junction_name} detected emergency events, boardcasting whole city'
                    emergency_message = f'On {junction_name} detected special vehicle {number_plate} stopped, please wait or consider our recommended routines {recommendations}'
                    print(emergency_event)

                    for driver in drivers:
                        recipient = driver.driverEmail
                        send_email_with_smtp(subject, emergency_message, recipient)
                    
                    time.sleep(5)

                else:
                    time.sleep(0.3)
            
            return Response({'replay success': 0}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)