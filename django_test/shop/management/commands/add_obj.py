from django.core.management.base import BaseCommand, CommandError
from shop.models import Order, OrderItem
import random
import datetime


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        start_date = datetime.datetime.strptime('2018-04-11 09:00:00', "%Y-%m-%d %H:%M:%S")
        hours_added = datetime.timedelta(hours=1)
        try:
            num = int(input("Введите количество объектов: "))
        except:
            return print("Нужно ввести число!")
        if Order.objects.exists():
            start_date = Order.objects.latest('id').created_date + hours_added
            for el in range(1, num + 1):
                current_order = Order.objects.create(number=(Order.objects.latest('number').number + 1),
                                                     created_date=start_date)
                for item in range(1, random.randrange(1, 6, 1) + 1):
                    OrderItem.objects.create(order_id=current_order.id,
                                             product_name=f"Товар - {random.randrange(1, 101, 1)}",
                                             product_price=random.randrange(100, 10000, 1),
                                             amount=random.randrange(1, 11, 1))
                start_date = start_date + hours_added

        else:
            for el in range(1, num + 1):
                current_order = Order.objects.create(number=el,
                                                     created_date=start_date)
                for item in range(1, random.randrange(1, 6, 1) + 1):
                    OrderItem.objects.create(order_id=current_order.id,
                                             product_name=f"Товар - {random.randrange(1, 101, 1)}",
                                             product_price=random.randrange(100, 10000, 1),
                                             amount=random.randrange(1, 11, 1))
                start_date = start_date + hours_added


