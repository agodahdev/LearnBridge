from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),  # View all courses
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),  # View course details
    path('course/<int:course_id>/review/', views.submit_review, name='submit_review'),
    path('course/create/', views.create_course, name='create_course'),  # ✅ Create a course
    path('course/update/<int:course_id>/', views.update_course, name='update_course'),  #  Update a course
    path('course/delete/<int:course_id>/', views.delete_course, name='delete_course'),  # Delete a course
    path('course/<int:course_id>/enroll/', views.enroll_course, name='enroll_course'),  # Enroll in a course
]