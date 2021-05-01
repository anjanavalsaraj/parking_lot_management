from django.db import models
# Create your models here.
import random
import string



def key_generator():
    key = ''.join(random.choice(string.digits) for x in range(6))
    if CustomerData.objects.filter(code=key).exists():
        key = key_generator()
    return key


class CustomerData(models.Model):
    customer = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True, blank=True)
    code = models.CharField(max_length=6, default=key_generator, unique=True, editable=False)
    vehicle_number = models.CharField(max_length=100,null=True, blank=True)
    entry_time = models.DateTimeField(null=True, blank=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.customer.email
