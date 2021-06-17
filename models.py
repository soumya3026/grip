from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    current_balance=models.IntegerField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    sender=models.CharField(max_length=50)
    receiver=models.CharField(max_length=50)
    transfer=models.IntegerField()

    def __str__(self):
        return self.sender+" to "+self.receiver