from src.order_system_pkg.Customer import Customer
from src.order_system_pkg.Cart import Cart
from src.order_system_pkg.Item import Item
from src.order_system_pkg.Order import Order
from src.order_system_pkg.BulkitemPromo import BulkitemPromo
from src.order_system_pkg.FidelityPromo import FidelityPromo
from src.order_system_pkg.LargeOrderPromo import LargeOrderPromo
BrusLee = Customer('Brus Lee', 90)
JackChen = Customer('Jack Chen', 2000)
items = [Item('apple', 5, 10), Item('banana', 50, 6.7), Item('mobile', 1, 1000)]
cart1 = Cart(items)
bulkItemPromo = BulkitemPromo()
fidelityPromo = FidelityPromo()
largeOrderPromo = LargeOrderPromo()
order1 = Order(JackChen, cart1, bulkItemPromo)
print(order1)
order2 = Order(JackChen, cart1, fidelityPromo)
print(order2)
items = [Item("item_"+str(i), 1, 1) for i in range(1,11)]
cart2 = Cart(items)
order3 = Order(JackChen, cart2, largeOrderPromo)
print(order3)
