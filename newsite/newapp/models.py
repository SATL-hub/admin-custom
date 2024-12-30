from django.db import models

# Create your models here.
class departments(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class student_details(models.Model):
    name=models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(departments,on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return self.name