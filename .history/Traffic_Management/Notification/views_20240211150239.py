from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import send_email_with_smtp
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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

