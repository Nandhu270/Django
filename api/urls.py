from django.urls import path

from . import views

urlpatterns = [
    path('student/',views.Home),
    path('student/<int:id>/',views.FetchByid),
    path('emp/',views.Employees.as_view()),
    path('emp/<int:id>',views.EmployeeId.as_view()),
    path('emp1/',views.Empl.as_view()),
    path('emp1/<int:pk>',views.EmplID.as_view()),
]