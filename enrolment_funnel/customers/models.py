from django.db import models
from funnel.models import Funnel

# Create your models here.


class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    funnels = models.ManyToManyField(Funnel, related_name='customers', through='FunnelAssignment')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name
    

class FunnelAssignment(models.Model):
    funnel = models.ForeignKey(Funnel, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.funnel.title} assigned to {self.customer.name} at {self.added_at}"