from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Enrollment, Review
from .forms import CourseForm, ReviewForm

# View to display all courses
def course_list(request):
    courses = Course.objects.all()  # Fetch all courses from database
    return render(request, 'courses/course_list.html', {'courses': courses})

# View to display course details
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)  # Fetch course by ID
    reviews = Review.objects.filter(course=course)  # Get all reviews for this course
    return render(request, 'courses/course_detail.html', {'course': course, 'reviews': reviews})

# View to enroll a user in a course
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    Enrollment.objects.get_or_create(user=request.user, course=course)  # Enroll user if not already enrolled
    return render(request, 'courses/enrollment_success.html', {'course': course})

# View to submit a course review
@login_required
def submit_review(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.course = course
            review.user = request.user
            review.save()
            return redirect('course_detail', course_id=course.id)
    else:
        form = ReviewForm()
    return render(request, 'courses/submit_review.html', {'form': form, 'course': course})