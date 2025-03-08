from django.contrib import admin
from .models import Course, Enrollment #Import Enrollment model

# Register your models here.
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Review)