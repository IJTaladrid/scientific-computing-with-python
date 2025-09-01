class Category:
    def __init__(self, name):
        """Initializes a Category object with a name and an empty ledger."""
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Adds a deposit to the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        Adds a withdrawal to the ledger if sufficient funds are available.
        Returns True on success, False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Calculates and returns the current balance of the category."""
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance

    def transfer(self, amount, category):
        """
        Transfers an amount to another category if sufficient funds are available.
        Adds a withdrawal to the source and a deposit to the destination.
        Returns True on success, False otherwise.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """
        Checks if the amount is less than or equal to the current balance.
        """
        return amount <= self.get_balance()

    def __str__(self):
        """
        Formats the budget category object for printing, displaying the title,
        ledger items, and total balance.
        """
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            # Format description and amount
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            items += f"{description}{amount}\n"
            total += item["amount"]

        total_line = f"Total: {total:.2f}"
        return title + items + total_line


def create_spend_chart(categories):
    """
    Creates a bar chart showing the percentage of spending by category.
    """
    chart_title = "Percentage spent by category"
    spent_amounts = []

    # Get total spent (withdrawals only) in each category
    for category in categories:
        spent = sum(item["amount"] for item in category.ledger if item["amount"] < 0)
        spent_amounts.append(abs(spent))

    # Calculate percentage rounded down to the nearest 10
    total_spent = sum(spent_amounts)
    spent_percentage = [
        int(amount / total_spent * 10) * 10 if total_spent > 0 else 0 
        for amount in spent_amounts
    ]

    # Build the chart strings
    chart = ""
    for value in range(100, -1, -10):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"  # Note the extra space for correct alignment

    # Build the horizontal line
    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"

    # Build the vertical category names
    descriptions = [category.name for category in categories]
    max_length = max(len(desc) for desc in descriptions) if descriptions else 0
    descriptions = [desc.ljust(max_length) for desc in descriptions]

    for x in zip(*descriptions):
        footer += "    " + "".join(f" {s} " for s in x) + " \n"

    return (chart_title + "\n" + chart + footer).rstrip("\n")

food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing.deposit(100, "initial deposit")
clothing.withdraw(50, "new jacket")
auto.deposit(200, "initial deposit")
auto.withdraw(75, "gas")
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing, auto]))