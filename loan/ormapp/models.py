from django.db import models
from django.contrib import admin
class loan_db(models.Model):
    customer_id=models.CharField(max_length=20)
    customer_name=models.CharField(max_length=100)
    amount=models.IntegerField()
    acc_no=models.IntegerField()
    email=models.EmailField()

class loan_dbAdmin(admin.ModelAdmin):
    list_display=('customer_id','customer_name','amount','acc_no','email')    
# Create your models here.
