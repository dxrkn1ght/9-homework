from django.urls import path
from . import views


app_name = 'sports'
urlpatterns = [
    path('list/', views.sports_list, name='list'),
    path('create/', views.sports_create, name='create'),
    path('detail/<int:detail_id>/', views.sports_detail, name='detail'),
    path('delete/<int:del_id>/', views.sports_del, name='delete'),
    path('update/<int:update_id>/', views.sports_update, name='update')
]