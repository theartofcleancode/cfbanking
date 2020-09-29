import unittest

from cfbanking.domain import Client

class TestRead(unittest.TestCase):
    @unittest.skip('asks user input but already tested')
    def test_simple(self):
        client = Client()
        firstname, lastname, address = client.read_client()
        self.assertIsInstance(firstname, tuple)
        self.assertEqual(firstname[0], 'firstname')
        self.assertIsInstance(firstname[1], str)
        self.assertIsInstance(lastname, tuple)
        self.assertEqual(lastname[0], 'lastname')
        self.assertIsInstance(lastname[1], str)
        self.assertIsInstance(address, tuple)
        self.assertEqual(address[0], 'address')
        self.assertIsInstance(address[1], str)


class TestReadBalance(unittest.TestCase):
    @unittest.skip('asks user input, but worked')
    def test_simple(self):
        client = Client()
        balance = client.read_balance()
        self.assertIsInstance(balance, tuple)
        self.assertEqual(balance[0], 'balance')
        self.assertIsInstance(balance[1], float)

class TestReadAction(unittest.TestCase):
    # @unittest.skip('asks user input, but worked')
    def test_simple(self):
        client = Client()
        action = client.read_action()
        self.assertIsInstance(action, tuple)
        self.assertEqual(action[0], 'action')
        self.assertIsInstance(action[1], str)

if __name__ == '__main__':
    unittest.main()