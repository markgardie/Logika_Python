import unittest

class TestOrder(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("John")
        self.product1 = Product("Laptop", 1000)
        self.product2 = Product("Headphones", 100)
        self.order = Order(self.customer)
        self.order.add_item(self.product1, 2)
        self.order.add_item(self.product2, 1)

    def test_calculate_total(self):
        total = self.order.calculate_total()
        self.assertEqual(total, 2100)



if __name__ == "__main__":  
    unittest.main()