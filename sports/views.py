from django.shortcuts import render, redirect, get_object_or_404
from .models import Sport


def sports_list(request):
    sports = Sport.objects.all
    ctx = {'sports': sports}
    return render(request, 'sport-html/list.html', ctx)


def sports_create(request):
    if request.method == 'POST':
        event = request.POST.get('event')
        location = request.POST.get('location')
        date = request.POST.get('date')
        type = request.POST.get('type')
        if location and date and type and event:
            Sport.objects.create(
                event = event,
                location = location,
                date = date,
                type = type,
            )
            return redirect('sports:list')
    return render(request, 'sport-html/create.html')


def sports_detail(request, detail_id):
    sport = get_object_or_404(Sport, pk=detail_id)
    ctx = {'sport': sport}
    return render(request, 'sport-html/detail.html', ctx)


def sports_del(request, del_id):
    sport = get_object_or_404(Sport, pk=del_id)
    sport.delete()
    return redirect('sports:list')

def sports_update(request, update_id):
    sport = get_object_or_404(Sport, pk=update_id)
    if request.method == 'POST':
        event = request.POST.get('event')
        location = request.POST.get('location')
        date = request.POST.get('date')
        type = request.POST.get('type')
        if location and date and type and event:
            sport.event = event
            sport.location = location
            sport.date = date
            sport.type = type
            sport.save()
            return redirect('sports:list')
    ctx = {'sport': sport}
    return render(request, 'sport-html/create.html', ctx)



