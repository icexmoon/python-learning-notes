from src.order_system_pkg.Customer import Customer
from src.order_system_pkg.Cart import Cart
from src.order_system_pkg.Item import Item
from src.order_system_pkg.Order import Order
from src.order_system_pkg import promotion_func
import inspect


def best_promo(order: Order):
    promotionFuncs = inspect.getmembers(promotion_func, inspect.isfunction)
    return max(promoFunc(order) for funcName, promoFunc in promotionFuncs)


BrusLee = Customer('Brus Lee', 90)
JackChen = Customer('Jack Chen', 2000)
items = [Item('apple', 5, 10), Item(
    'banana', 50, 6.7), Item('mobile', 1, 1000)]
cart1 = Cart(items)
order1 = Order(JackChen, cart1, best_promo)
print(order1)
order2 = Order(JackChen, cart1, best_promo)
print(order2)
items = [Item("item_"+str(i), 1, 1) for i in range(1, 11)]
cart2 = Cart(items)
order3 = Order(JackChen, cart2, best_promo)
print(order3)

# <Order total:1385.00 due:1315.75>
# <Order total:1385.00 due:1315.75>
# <Order total:10.00 due:9.30>
