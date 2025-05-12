class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount_percent):
        if 0 < discount_percent < 100:
            discount_amount = self.price * (discount_percent / 100)
            self.price -= discount_amount
            print(f"Discount of {discount_percent}% applied. New price: ₹{self.price}")
        else:
            print("Invalid discount percentage. Must be between 0 and 100.")

book1 = Book("The Alchemist", "Paulo Coelho", 500)

print(f"Original Price: ₹{book1.price}")
book1.apply_discount(20)  # Apply 20% discount
