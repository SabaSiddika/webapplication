from django.db import models

# Create your models here.

class Employee(models.Model):
    
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    contact = models.CharField(max_length = 20)

    class Meta:

        db_table = 'employee'
