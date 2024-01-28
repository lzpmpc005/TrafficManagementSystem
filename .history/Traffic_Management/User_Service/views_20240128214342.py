from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Driver, Vehicle
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
            return Response('Driver registered successfully', status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register_vehicle(request):
    if request.method == 'POST':
        vehicle_data = request.data
        number_plate = vehicle_data.get('numberPlate', '')

        # Validate number plate using PlateRecognition
        if not PlateRecognition.validation_number_plate(number_plate):
            return Response("Number plate format is not valid", status=status.HTTP_400_BAD_REQUEST)
        
        # If number plate is valid, check if plate exists
            # If plate doesn't exist, create plate
        
            # If plate exist, check if the plate already has a vehicle
                # If the plate has a vehicle, validation failed, go to other process
                # If the plate doesn't have a vehicle, continue
            
            # If plate exist, and doesn't have a vehicle, now create vehicle
