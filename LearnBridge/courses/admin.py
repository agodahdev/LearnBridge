from django.contrib import admin
from .models import Course, Enrollment, Review 

# Register your models here.
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Review)