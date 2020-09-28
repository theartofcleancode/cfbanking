import unittest

import cfbanking as cfb
import consolefile as cf

class TestBank(unittest.TestCase):
    def setUp(self):
        self.reader = cf.Reader('console')

    @unittest.skip('asks user input, but worked')
    def test_receive_client(self):
        bank = cfb.Bank()
        client = bank.receive_client()
        print(client)

    @unittest.skip('asks user input, but worked')
    def test_prepare_transactions(self):
        bank = cfb.Bank()
        account = bank.prepare_transaction()
        print(account)

    def test_prepare_create_account(self):
        bank = cfb.Bank()
        client = bank.receive_client()
        balance = self.reader.read('balance')
        print(client+(balance,))

if __name__ == '__main__':
    unittest.main()