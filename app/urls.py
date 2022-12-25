from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/sv<int:value>', views.sv, name='sv')
]