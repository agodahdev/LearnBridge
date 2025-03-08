from django.test import TestCase
from .models import Course

# Test if a course is created correctly
class CourseModelTest(TestCase):
    def test_create_course(self):
        course = Course.objects.create(
            title="Test Course",
            description="This is a test description.",
            price=100.00
        )
        self.assertEqual(course.title, "Test Course")