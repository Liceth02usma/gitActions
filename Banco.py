import unittest


class Account:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance

def create_account(account_id, initial_balance=0):
    return Account(account_id, initial_balance)

def deposit_money(account, amount):
    if amount < 0:
        raise ValueError("Cannot deposit a negative amount")
    account.balance += amount

def transfer_money(from_account, to_account, amount):
    if amount < 0:
        raise ValueError("Cannot transfer a negative amount")
    if from_account.balance < amount:
        raise ValueError("Insufficient funds")
    from_account.balance -= amount
    to_account.balance += amount




class TestAccount(unittest.TestCase):
    """Test case for the create_account function."""

    def test_create_account(self):
        """Test create account"""
        self.assertEqual(create_account(19000221, 10000).balance, 10000, "Should be 10000")

    def test_deposit_money(self):
        """Test deposit money"""
        account = create_account(19000221, 10000)
        deposit_money(account, 1320)
        self.assertEqual(account.balance, 11320, "Should be 11320")
    
    def test_deposit_money_negative(self):
        """Test deposit money negative"""
        account = create_account(19000221, 10000)
        with self.assertRaises(ValueError):
            deposit_money(account, -1320)

    def test_transfer_money(self):
        """Test transfer money"""
        account1 = create_account(19000221, 10000)
        account2 = create_account(19000221, 29000)
        transfer_money(account2,account1, 200)
        self.assertTrue(account1.balance == 10200 and account2.balance == 28800, "Should be 10200 and 28800")

    def test_transfer_money_negative(self):
        """Test transfer money negative"""
        account1 = create_account(19000221, 10000)
        account2 = create_account(19000221, 29000)
        with self.assertRaises(ValueError):
             transfer_money(account2,account1, -200)

    def test_transfer_money_negative(self):
        """Test transfer more money"""
        account1 = create_account(19000221, 10000)
        account2 = create_account(19000221, 29000)
        with self.assertRaises(ValueError):
             transfer_money(account2,account1, 2000000)




if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

