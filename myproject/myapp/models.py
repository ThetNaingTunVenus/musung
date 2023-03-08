from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Buyer(models.Model):
    buyer_name = models.CharField(max_length=225)
    address = models.CharField(max_length=255)
    joined_on = models.DateTimeField(auto_now_add=True)

class StyleCode(models.Model):
    StyleCode = models.CharField(max_length=225)


class Items(models.Model):
    Item_name = models.CharField(max_length=225)

class ShiftAssign(models.Model):
    ShiftName = models.CharField(max_length=225)
    From_Time = models.CharField(max_length=225)
    End_Time = models.CharField(max_length=225)


class ProductionLine(models.Model):
    LineNo = models.CharField(max_length=225)
    ProductItem = models.ForeignKey(Items, on_delete=models.CASCADE)
    Supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    Target_Qty = models.PositiveIntegerField(default=0)
    Date = models.DateTimeField(auto_now_add=True)

class DailyReport(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    ProductionLine = models.ForeignKey(ProductionLine, on_delete=models.CASCADE)
    Buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    StyleCode = models.ForeignKey(StyleCode, on_delete=models.CASCADE)
    Items = models.ForeignKey(Items, on_delete=models.CASCADE)
    OrderQty = models.PositiveIntegerField(default=0)
    In_Put = models.PositiveIntegerField(default=0)
    Daily_Output = models.PositiveIntegerField(default=0)
    Balance_Qty = models.PositiveIntegerField(default=0)
    CMP = models.PositiveIntegerField(default=0)
    Daily_CMP_by_Style = models.PositiveIntegerField(default=0)
    Daily_CMP_by_Line = models.PositiveIntegerField(default=0)



