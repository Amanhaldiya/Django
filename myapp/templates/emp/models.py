from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id1=models.CharField(max_length=200)
    phone=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    working=models.BooleanField(default=False)
    department=models.CharField(max_length=100)                                                 


    def __str__(self):
        return self.name
    


class Testimonial(models.Model):
    name=models.CharField(max_length=100)
    testimonial=models.TextField()
    photo=models.ImageField(upload_to="testimonials/")
    rating=models.IntegerField(max_length=1)




    def __str__(self):
        return self.testimonial
