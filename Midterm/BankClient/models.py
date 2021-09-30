from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    birthdate=models.DateField()
    mobile_number=models.CharField(max_length=25)
    class meta:
        db_table = 'client'

class Account(models.Model):
    account_number=models.AutoField(primary_key=True)
    account_type=models.CharField(max_length=25)
    balance=models.FloatField()
    class meta:
        db_table = 'account'

class owner(models.Model):
    owner_id=models.AutoField(primary_key=True)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    account=models.ForeignKey(Account,on_delete=models.CASCADE)
    class meta:
        db_table = 'owner'