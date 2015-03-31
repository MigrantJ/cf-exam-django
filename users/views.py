from django.shortcuts import render
from django.http import HttpResponse

from users.models import User

def index(request):
    context = {'user_list': User.objects.order_by('first_name')}
    return render(request, 'users/index.html', context)

def detail(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'users/detail.html', {'user': user})
