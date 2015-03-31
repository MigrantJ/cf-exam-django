from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

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

def edit(request, user_id):
    p = get_object_or_404(User, pk=user_id)
    p.first_name = request.POST['first_name']
    p.save()
    return HttpResponseRedirect(reverse('index'))
