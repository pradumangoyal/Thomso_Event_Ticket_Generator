from django.urls import path, include

from . import views

app_name = 'register'
urlpatterns = [
    path('/', views.index, name='index'),
    path('/<int:participant_id>/', views.ticket, name='ticket'),
    path('/', include('django.contrib.auth.urls')),
]
