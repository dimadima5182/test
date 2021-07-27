from django.core.management.base import BaseCommand, CommandError
from shop.models import Order, OrderItem
import random
import datetime


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        try:
            num = int(input("Введите количество объектов: "))
        except:
            return print("Нужно ввести число!")
        for el in range(1, num + 1):
            if el < 16:
                date = f'2018-04-11 {el + 8}:00'
            else:
                date = f'2018-04-{11 + ((el + 8) // 24)} {((el + 8) % 24)}:00'
                pass
            current_order = Order.objects.create(number=el,
                                                 created_date=date)
            for item in range(1, random.randrange(1, 6, 1) + 1):
                OrderItem.objects.create(order_id=current_order.id,
                                         product_name=f"Товар - {random.randrange(1,101, 1)}",
                                         product_price=random.randrange(100, 10000, 1),
                                         amount=random.randrange(1, 11, 1))
                pass


