from django.shortcuts import render, redirect, get_object_or_404
from .models import Travel


def travels_list(request):
    travels = Travel.objects.all
    ctx = {'travels': travels}
    return render(request, 'travel-html/list.html', ctx)


def travels_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        description = request.POST.get('description')
        season = request.POST.get('season')
        if name and country and description and season:
            Travel.objects.create(
                name = name,
                country = country,
                description = description,
                season = season,
            )
            return redirect('travel:list')
    return render(request, 'travel-html/create.html')


def travels_detail(request, detail_id):
    travel = get_object_or_404(Travel, pk=detail_id)
    ctx = {'travel': travel}
    return render(request, 'travel-html/detail.html', ctx)


def travels_del(request, del_id):
    travel = get_object_or_404(Travel, pk=del_id)
    travel.delete()
    return redirect('travel:list')

def travels_update(request, update_id):
    travel = get_object_or_404(Travel, pk=update_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        description = request.POST.get('description')
        season = request.POST.get('season')
        if name and country and description and season :
            travel.name = name
            travel.country = country
            travel.description = description
            travel.season = season
            travel.save()
            return redirect('travel:list')
    ctx = {'travel': travel}
    return render(request, 'travel-html/create.html', ctx)



