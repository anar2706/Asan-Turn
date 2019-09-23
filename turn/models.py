from django.db import models
from django.urls import reverse
from operators.models import Service,Dated,Operator
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
# Create your models here.

STATE_CHOICES = (
    (1,'Waiting'),
    (2,'Working'),
    (3,'Endup')
)


class Order(Dated):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    service = models.ForeignKey(Service,on_delete=models.DO_NOTHING,related_name='turn',default=1)
    operator = models.ForeignKey(Operator,on_delete=models.DO_NOTHING,related_name='turn',null=True,blank=True)
    code = models.CharField(max_length=40,null=True,blank=True)
    state = models.IntegerField(choices=STATE_CHOICES,default=1)

  
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('turn:detail',kwargs={'pk':self.pk})


    class Meta:
        ordering = ['created']


@receiver(post_save, sender=Order)
def save_profile(sender, instance, **kwargs):
    instance.code = f'{instance.service.name[0].upper()}00{str(instance.id)}'

