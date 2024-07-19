from django.db import models

# Create your models here.
class Product(models.Model):
    P_id=models.IntegerField()
    P_name=models.CharField(max_length=20)
    Price=models.IntegerField()


class Users(models.Model):
    U_id=models.IntegerField()
    U_name=models.CharField(max_length=20)
    Email=models.EmailField()  
    Mobile=models.IntegerField()

class Orders(models.Model):
    O_id=models.IntegerField()
    P_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    U_id=models.ForeignKey(Users,on_delete=models.CASCADE)
    OrderDate=models.DateField()

class Payment(models.Model):
    Pay_id=models.IntegerField()
    O_id=models.OneToOneField(Orders,on_delete=models.CASCADE)
    Pay_status=models.CharField(max_length=20)

         

