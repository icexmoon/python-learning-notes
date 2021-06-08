from .Order import Order


def bulk_item_promo(order: Order):
    discount = 0
    for item in order.cart.items:
        if item.num > 20:
            discount += item.total()*0.1
    return discount


def fidelity_promo(order: Order):
    if order.customer.fidelity >= 1000:
        return 0.05*order.total()
    else:
        return 0


def large_order_promo(order: Order):
    if len(order.cart.items) >= 10:
        return order.total()*0.07
    else:
        return 0


# def best_promo(order: Order):
#     functions = globals()
#     promotionFuncs = []
#     for funcName,function in functions.items():
#         if funcName.endswith('_promo') and funcName!='best_promo' and callable(function):
#             promotionFuncs.append(function)
#     return max(promoFunc(order) for promoFunc in promotionFuncs)