class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name: str, price: float, qty: int = 1):
        if name in self.items:
            self.items[name]['qty'] += qty
        else:
            self.items[name] = {'price': price, 'qty': qty}

    def remove_item(self, name: str):
        if name in self.items:
            del self.items[name]

    def total(self) -> float:
        return sum(item['price'] * item['qty'] for item in self.items.values())

    def apply_discount(self, percent: float) -> float:
        if not (0 <= percent <= 100):
            raise ValueError("Discount must be between 0 and 100")
        current_total = self.total()
        discount_amount = current_total * (percent / 100.0)
        return current_total - discount_amount

    def apply_coupon(self, code: str) -> float:
        raise NotImplementedError("Coupon feature not implemented yet")
