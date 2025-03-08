from django import forms
from .models import Course, Review

# Form for course creation and updates
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price']

# Form for submitting course reviews
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']