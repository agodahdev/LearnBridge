from django.test import TestCase
from django.contrib.auth.models import User

# Test if a user can register
class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username="testuser", password="testpass123")
        self.assertEqual(user.username, "testuser")
