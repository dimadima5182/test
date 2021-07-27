from django.db import models


class Order(models.Model):
    number = models.IntegerField()
    created_date = models.DateTimeField()

    def __str__(self):
        return self.number

    def get_total_sum(self):
        order_items = self.order_related.filter(order_id=self.id)
        total_sum = 0
        for el in order_items:
            total_sum += el.product_price * el.amount
        return total_sum

    def get_items(self):
        items_list = []
        for el in self.order_related.filter(order_id=self.id):
            items_list.append(f"{el.product_name} x {el.amount}")
        return items_list


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_related')
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(decimal_places=0, max_digits=4)
    amount = models.IntegerField()

    def __str__(self):
        return self.product_name
