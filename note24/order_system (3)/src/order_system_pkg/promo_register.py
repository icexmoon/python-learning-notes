from .Order import Order
promotions = []


def regist_promo(func):
    promotions.append(func)
    return func
