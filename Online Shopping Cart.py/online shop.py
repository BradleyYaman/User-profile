class CartItem:
    def __init__(self, item_name, price, quantity= 1):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
    def additem(self,count):
        self.quantity += count
        print(f"{count} more '{self.item_name}' added. Total: {self.quantity}")
            
    def removeitem(self, count):
        if count > self.quantity:
            print(f"Cannot remove {count}. Only {self.quantity} available.")
        else:
            self.quantity -= count
            print(f"{count} '{self.item_name}' removed. Remaining: {self.quantity}")

    def calculate_total(self):
        return self. price * self.quantity
    
#Creating an object
cart_item1 = CartItem("Laptop",1000,2)
cart_item1.additem(1)
cart_item1.removeitem(1)
print(f"Total Price:${cart_item1.calculate_total()}")