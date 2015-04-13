from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from users.models import User


def index(request):
    context = {'user_list': User.objects.order_by('first_name'),
               'sub_template': 'users/index.html'}
    return render(request, 'users/base.html', context)


def detail(request, user_id=None):
    context = {'user': get_object_or_404(User, pk=user_id),
               'sub_template': 'users/detail.html'}

    return render(request, 'users/base.html', context)


def add(request):
    user = {
        'id': 0,
        'first_name': '',
        'last_name': '',
        'email': ''
    }
    context = {
        'user': user,
        'sub_template': 'users/detail.html'
    }

    return render(request, 'users/base.html', context)


def edit(request, user_id):
    if user_id != '0':
        u = get_object_or_404(User, pk=user_id)
    else:
        # user id of 0 means add a new user
        u = User()

    u.first_name = request.POST['first_name']
    u.last_name = request.POST['last_name']
    u.email = request.POST['email']

    u.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, user_id):
    u = get_object_or_404(User, pk=user_id)
    u.delete()
    return HttpResponseRedirect(reverse('index'))