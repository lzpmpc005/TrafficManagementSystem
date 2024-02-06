from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import Driver, Vehicle, Plate, JunctionsLog, Driver, ViolationLog, Violation, FineLog
from .recognition_function import PlateRecognition
from datetime import datetime
import json
from django.db import IntegrityError
import random


#this function is used to test connection
@api_view
def dash_board(request):
    return Response('ok')

@api_view(['POST'])
def register_driver(request):
    if request.method == 'POST':
        driver_data = request.data
        try:
            driver = Driver.objects.create(
                driverName=driver_data['driverName'],
                driverEmail=driver_data['driverEmail'],
                driverPhone=driver_data['driverPhone']
            )
            return Response("Driver registered successfully.", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def register_vehicle(request):
    if request.method == 'POST':
        vehicle_data = request.data
        number_plate = vehicle_data.get('numberPlate', '')
        plate_recognition = PlateRecognition()

        # Validate number plate using PlateRecognition
        if not plate_recognition._PlateRecognition__validation_number_plate(number_plate):
            return Response("Number plate format is not valid.", status=status.HTTP_400_BAD_REQUEST)
        
        # If number plate is valid, check if plate exists
            # If plate doesn't exist, create plate
        try:
            plate = Plate.objects.get(numberPlate=number_plate)
        except Plate.DoesNotExist:
            plate_info = plate_recognition.recognition_number_plate(number_plate)
            plate = Plate.objects.create(
                numberPlate=number_plate,
                region=plate_info['region'],
                postal_area=plate_info['postal_area'],
                age_identifier=plate_info['age_identifier'],
                random_letters=plate_info['random_letters']
            )
            return Response("New plate has been added to our system.", status=status.HTTP_201_CREATED)
            # If plate exist, check if the plate already has a vehicle
                # If the plate has a vehicle, validation failed, go to other process
        if hasattr(plate, 'vehicle'):
                return Response("This plate is already associated with a vehicle. Please contact us.", status=status.HTTP_400_BAD_REQUEST)
                # If the plate doesn't have a vehicle, continue
        try:
            owner_id = vehicle_data.get('ownerID', '')
            driver = Driver.objects.get(driverID=owner_id)
        except Driver.DoesNotExist:
            return Response("Driver does not exist. Please contact us.", status=status.HTTP_400_BAD_REQUEST)
            
            # If plate exist, and doesn't have a vehicle, now create vehicle
        try:
            vehicle = Vehicle.objects.create(
                numberPlate=plate,
                ownerID=driver,
                vehicleType=vehicle_data.get('vehicleType', '')
            )
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
        return Response('Vehicle registered successfully', status=status.HTTP_201_CREATED)

#out of date, need to be updated
# @api_view(['GET'])
# def process_junctions_log(request, formatted_date):
#     file_path = f"/Users/charton/Git/TrafficTest/junctions_log_{formatted_date}.json"

#     try:
#         with open(file_path, 'r') as json_file:
#             junctions_log_data = json.load(json_file)
#     except FileNotFoundError:
#         return Response(f"File '{file_path}' not found", status=404)

#     car_count_per_period = {}

#     for entry in junctions_log_data:
#         number_plate = entry['numberPlate']
#         dateTime = datetime.strptime(entry['dateTime'], "%Y-%m-%d")
#         period = entry['period']

#         try:
#             plate_instance = Plate.objects.get(numberPlate=number_plate)
#             status = 'Registered'
#         except ObjectDoesNotExist:
#             plate_instance = None
#             status = 'Unknown'

#         log_entry = JunctionsLog.objects.create(
#             numberPlate=number_plate,
#             dateTime=dateTime,
#             period=period,
#             location=entry['location'],
#             event=entry['event'],
#             status=status
#         )

#         car_count_per_period[period] = car_count_per_period.get(period, 0) + 1

#     return Response(car_count_per_period, status=200)

@api_view(['POST'])
def import_driver(request):
    if request.method == 'POST':
        try:
            file_path = '/Users/charton/Git/TrafficTest/fake_drivers_20240205_155208.json'
            with open(file_path, 'r') as json_file:
                drivers_data = json.load(json_file)

            for driver_data in drivers_data:
                driver = Driver.objects.create(
                    driverName=driver_data['driverName'],
                    driverEmail=driver_data['driverEmail'],
                    driverPhone=driver_data['driverPhone']
                )
                print(f"Driver {driver.driverName} added to the database.")

            return Response({'message': 'Drivers imported successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def import_plate(request):
    if request.method == 'POST':
        try:
            file_path = '/Users/charton/Git/TrafficTest/fake_plates_20240205_161657.json'
            with open(file_path, 'r') as json_file:
                plates_data = json.load(json_file)

            plate_recognition = PlateRecognition()

            for plate_data in plates_data:
                number_plate = plate_data['number_plate']
                
                try:
                    plate_info = plate_recognition.recognition_number_plate(number_plate)
                except ValueError as e:
                    plate_info = {
                        'region': 'Unknown',
                        'postal_area': 'Unknown',
                        'age_identifier': {'register_month': 'Unknown', 'register_year': 'Unknown'},
                        'random_letters': 'XXX'
                    }
                try:
                    plate = Plate.objects.create(
                        numberPlate=number_plate,
                        region=plate_info['region'],
                        postal_area=plate_info['postal_area'],
                        age_identifier=plate_info['age_identifier'],
                        random_letters=plate_info['random_letters']
                    )
                    print(f"Plate {plate.numberPlate} added to the database.")
                except IntegrityError:
                    print(f"Skipping insertion for duplicate primary key: {number_plate}")
                    continue

            return Response({'message': 'Plates imported successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def create_vehicles(request):
    vehicle_types = ['SUV', 'Truck', 'Sedan', 'Van', 'Motorcycle', 'Electric Car']

    json_file_path = '/Users/charton/Git/TrafficTest/fake_plates_20240205_161657.json'

    with open(json_file_path, 'r') as f:
        plate_data = json.load(f)

    try:
        for driver_id, plate_info in enumerate(plate_data, start=1):
            driver = Driver.objects.get(driverID=driver_id)

            number_plate = plate_info['number_plate']

            random_vehicle_type = random.choice(vehicle_types)

            vehicle = Vehicle.objects.create(
                numberPlate=Plate.objects.get(numberPlate=number_plate),
                ownerID=driver,
                vehicleType=random_vehicle_type
            )

            vehicle.save()

        return Response("Vehicles created successfully.", status=status.HTTP_200_OK)

    except IntegrityError:
        return Response("Integrity Error: Already created.", status=status.HTTP_409_CONFLICT)

    except ObjectDoesNotExist:
        return Response("Driver with ID does not exist.", status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def process_junctions_log(request, formatted_date):
    file_path = f"/Users/charton/Git/TrafficTest/junctions_log_{formatted_date}.json"

    try:
        with open(file_path, 'r') as json_file:
            junctions_log_data = json.load(json_file)
    except FileNotFoundError:
        return Response(f"File '{file_path}' not found", status=404)
    
    for entry in junctions_log_data:
        number_plate = entry['numberPlate']

        try:
            number_plate = Plate.objects.get(numberPlate=number_plate)
            register_status = True
        except ObjectDoesNotExist:
            number_plate = entry['numberPlate']
            register_status = False

        log_entry = JunctionsLog.objects.create(
            numberPlate=number_plate,
            dateTime=entry['dateTime'],
            period=entry['period'],
            location=entry['location'],
            speed=entry['speed'],
            hitSuspicion=entry['hitSuspicion'],
            redlightSuspicion=entry['redlightSuspicion'],
            beltStatus=entry['beltStatus'],
            phoneStatus=entry['phoneStatus'],
            registerStatus=register_status
        )

    return Response("Junction log imported successfully.", status=status.HTTP_200_OK)

@api_view(['GET'])
def process_violation_log(request, formatted_date, violation_type):
    valid_violation_types = ['hitSuspicion', 'redlightSuspicion', 'beltStatus', 'phoneStatus']
    
    if violation_type not in valid_violation_types:
        return Response(f"Violation type '{violation_type}' is not valid", status=status.HTTP_400_BAD_REQUEST)
    
    query_filter = {violation_type: True, 'dateTime': formatted_date}

    try:
        junctions_log_entries = JunctionsLog.objects.filter(**query_filter)
    except JunctionsLog.DoesNotExist:
        return Response(f"No records found for date '{formatted_date}' and violation type '{violation_type}'", status=status.HTTP_404_NOT_FOUND)
    
    for junctions_log_entry in junctions_log_entries:

        violation_instance, _ = Violation.objects.get_or_create(violationType=violation_type)

        violation_log = ViolationLog.objects.create(
            numberPlate=junctions_log_entry.numberPlate,
            dateTime=junctions_log_entry.dateTime,
            location=junctions_log_entry.location,
            violationType=violation_instance
        )
    
    return Response(f"ViolationLog created on {formatted_date} about {violation_type}", status=status.HTTP_201_CREATED)

@api_view(['GET'])
def generate_fine_log(request, formatted_date, violation_type):
    valid_violation_types = ['hitSuspicion', 'redlightSuspicion', 'beltStatus', 'phoneStatus']
    
    if violation_type not in valid_violation_types:
        return Response(f"Violation type '{violation_type}' is not valid", status=status.HTTP_400_BAD_REQUEST)
    
    try:
        violation_instance = Violation.objects.get(violationType=violation_type)
        violation_id = violation_instance.logID
    except Violation.DoesNotExist:
        return Response(f"Violation type '{violation_type}' not found", status=status.HTTP_404_NOT_FOUND)
    
    query_filter = {'dateTime': formatted_date, 'violationType_id': violation_id}

    try:
        violation_log_entries = ViolationLog.objects.filter(**query_filter)
    except ViolationLog.DoesNotExist:
        return Response(f"No records found for date '{formatted_date}' and violation type '{violation_type}'", status=status.HTTP_404_NOT_FOUND)
    
    for violation_log_entry in violation_log_entries:

        try:
            vehicle = Vehicle.objects.get(numberPlate=violation_log_entry.numberPlate)
            driver_id = vehicle.ownerID_id
        except ObjectDoesNotExist:
            driver_id = 0
        
        try:
            driver = Driver.objects.get(driverID=driver_id)
            driver_name = driver.driverName
        except ObjectDoesNotExist:
            driver_name = 'Unknown'

        try:
            violation = Violation.objects.get(violationType=violation_type)
            fine_amount = violation.fineAmount
        except Violation.DoesNotExist:
            fine_amount = 0

        fine_log = FineLog.objects.create(
            numberPlate=violation_log_entry.numberPlate,
            driverID=driver_id,
            driverName=driver_name,
            dateTime=violation_log_entry.dateTime,
            location=violation_log_entry.location,
            violationType=violation_instance,
            fineAmount=fine_amount,
            closedStatus=False
        )
    
    return Response(f"FineLogs created for date '{formatted_date}' and violation type '{violation_type}'", status=status.HTTP_201_CREATED)

