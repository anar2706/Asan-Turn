from django.db import models
from django.urls import reverse
# Create your models here.


class Dated(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta: 
        abstract = True

class Service(Dated):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Operator(Dated):
    name    = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    service = models.ForeignKey(Service,on_delete=models.CASCADE,related_name='operators',default=1)
    image   = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('oper:detail',kwargs={'pk':self.pk})