from django.urls import path

from . import views

urlpatterns = [
    path('student/',views.Home),
    path('student/<int:id>/',views.FetchByid),
    path('emp/',views.Employees.as_view())
]