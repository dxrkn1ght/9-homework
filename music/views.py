from django.shortcuts import render, redirect, get_object_or_404
from .models import Music


def musics_list(request):
    musics = Music.objects.all
    ctx = {'musics': musics}
    return render(request, 'music-html/list.html', ctx)


def musics_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        date = request.POST.get('date')
        genre = request.POST.get('genre')
        if title and artist and date and genre:
            Music.objects.create(
                title = title,
                artist = artist,
                date = date,
                genre = genre,
            )
            return redirect('musics:list')
    return render(request, 'music-html/create.html')


def musics_detail(request, detail_id):
    music = get_object_or_404(Music, pk=detail_id)
    ctx = {'music': music}
    return render(request, 'music-html/detail.html', ctx)


def musics_del(request, del_id):
    music = get_object_or_404(Music, pk=del_id)
    music.delete()
    return redirect('musics:list')

def musics_update(request, update_id):
    music = get_object_or_404(Music, pk=update_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        date = request.POST.get('date')
        genre = request.POST.get('genre')
        if artist and date and genre:
            music.title = title
            music.artist = artist
            music.date = date
            music.genre = genre
            music.save()
            return redirect('musics:list')
    ctx = {'music': music}
    return render(request, 'music-html/create.html', ctx)



