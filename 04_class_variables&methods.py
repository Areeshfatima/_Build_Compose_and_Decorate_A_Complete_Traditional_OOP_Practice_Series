# Class Variables and Class Methods

class Bank:

    # Class variable: shared by all objects of the class
    bank_name = "HBL"

    def __init__(self, account_holder):

            # Instance variable: unique for each object
            self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
            
            # Class method: modifies the class variable using 'cls'
            cls.bank_name = name
        
    def display(self):
            
            # This method displays the account holder and the current bank name
            print(f"Account Holder: {self.account_holder} , Bank: {self.bank_name}")


# Creating two Bank account objects
my_account1 = Bank("Arsh")
my_account2 = Bank("Hooria")

# Displaying initial values (both show 'HBL')
my_account1.display()
my_account2.display()

# Changing the class variable 'bank_name' using class method
Bank.change_bank_name("Islamic Bank")

# Displaying values again (both now show 'Islamic Bank')
my_account1.display()
my_account2.display()