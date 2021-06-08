#######################################################
#
# Order.py
# Python implementation of the Class Order
# Generated by Enterprise Architect
# Created on:      20-4��-2021 13:21:58
# Original author: 70748
#
#######################################################
from .Cart import Cart
from .Promotion import Promotion
from .Customer import Customer


class Order:
    def __init__(self, customer: Customer, cart: Cart, promotion: Promotion):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def due(self):
        return self.total()-self.promotion.discount(self)

    def total(self):
        if not hasattr(self, '_total'):
            self._total = self.cart.total()
        return self._total

    def __repr__(self):
        fmt = "<Order total:{:.2f} due:{:.2f}>"
        return fmt.format(self.total(), self.due())
