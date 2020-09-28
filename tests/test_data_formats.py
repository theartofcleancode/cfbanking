import unittest

import pythonapi as api

class TestReqestClientData(unittest.TestCase):
    def test_read_client(self):
        data = (('firstname', 'moctar'),
                ('lastname', 'diallo'),
                ('address', 'plateau'),
                ('balance', '8000'))
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'firstname': 'moctar',
            'lastname': 'diallo',
            'address': 'plateau',
            'balance': '8000'
        })

    def test_read_client_for_user(self):
        data = (('client',
                (('firstname', 'moctar'),
                ('lastname', 'diallo'),
                ('address', 'medina'),
                ('balance', '8000'))),)
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'client': {
                'firstname': 'moctar',
                'lastname': 'diallo',
                'address': 'medina',
                'balance': '8000'
            }
        })

class TestReqestAccountData(unittest.TestCase):
    def test_account(self):
        data = (('action', 'deposit'), 
                ('account', (
                     ('client', (
                         ('firstname', 'moctar'), 
                         ('lastname', 'diallo'), 
                         ('address', 'medina'), 
                         ('balance', '80000'))
                    ),
                    ('code', '4455'), 
                    ('amount', '5000'))
                ))
        req = api.TupleRequest(data)
        self.assertEqual(req.data, {
            'action': 'deposit',
            'account': {
                'client': {
                    'firstname': 'moctar',
                    'lastname': 'diallo',
                    'address': 'medina',
                    'balance': '80000'
                },
                'code': '4455',
                'amount': '5000'
            }
        })

if __name__ == '__main__':
    unittest.main()