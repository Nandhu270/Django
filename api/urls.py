from django.urls import path,include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('emp1',views.ViewEmployee,basename='employee')

urlpatterns = [
    path('student/',views.Home),
    path('student/<int:id>/',views.FetchByid),
    path('emp/',views.Employees.as_view()),
    path('emp/<int:id>/',views.EmployeeId.as_view()),
    # path('emp1/',views.Empl.as_view()),
    # path('emp1/<int:pk>',views.EmplID.as_view()),

    path('',include(router.urls)),

    path('blogs/',views.ViewBlog.as_view()),
    path('comment/',views.ViewComment.as_view()),

    path('blogs/<int:pk>/',views.ViewDetailBlog.as_view()),
    path('comment/<int:pk>/',views.ViewDetailComment.as_view()),

]