import unittest
import cfbanking as cfb

class TestRead(unittest.TestCase):
    def test_simple(self):
        account = cfb.domain.Account('./tests/read_accounts.txt')
        data = account.read()
        print(data)

class TestWrite(unittest.TestCase):
    def test_simple(self):
        account = cfb.domain.Account('./tests/write_accounts.txt')
        data = ['CLIENT:\n', '    FIRSTNAME: Moctar\n', '    LASTNAME: Diallo\n', '    ADDRESS: Medina\n', 'BALANCE: 40.0\n', 'CODE: 6732\n', '\n', 'CLIENT:\n', '    FIRSTNAME: Amadou\n', '    LASTNAME: Sow\n', '    ADDRESS: Plateau\n', 'BALANCE: 555.5\n', 'CODE: 5144\n', '\n']
        account.write(data)

    def test_write_paragraph(self):
        paragraph = """ACCOUNT:
CLIENT:
    FIRSTNAME: Moctar
    LASTNAME: Diallo
BALANCE: 5000

"""
        account = cfb.domain.Account('./tests/write_paragraphs.txt')
        account.write(paragraph)

class TestAdd(unittest.TestCase):
    def test_simple(self):
        account = cfb.domain.Account('./tests/append_accounts.txt')
        data = ['CLIENT:\n', '    FIRSTNAME: Moctar\n', '    LASTNAME: Diallo\n', '    ADDRESS: Medina\n', 'BALANCE: 40.0\n', 'CODE: 6732\n', '\n']
        account.write(data)
        data = ['CLIENT:\n', '    FIRSTNAME: Amadou\n', '    LASTNAME: Sow\n', '    ADDRESS: Plateau\n', 'BALANCE: 555.5\n', 'CODE: 5144\n', '\n']
        account.add(data)

if __name__ == '__main__':
    unittest.main()