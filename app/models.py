from django.db import models
from datetime import datetime
import re

class CourseManager(models.Manager):

    def basic_validator(self, postData):
        errors = {}
        today=datetime.now().strftime('%Y-%m-%d')

        if Course.objects.filter(name=postData['name']):
            errors['name'] = "This show already exists"
        if len(postData['name']) < 5:
            errors['name'] = "Name must have at least 5 characters"
        if postData['date'] == '':
            errors['date'] = "Date is required"
        if postData['date'] > today:
            errors['date'] = "Date is not valid"
        if len(postData['desc']) > 0 and len(postData['desc'])< 15:
            errors['desc'] = "Description must have at least 10 characters"

        return errors

class Course(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(null=True, blank=True)
    desc = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()