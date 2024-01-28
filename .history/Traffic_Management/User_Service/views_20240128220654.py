from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Driver, Vehicle, Plate, JunctionsLog
from .recognition_function import PlateRecognition



#this function is used to test
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
        if not plate_recognition.validation_number_plate(number_plate):
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
        if plate.vehicle_set.exists():
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
                numberPlate=number_plate,
                ownerID=driver,
                vehicleType=vehicle_data.get('vehicleType', '')
            )
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        
        return Response('Vehicle registered successfully', status=status.HTTP_201_CREATED)
