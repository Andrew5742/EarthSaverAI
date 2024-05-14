from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about),
    path('plot', views.plot_predicted_data, name = 'plot_predicted_data')

]