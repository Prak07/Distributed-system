import threading
import time
from django.core.management.base import BaseCommand
from database_simulation.models import User, Product, Order

# Separate thread class for inserting users
class Users(threading.Thread):
    def run(self):
        users = [
            (1, "Alice", "alice@example.com"),
            (2, "Bob", "bob@example.com"),
            (3, "Charlie", "charlie@example.com"),
            (4, "David", "david@example.com"),
            (5, "Eve", "eve@example.com"),
            (6, "Frank", "frank@example.com"),
            (7, "Grace", "grace@example.com"),
            (8, "Alice", "alice@example.com"),
            (9, "Henry", "henry@example.com"),
            (10, "Jane", "jane@example.com"),
        ]
        for user in users:
            User.objects.using('users').create(id=user[0], name=user[1], email=user[2])
            print(f"Inserted User: {user[1]} with Email: {user[2]}")
            time.sleep(1)  # simulate a delay


# Separate thread class for inserting products
class Products(threading.Thread):
    def run(self):
        products = [
            (1, "Laptop", 1000.00),
            (2, "Smartphone", 700.00),
            (3, "Headphones", 150.00),
            (4, "Monitor", 300.00),
            (5, "Keyboard", 50.00),
            (6, "Mouse", 30.00),
            (7, "Laptop", 1000.00),
            (8, "Smartwatch", 250.00),
            (9, "Gaming Chair", 500.00),
            (10, "Earbuds", -50.00),
        ]
        for product in products:
            Product.objects.using('products').create(id=product[0], name=product[1], price=product[2])
            print(f"Inserted Product: {product[1]} with Price: {product[2]}")
            time.sleep(1)  # simulate a delay


# Separate thread class for inserting orders
class Orders(threading.Thread):
    def run(self):
        orders = [
            (1, 1, 1, 2),
            (2, 2, 2, 1),
            (3, 3, 3, 5),
            (4, 4, 4, 1),
            (5, 5, 5, 3),
            (6, 6, 6, 4),
            (7, 7, 7, 2),
            (8, 8, 8, 0),
            (9, 9, 1, -1),
            (10, 10, 11, 2),
        ]
        for order in orders:
            Order.objects.using('orders').create(
                id=order[0],
                user_id=order[1],
                product_id=order[2],
                quantity=order[3],
            )
            print(f"Inserted Order: {order[0]} with User ID: {order[1]} and Product ID: {order[2]}")
            time.sleep(1)  # simulate a delay


class Command(BaseCommand):
    help = 'Insert data into the databases'

    def handle(self, *args, **kwargs):
        # Create thread instances for each class
        users_thread = Users()
        products_thread = Products()
        orders_thread = Orders()

        # Start threads
        users_thread.start()
        products_thread.start()
        orders_thread.start()

        # Join threads to ensure all threads complete before proceeding
        users_thread.join()
        products_thread.join()
        orders_thread.join()

        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))
