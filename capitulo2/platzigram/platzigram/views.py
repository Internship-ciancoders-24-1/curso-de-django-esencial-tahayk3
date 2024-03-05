from django.http import HttpResponse
#utilities
from datetime import datetime
#para tener el formato json
import json 
from django.http import JsonResponse

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y -  %H:%M hrs:')
    return HttpResponse('Oh, hi! Current server time is {now}'.format(now=str(now)))

def sort_floats(request):
    numbers = request.GET.get('numbers')  
    
    numbers_list = [float(num) for num in numbers.split(',')] 
    numbers_list.sort() 
    
    data = {
        'status': 'ok',
        'numbers': numbers_list,
        'message': 'Float sorted successfully'
    }
    
    return JsonResponse(data)

def say_hi(request,name,age):
    if age < 18:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, welcome'.format(name)
    return HttpResponse(message)