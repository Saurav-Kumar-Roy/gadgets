#from index.views import confirm
from django.db import models
#from django.db.models.expressions import Combinable
# Create your models here.
 
class Products(models.Model):
    code = models.IntegerField()
    name = models.TextField()
    image = models.ImageField(upload_to='pics')
    ammount = models.IntegerField()
    short_dis = models.TextField()
    details = models.TextField()

class Order(models.Model):
    item_name = models.TextField()
    item_price = models.IntegerField()
    email = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    payment_method = models.TextField()
    transcetion_no = models.IntegerField()
    account = models.IntegerField()
    delevary_address = models.TextField()
    confirm = models.BooleanField(default=False)  
    delevered = models.BooleanField(default=False)  