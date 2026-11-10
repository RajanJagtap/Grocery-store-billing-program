class GroceryStore:
    def __init__(self) -> None:
        self.products = {
            "Fruit": (
                ("Apple 1kg", 180),
                ("Banana 1 dozen", 60),
                ("Mango 1kg", 150),
            ),
            "Vegetable": (
                ("Potato 1kg", 30),
                ("Tomato 1kg", 40),
                ("Onion 1kg", 35),
            ),
            "Biscuit": (
                ("Parle-G Biscuits", 10),
                ("Oreo Biscuits", 40),
                ("Good Day Biscuits", 30),
            ),
            "Drink": (
                ("Coca-Cola 2L", 95),
                ("Pepsi 2L", 90),
                ("Tropicana Juice 1L", 120),
            ),
            "Pulse": (
                ("Toor Dal 1kg", 160),
                ("Moong Dal 1kg", 130),
                ("Chana Dal 1kg", 110),
            ),
            "Oil": (
                ("Sunflower Oil 1L", 140),
                ("Groundnut Oil 1L", 180),
                ("Mustard Oil 1L", 170),
            ),
        }

    def get_number(self, number):
        try:
            return int(input(number))
        except ValueError:
            print("Please enter a valid number.")
            return None

    def print_bill(
        self, cart: list[tuple[str, tuple[str, int], int]]
    ) -> None:
        total = sum(product[1] * quantity for _, product, quantity in cart)
        print("\n" + "=" * 50)
        print("          RAJAN'S GROCERY STORE")
        print("                 CUSTOMER BILL")
        print("=" * 50)
        for category, (name, price), quantity in cart:
            print(f"Product Category : {category}")
            print(f"Product Name     : {name}")
            print(f"Price            : Rs. {price:,}")
            print(f"Quantity         : {quantity}")
            print(f"Item Total       : Rs. {price * quantity:,}")
            print("-" * 50)
        print(f"TOTAL AMOUNT     : Rs. {total:,}")
        print("=" * 50)
        print("\nThank you for shopping with us!")
        print("Please visit Rajan's Grocery Store again!")
        print("=" * 50)

    def run(self) -> None:
        print("=" * 50)
        print("   WELCOME TO RAJAN'S GROCERY STORE")
        print("=" * 50)
        print("We are happy to have you here!\n")
        categories = tuple(self.products)
        cart: list[tuple[str, tuple[str, int], int]] = []

        while True:
            print("What would you like to purchase?\n")
            for number, category in enumerate(categories, start=1):
                print(f"{number}. {category}")

            category_choice = self.get_number(
                f"\nEnter your choice (1-{len(categories)}): "
            )
            if category_choice is None or not 1 <= category_choice <= len(categories):
                print("Invalid category choice!")
                return

            category = categories[category_choice - 1]
            category_products = self.products[category]

            print("\n" + "=" * 50)
            print(f"Available {category}s:")
            print("=" * 50)
            for number, (name, price) in enumerate(category_products, start=1):
                print(f"{number}. {name} - Rs. {price:,}")

            product_choice = self.get_number(
                "\nEnter the product number you want to purchase: "
            )
            if (
                product_choice is None
                or not 1 <= product_choice <= len(category_products)
            ):
                print("Invalid product choice!")
                return

            quantity = self.get_number("Enter quantity: ")
            if quantity is None or quantity <= 0:
                print("Quantity must be a positive number.")
                return

            product = category_products[product_choice - 1]
            cart.append((category, product, quantity))

            while True:
                answer = input(
                    "Would you like to buy another product? (yes/no): "
                ).strip().lower()
                if answer in ("yes", "y"):
                    break
                if answer in ("no", "n"):
                    self.print_bill(cart)
                    return
                print("Please answer yes or no.")


if __name__ == "__main__":
    GroceryStore().run()
