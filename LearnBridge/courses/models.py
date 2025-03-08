from django.db import models
from django.contrib.auth.models import User  # Import Django's built-in User model

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=255)  # Stores the course title
    description = models.TextField()  # Detailed course description
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)  # Course price, optional
    date_created = models.DateTimeField(auto_now_add=True)  # Auto-set timestamp when course is created

    def __str__(self):
        return self.title  # Returns the course title when referenced

# Enrollment Model
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User (who enrolled)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Link to Course (enrolled in)
    enrolled_at = models.DateTimeField(auto_now_add=True)  # Timestamp when enrolled

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.title}"  # Displays enrollment info

# Review Model
class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # The course being reviewed
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who wrote the review
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Rating between 1 and 5 stars
    comment = models.TextField()  # Review comment text
    date_posted = models.DateTimeField(auto_now_add=True)  # Auto-set timestamp for review

    def __str__(self):
        return f"{self.user.username} - {self.course.title} ({self.rating} stars)"  # Displays review info