from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import send_email_with_smtp
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from User_Service.models import Driver
from User_Service.predict_traffictime_nextday_v2 import predict_next_day_traffic

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
            message = conclusion
            
            for driver in drivers:
                recipient = driver.driverEmail
                send_email_with_smtp(subject, message, recipient)
            return Response({'Email sent about:': message, 'Flows details:': result}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)