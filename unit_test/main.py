from abc import ABC, abstractmethod

# Принцип єдиної відповідальності (Single Responsibility Principle - SRP)
class Order:
    def __init__(self, customer):
        self.customer = customer
        self.status = "Processing"
        self.items = []

    def add_item(self, product, quantity):
        self.items.append(OrderItem(product, quantity))

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.calculate_subtotal()
        return total

# Принцип відкритості для розширення і закритості для зміни (Open-Closed Principle - OCP)
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total

class FixedDiscount(DiscountStrategy):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, total):
        return total - self.discount_amount

class PercentageDiscount(DiscountStrategy):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def apply_discount(self, total):
        return total * (1 - self.discount_percentage / 100)

# Принцип роздільного інтерфейсу (Interface Segregation Principle - ISP)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name):
        self.name = name

# Принцип інверсії залежності (Dependency Inversion Principle - DIP)
class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.product.price * self.quantity

class OrderProcessor:
    def process_order(self, order, discount_strategy):
        total = order.calculate_total()
        total_after_discount = discount_strategy.apply_discount(total)
        if total_after_discount > 100:
            order.status = "Completed"

# Використання
customer = Customer("John")
product1 = Product("Laptop", 1000)
product2 = Product("Headphones", 100)
order = Order(customer)
order.add_item(product1, 2)
order.add_item(product2, 1)

discount_strategy = FixedDiscount(50)
order_processor = OrderProcessor()
order_processor.process_order(order, discount_strategy)

print(f"Order total: ${order.calculate_total()}")
print(f"Order status: {order.status}")