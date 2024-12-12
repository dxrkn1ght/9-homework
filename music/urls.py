from django.urls import path
from . import views


app_name = 'musics'
urlpatterns = [
    path('list/', views.musics_list, name='list'),
    path('create/', views.musics_create, name='create'),
    path('detail/<int:detail_id>/', views.musics_detail, name='detail'),
    path('delete/<int:del_id>/', views.musics_del, name='delete'),
    path('update/<int:update_id>/', views.musics_update, name='update')
]