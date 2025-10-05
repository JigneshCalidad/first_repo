"""
🏦 OOP PROJECT - Bank System
===========================

A comprehensive bank system demonstrating OOP principles including
encapsulation, inheritance, polymorphism, and abstraction! 💰
"""

print("=== BANK SYSTEM PROJECT ===")

# This project demonstrates:
# - Encapsulation: Private attributes and controlled access
# - Inheritance: Different account types
# - Polymorphism: Same interface, different implementations
# - Abstraction: Complex banking operations simplified

class BankAccount:
    """Base class for all bank accounts"""
    
    def __init__(self, account_number, account_holder, initial_balance=0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = initial_balance
        self._transactions = []
        self._is_active = True
    
    def deposit(self, amount):
        """Deposit money into account"""
        if not self._is_active:
            return "Account is inactive"
        
        if self._validate_amount(amount):
            self._balance += amount
            self._record_transaction(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self._balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if not self._is_active:
            return "Account is inactive"
        
        if self._validate_amount(amount) and self._has_sufficient_funds(amount):
            self._balance -= amount
            self._record_transaction(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        else:
            return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Get current balance"""
        return self._balance
    
    def get_account_info(self):
        """Get account information"""
        return f"Account: {self._account_number}, Holder: {self._account_holder}, Balance: ${self._balance}"
    
    def get_transactions(self):
        """Get transaction history"""
        return self._transactions.copy()
    
    def deactivate(self):
        """Deactivate account"""
        self._is_active = False
        return "Account deactivated"
    
    def activate(self):
        """Activate account"""
        self._is_active = True
        return "Account activated"
    
    # Private methods
    def _validate_amount(self, amount):
        """Validate amount"""
        return isinstance(amount, (int, float)) and amount > 0
    
    def _has_sufficient_funds(self, amount):
        """Check if account has sufficient funds"""
        return amount <= self._balance
    
    def _record_transaction(self, transaction):
        """Record transaction"""
        self._transactions.append(transaction)

class SavingsAccount(BankAccount):
    """Savings account with interest"""
    
    def __init__(self, account_number, account_holder, initial_balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, initial_balance)
        self._interest_rate = interest_rate
        self._minimum_balance = 100
    
    def add_interest(self):
        """Add interest to account"""
        if self._is_active and self._balance >= self._minimum_balance:
            interest = self._balance * self._interest_rate
            self._balance += interest
            self._record_transaction(f"Interest added: ${interest:.2f}")
            return f"Interest added: ${interest:.2f}. New balance: ${self._balance:.2f}"
        else:
            return "Cannot add interest - account inactive or below minimum balance"
    
    def withdraw(self, amount):
        """Override withdraw to check minimum balance"""
        if self._balance - amount < self._minimum_balance:
            return f"Cannot withdraw ${amount} - would go below minimum balance of ${self._minimum_balance}"
        return super().withdraw(amount)
    
    def get_account_info(self):
        """Override to include interest rate"""
        base_info = super().get_account_info()
        return f"{base_info}, Interest Rate: {self._interest_rate*100}%"

class CheckingAccount(BankAccount):
    """Checking account with overdraft protection"""
    
    def __init__(self, account_number, account_holder, initial_balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, initial_balance)
        self._overdraft_limit = overdraft_limit
        self._overdraft_used = 0
    
    def withdraw(self, amount):
        """Override withdraw to allow overdraft"""
        if not self._is_active:
            return "Account is inactive"
        
        if not self._validate_amount(amount):
            return "Invalid withdrawal amount"
        
        if amount <= self._balance:
            # Normal withdrawal
            self._balance -= amount
            self._record_transaction(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        elif amount <= self._balance + self._overdraft_limit - self._overdraft_used:
            # Overdraft withdrawal
            overdraft_needed = amount - self._balance
            self._overdraft_used += overdraft_needed
            self._balance = 0
            self._record_transaction(f"Withdrew ${amount} (Overdraft: ${overdraft_needed})")
            return f"Withdrew ${amount} using overdraft. Balance: ${self._balance}, Overdraft used: ${self._overdraft_used}"
        else:
            return f"Insufficient funds and overdraft limit exceeded"
    
    def get_account_info(self):
        """Override to include overdraft information"""
        base_info = super().get_account_info()
        return f"{base_info}, Overdraft Limit: ${self._overdraft_limit}, Overdraft Used: ${self._overdraft_used}"

class BusinessAccount(BankAccount):
    """Business account with special features"""
    
    def __init__(self, account_number, account_holder, initial_balance=0, business_type="LLC"):
        super().__init__(account_number, account_holder, initial_balance)
        self._business_type = business_type
        self._employees = []
        self._monthly_fee = 25
    
    def add_employee(self, employee_name, employee_id):
        """Add employee to business account"""
        self._employees.append({"name": employee_name, "id": employee_id})
        return f"Added employee: {employee_name} (ID: {employee_id})"
    
    def remove_employee(self, employee_id):
        """Remove employee from business account"""
        for i, emp in enumerate(self._employees):
            if emp["id"] == employee_id:
                removed = self._employees.pop(i)
                return f"Removed employee: {removed['name']}"
        return "Employee not found"
    
    def get_employees(self):
        """Get list of employees"""
        return self._employees.copy()
    
    def charge_monthly_fee(self):
        """Charge monthly fee"""
        if self._is_active:
            self._balance -= self._monthly_fee
            self._record_transaction(f"Monthly fee charged: ${self._monthly_fee}")
            return f"Monthly fee charged: ${self._monthly_fee}. New balance: ${self._balance}"
        else:
            return "Cannot charge fee - account inactive"
    
    def get_account_info(self):
        """Override to include business information"""
        base_info = super().get_account_info()
        return f"{base_info}, Business Type: {self._business_type}, Employees: {len(self._employees)}"

class Bank:
    """Bank class to manage all accounts"""
    
    def __init__(self, name):
        self.name = name
        self._accounts = {}
        self._account_counter = 1000
    
    def create_account(self, account_type, account_holder, initial_balance=0, **kwargs):
        """Create a new account"""
        account_number = str(self._account_counter)
        self._account_counter += 1
        
        if account_type.lower() == "savings":
            account = SavingsAccount(account_number, account_holder, initial_balance, **kwargs)
        elif account_type.lower() == "checking":
            account = CheckingAccount(account_number, account_holder, initial_balance, **kwargs)
        elif account_type.lower() == "business":
            account = BusinessAccount(account_number, account_holder, initial_balance, **kwargs)
        else:
            return "Invalid account type"
        
        self._accounts[account_number] = account
        return f"Created {account_type} account {account_number} for {account_holder}"
    
    def get_account(self, account_number):
        """Get account by number"""
        return self._accounts.get(account_number)
    
    def get_all_accounts(self):
        """Get all accounts"""
        return self._accounts.copy()
    
    def get_bank_info(self):
        """Get bank information"""
        total_accounts = len(self._accounts)
        total_balance = sum(account.get_balance() for account in self._accounts.values())
        return f"Bank: {self.name}, Accounts: {total_accounts}, Total Balance: ${total_balance:.2f}"

# Test the bank system
print("=== Bank System Test ===")

# Create bank
bank = Bank("Python Bank")
print(bank.get_bank_info())

# Create different account types
print("\n=== Creating Accounts ===")
print(bank.create_account("savings", "Alice", 1000, interest_rate=0.03))
print(bank.create_account("checking", "Bob", 500, overdraft_limit=1000))
print(bank.create_account("business", "Charlie", 5000, business_type="Corporation"))

# Get accounts
alice_account = bank.get_account("1000")
bob_account = bank.get_account("1001")
charlie_account = bank.get_account("1002")

print("\n=== Account Operations ===")
# Test savings account
print("=== Savings Account (Alice) ===")
print(alice_account.get_account_info())
print(alice_account.deposit(500))
print(alice_account.withdraw(200))
print(alice_account.add_interest())
print(f"Transactions: {alice_account.get_transactions()}")

print("\n=== Checking Account (Bob) ===")
print(bob_account.get_account_info())
print(bob_account.deposit(300))
print(bob_account.withdraw(800))  # This will use overdraft
print(bob_account.withdraw(200))  # This will use more overdraft
print(f"Transactions: {bob_account.get_transactions()}")

print("\n=== Business Account (Charlie) ===")
print(charlie_account.get_account_info())
print(charlie_account.add_employee("David", "E001"))
print(charlie_account.add_employee("Eve", "E002"))
print(charlie_account.charge_monthly_fee())
print(f"Employees: {charlie_account.get_employees()}")
print(f"Transactions: {charlie_account.get_transactions()}")

print("\n=== Bank Summary ===")
print(bank.get_bank_info())

print("\n=== OOP PRINCIPLES DEMONSTRATED ===")

print("""
This bank system demonstrates:

1. ENCAPSULATION:
   - Private attributes (_account_number, _balance, etc.)
   - Controlled access through public methods
   - Data validation in private methods

2. INHERITANCE:
   - BankAccount as base class
   - SavingsAccount, CheckingAccount, BusinessAccount inherit from BankAccount
   - Method overriding (withdraw, get_account_info)

3. POLYMORPHISM:
   - Same interface (deposit, withdraw, get_balance) for different account types
   - Different implementations for each account type
   - Runtime behavior based on actual object type

4. ABSTRACTION:
   - Complex banking operations simplified through methods
   - Hidden implementation details
   - Simple interface for users

5. COMPOSITION:
   - Bank class contains multiple accounts
   - BusinessAccount contains employees
   - Modular design for easy extension
""")

print("\n=== EXTENDING THE SYSTEM ===")

# Example of extending the system
class CreditCardAccount(BankAccount):
    """Credit card account with credit limit"""
    
    def __init__(self, account_number, account_holder, credit_limit=5000):
        super().__init__(account_number, account_holder, 0)
        self._credit_limit = credit_limit
        self._credit_used = 0
    
    def make_purchase(self, amount):
        """Make a purchase with credit card"""
        if self._credit_used + amount <= self._credit_limit:
            self._credit_used += amount
            self._record_transaction(f"Purchase: ${amount}")
            return f"Purchase of ${amount} approved. Credit used: ${self._credit_used}"
        else:
            return "Purchase declined - credit limit exceeded"
    
    def make_payment(self, amount):
        """Make payment to credit card"""
        if amount <= self._credit_used:
            self._credit_used -= amount
            self._record_transaction(f"Payment: ${amount}")
            return f"Payment of ${amount} processed. Credit used: ${self._credit_used}"
        else:
            return "Payment amount exceeds credit used"
    
    def get_available_credit(self):
        """Get available credit"""
        return self._credit_limit - self._credit_used
    
    def get_account_info(self):
        """Override to include credit information"""
        base_info = super().get_account_info()
        return f"{base_info}, Credit Limit: ${self._credit_limit}, Credit Used: ${self._credit_used}"

# Test credit card account
print("=== Credit Card Account ===")
credit_card = CreditCardAccount("2000", "Frank", 3000)
print(credit_card.get_account_info())
print(credit_card.make_purchase(500))
print(credit_card.make_purchase(1000))
print(credit_card.make_payment(300))
print(f"Available credit: ${credit_card.get_available_credit()}")
print(f"Transactions: {credit_card.get_transactions()}")

print("\n=== PROJECT COMPLETED ===")

print("""
This bank system project demonstrates:
- Real-world OOP application
- Multiple inheritance patterns
- Complex business logic
- Extensible design
- Professional code structure
- Comprehensive testing

Key Learning Points:
1. OOP principles in practice
2. Design patterns (Factory, Strategy)
3. Error handling and validation
4. Code organization and structure
5. Real-world problem solving
""")

"""
Key Points to Remember:
1. Use OOP principles to solve real problems
2. Design for extensibility and maintainability
3. Implement proper error handling
4. Test your code thoroughly
5. Document your design decisions
6. Practice with real-world examples
7. Learn from existing systems
8. Keep code simple and focused
9. Follow best practices
10. Continuously improve your skills
"""
