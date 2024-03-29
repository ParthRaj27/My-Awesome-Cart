from django.db import models

# Create your models here.

class Product(models.Model):
    product_id= models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=20000)
    pub_date = models.DateField()
    category= models.CharField(max_length=20 ,default="")
    sub_category = models.CharField(max_length=20, default="")
    price = models.IntegerField(default=0)
    MRP = models.IntegerField(default=0)
    image= models.ImageField(upload_to='shop/images' , default="")
    @property
    def discount_percentage(self):
        if self.MRP > 0 and self.price > 0:
            discount_percent = ((self.MRP - self.price) / self.MRP) * 100
            return round(discount_percent, 2)
        else:
            return 0

    def __str__(self):
        return self.product_name    

class Contact(models.Model):#alwasy capital first letter of any class
    msg_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    desc = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name
    
class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=111, default="")
    city=models.CharField(max_length=111)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
            return self.update_desc[0:7] + "..."


    
