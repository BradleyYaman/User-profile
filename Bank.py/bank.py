class BankAccount:
    
    def __init__(self, account_name, account_number, balance, pin):
        self.account_name = account_name  
        self.account_number = account_number  
        self._balance = balance  
        self.__pin = pin  
        
    def get_balance(self):
        """Returns the account balance"""
        return self._balance  

    def set_balance(self, amount):
        """Updates the account balance if the amount is valid"""
        if amount > 0:
            self._balance = amount
        else:
            print("Balance must be a positive value.")

    def verify_pin(self, pin):
        """Verifies the PIN"""
        return pin == self.__pin

# Creating an instance of BankAccount
account = BankAccount("Bradley Yaman", "12345678", 1000, "22569984")

# Accessing public attributes
print("Account Name:", account.account_name)
print("Account Number:", account.account_number)

# Accessing the protected attribute (allowed but not recommended)
print("Balance (protected access):", account._balance)

# Attempting to access the private attribute (will raise an AttributeError)
try:
    print("PIN (Private Access):", account.__pin)
except AttributeError:
    print("Cannot access private attribute __pin directly.")

# Using the getter method
print("Balance (via Getter):", account.get_balance())

# Using the setter method 
account.set_balance(1500)
print("Updated Balance (via Setter):", account.get_balance())

# Verifying the PIN
pin_input = "22569984"
if account.verify_pin(pin_input):
    print("PIN verification successful.")
else:
    print("Incorrect PIN.")

