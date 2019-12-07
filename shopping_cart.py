class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        
    def add_item(self, name, price, quantity=1):
        self.total += price * quantity
        for i in range(0, quantity): self.items.append({ 'name': name , 'price': price })

        return self.total

    def mean_item_price(self):
        total_dollars = 0
        total_quantity = len(self.items)
        
        if total_quantity == 0: return 0
        
        for i in self.items:
            total_dollars += i['price'] 
            
        return total_dollars / total_quantity    

    def median_item_price(self):
        num_items = len(self.items)
        if num_items == 0: return 0

        sorted_items = sorted(self.items, key=lambda i: i['price'])
        
        if num_items%2 == 1: return sorted_items[num_items//2]['price']
        else: return (sorted_items[num_items//2]['price'] + sorted_items[num_items//2 - 1]['price']) / 2

    def apply_discount(self):
        if not self.employee_discount: return 'Sorry, there is no discount to apply to your cart :('
        else: return self.total * (100 - self.employee_discount) / 100

    def void_last_item(self):
        if len(self.items) == 0: return 'There are no items in your cart!'
        
        i = self.items.pop()
        self.total -= i['price']