from .Order import Order
from .promo_register import regist_promo
from .promo_register import promotions

@regist_promo
def bulk_item_promo(order: Order):
    discount = 0
    for item in order.cart.items:
        if item.num > 20:
            discount += item.total()*0.1
    return discount

@regist_promo
def fidelity_promo(order: Order):
    if order.customer.fidelity >= 1000:
        return 0.05*order.total()
    else:
        return 0

@regist_promo
def large_order_promo(order: Order):
    if len(order.cart.items) >= 10:
        return order.total()*0.07
    else:
        return 0

def best_promo(order: Order):
    if len(promotions) == 0:
        return 0
    return max(promo(order) for promo in promotions)