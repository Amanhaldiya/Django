from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home1),
    path('home1/',views.index,name='index'),
    path('buy/<int:pk>/',views.buy,name='buy'),
    path('pdf/',views.pdf,name='pdf'),
]