
from django.shortcuts import render
from datetime import datetime

from django.contrib.auth.decorators import login_required


posts =[
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://static.vecteezy.com/system/resources/thumbnails/008/442/086/small/illustration-of-human-icon-user-symbol-icon-modern-design-on-blank-background-free-vector.jpg'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y -  %H:%M hrs:'),
        'photo':'https://media.moddb.com/images/mods/1/18/17093/portal2.png'
    },
     {
        'title': 'Otro post',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://static.vecteezy.com/system/resources/thumbnails/008/442/086/small/illustration-of-human-icon-user-symbol-icon-modern-design-on-blank-background-free-vector.jpg'
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y -  %H:%M hrs:'),
        'photo':'https://media.moddb.com/images/mods/1/18/17093/portal2.png'
    },

]

@login_required
def list_posts(request):
    return render(request, 'posts/feed.html', {'posts': posts})
