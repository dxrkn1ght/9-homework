from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('list/', views.movies_list, name='list'),
    path('create/', views.movies_create, name='create'),
    path('detail/<int:detail_id>/', views.movies_detail, name='detail'),
    path('delete/<int:del_id>/', views.movies_del, name='delete'),
    path('update/<int:update_id>/', views.movies_update, name='update'),

]