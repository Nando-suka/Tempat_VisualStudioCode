class CreditCard:
    """ A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """    The initial balance is zero.

    customer  the name of customers  (e.g, 'Fernando Tumanggor')
    bank      the name of bank       (e.g, 'Bank Mandiri')
    acnt      the account identifier (e.g, '5391 0375 9387 5309')
    limit     credit limit           (measured in dollars)
    """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of Customer """
        return self._customer

    def get_bank(self):
        """Return the bank's name"""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically stored as string)"""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit

        Return True if charge was processed; False if charge was denied
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def makepayment(self, amount):
        """Process customer payment that reduces balance"""
        self._balance -= amount

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit and instance

        The initial balance is zero.

        customer the name of the customer   (e.g 'John Bowman')
        bank     the name of the bank       (e.g 'California Savings')
        acnt     the account identifier     (e.g, '5391 0375 9387 5309')
        limit    credit limit               (measured in dollars)
        apr      annual percentage rate     (e.g, 0.0825 for 8,25% APR)
        """
        super.__init__(customer, bank, acnt, limit) # call super constructor
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit

        Return True if charge was proceed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price)     # call inherited method
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        """Assess monthly interest on outstanding balance"""

if __name__ == '__main__':
    cc = CreditCard('Fernando', 'Bank BCA', '6754 0984 1341 9834', 1000)
    cc2 = CreditCard('Maholi', 'Bank BRI', '3245 5325 9291 8341', 10000)

    wallet = [CreditCard('John Brown', 'California Savings', '5391 0375 9387', 2500),
              CreditCard('John Bowman', 'California Federal', '3485 0399 1954', 3500),
              CreditCard('John Bowman', 'California Finance', '5391 0375 5309', 5000),
              CreditCard('John Bowman', 'California Emerging', '2134 0281 5330', 4000)]

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)
        wallet[3].charge(4*val)

    for c in range(4):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].makepayment(100)
            print('New Balance =', wallet[c].get_balance())
        print()
