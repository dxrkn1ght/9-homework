from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie


def home(request):
    return render(request, 'index.html')


def movies_list(request):
    movies = Movie.objects.all
    ctx = {'movies': movies}
    return render(request, 'movie-html/list.html', ctx)


def movies_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        if title and director and year and genre:
            Movie.objects.create(
                title = title,
                director = director,
                year = year,
                genre = genre,
            )
            return redirect('movies:list')
    return render(request, 'movie-html/create.html')


def movies_detail(request, detail_id):
    movie = get_object_or_404(Movie, pk=detail_id)
    ctx = {'movie': movie}
    return render(request, 'movie-html/detail.html', ctx)


def movies_del(request, del_id):
    movie = get_object_or_404(Movie, pk=del_id)
    movie.delete()
    return redirect('movies:list')

def movies_update(request, update_id):
    movie = get_object_or_404(Movie, pk=update_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        director = request.POST.get('director')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        if title and director and year and genre:
            movie.title = title
            movie.director = director
            movie.year = year
            movie.genre = genre
            movie.save()
            return redirect('movies:list')
    ctx = {'movie': movie}
    return render(request, 'movie-html/create.html', ctx)



