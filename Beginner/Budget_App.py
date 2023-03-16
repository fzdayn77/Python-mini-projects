class Category:

    # constructor
    def __init__(self, category):
      self.category = category
      self.ledger = list()
    
    def deposit(self, amount, description=""):
      self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
      if self.check_funds(amount):
        self.ledger.append({"amount": -amount, "description": description})
        return True
      else:
        return False
    
    def get_balance(self):
      balance = 0
      for item in self.ledger:
        balance += item["amount"]
      return balance
    
    def transfer(self, amount, destination_categ):
      if self.check_funds(amount):
        self.withdraw(amount, f"Transfer to {destination_categ.category}")
        destination_categ.deposit(amount, f"Transfer from {self.category}")
        return True
      else:
        return False
    
    def check_funds(self, amount):
      return amount <= self.get_balance()

    def __str__(self):
      transactions = ''
      total = 0
      
      header = '*'*((30-len(self.category))//2) + self.category + '*'*((30-len(self.category))//2)
      for i in range(len(self.ledger)):
        decimal_number = '{0:.2f}'.format(self.ledger[i]["amount"])
        spaces = ' '*(30-len(decimal_number)-len(self.ledger[i]["description"][:23]))
        transactions += self.ledger[i]["description"][:23] + spaces + decimal_number + '\n'
        total += self.ledger[i]["amount"]
      
      return header + '\n' + transactions + f'Total: {total}'





def create_spend_chart(categories):
    
    # a list of dictionaries with the category name and the sum of corresponding withdrawals
    withdrawals = list()
    for category in categories:
        # sum of withdrawals for each category
        withdrawals_total = 0
        for transaction in category.ledger:
            if transaction["amount"] < 0:
                withdrawals_total += transaction["amount"]
        withdrawals.append({"category": category.category, "withdrawals_total": withdrawals_total})

    # calculating the percentage for each category
    withdrawals_total = sum(item["withdrawals_total"] for item in withdrawals)
    withdrawals_percentage = [(item["withdrawals_total"] / withdrawals_total) * 100 for item in withdrawals]

    output = list()
    # adding the o's for all categories
    for i in range(100, -1, -10):
        output.append(str(i).rjust(3) + "| " + "".join(["o  " if percentage >= i else "   " for percentage in withdrawals_percentage]))

    # adding dashes
    output.append("    " + "-" * (len(categories) * 3 + 1))

    # constructing the lower part with categories names
    categories_names = [category["category"] for category in withdrawals]
    max_category_length = max([len(name) for name in categories_names])
    for i in range(max_category_length):
        output.append("     " + "  ".join([name[i] if len(name) > i else " " for name in categories_names]) + "  ")
    
    
    return "Percentage spent by category\n" + "\n".join(output)

