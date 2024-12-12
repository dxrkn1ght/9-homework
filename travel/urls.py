from django.urls import path
from . import views


app_name = 'travel'
urlpatterns = [
    path('list/', views.travels_list, name='list'),
    path('create/', views.travels_create, name='create'),
    path('detail/<int:detail_id>/', views.travels_detail, name='detail'),
    path('delete/<int:del_id>/', views.travels_del, name='delete'),
    path('update/<int:update_id>/', views.travels_update, name='update')
]