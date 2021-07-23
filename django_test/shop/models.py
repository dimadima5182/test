from django.db import models


class Order(models.Model):
    number = models.IntegerField()
    created_date = models.DateTimeField()

    def __str__(self):
        return self.number


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(decimal_places=0, max_digits=4)
    amount = models.IntegerField()

    def __str__(self):
        return self.product_name
