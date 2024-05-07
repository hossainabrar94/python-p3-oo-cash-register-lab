#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0, items=None):
        self.discount = discount
        self.total = total
        if items is None:
            self.items = []
        else:
            self.items = items

    def add_item(self, item, item_price, quantity=1):
        for _ in range(quantity):
          self.items.append(item)
        self.total += item_price * quantity

    def apply_discount(self):
        if self.total != 0:
            self.total = self.total - int(self.total * .2)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        pass
