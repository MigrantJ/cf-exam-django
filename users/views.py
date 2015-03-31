from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from users.models import User

def index(request):
    context = {'user_list': User.objects.order_by('first_name')}
    return render(request, 'users/index.html', context)

def detail(request, user_id=None):
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")

    return render(request, 'users/detail.html', {'user': user})

def add(request):
    user = {
        'id': 0,
        'first_name': '',
        'last_name': '',
        'email': ''
    }

    return render(request, 'users/detail.html', {'user': user})

def edit(request, user_id):
    if user_id != '0':
        p = get_object_or_404(User, pk=user_id)
    else:
        # user id of 0 means add a new user
        p = User()

    p.first_name = request.POST['first_name']
    p.last_name = request.POST['last_name']
    p.email = request.POST['email']

    p.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request):
    return HttpResponseRedirect(reverse('index'))