from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Participant
# Create your views here.

@login_required(login_url='/register/login/')
def index(request):
    if(request.method == "POST" and request.user.is_superuser):
        if(request.POST['name'] and request.POST['institution'] and request.POST['event']):
            participant = Participant.objects.create(name=request.POST['name'], institution=request.POST['institution'], event=request.POST['event'])
            participant.save()
            participant.thomso_serial_key = 'THOMSO-2018-{}'.format(participant.id)
            participant.save()
            return HttpResponseRedirect(reverse('register:ticket', args=(participant.id,)))
        return render(request, 'register/register.html', {'error': "Please Fill All the Require Fields, Previous entry was not reccorded"})
    else:
        return render(request, 'register/register.html', {})
@login_required(login_url='/register/login/')
def ticket(request, participant_id):
    if(request.user.is_superuser):
        participant = get_object_or_404(Participant, pk=participant_id)
        return render(request, 'register/ticket.html', 
        {
            'participant': participant,
        })
    raise Http404("Page Not Found")
