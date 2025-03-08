from django.shortcuts import get_object_or_404
from .models import Enrollment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Allows logged-in users to enroll in a course
@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.create(user=request.user, course=course)
    messages.success(request, f"You have enrolled in {course.title}!")
    return redirect("course_list")

# View for showing detailed course info
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, "courses/course_detail.html", {"course": course})