
from django.shortcuts import render
from datetime import datetime


posts =[
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://c0.klipartz.com/pngpicture/81/570/gratis-png-perfil-logo-iconos-de-computadora-usuario-usuario-thumbnail.png'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y -  %H:%M hrs:'),
        'photo':'https://i0.wp.com/tvaztecaguate.com/wp-content/uploads/2023/11/maxresdefault-1.jpg?fit=1280%2C720&ssl=1'
    },
     {
        'title': 'Otro post',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://c0.klipartz.com/pngpicture/81/570/gratis-png-perfil-logo-iconos-de-computadora-usuario-usuario-thumbnail.png'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y -  %H:%M hrs:'),
        'photo':'https://i0.wp.com/tvaztecaguate.com/wp-content/uploads/2023/11/maxresdefault-1.jpg?fit=1280%2C720&ssl=1'
    },

]

def list_posts(request):

    return render(request, 'feed.html', {'posts': posts})
