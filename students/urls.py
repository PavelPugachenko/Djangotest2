from django.urls import path
from students import views

app_name = 'students'

urlpatterns = [
    path('about/', views.about, name='about'),
]