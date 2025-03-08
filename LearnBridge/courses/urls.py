from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/create/', views.create_course, name='create_course'),
    path('course/update/<int:course_id>/', views.update_course, name='update_course'),
    path('course/delete/<int:course_id>/', views.delete_course, name='delete_course'),
]