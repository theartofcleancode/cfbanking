import banking
import pythonapi as api
import consolefile as cf
class Bank:
    def __init__(self):
        self.reader = cf.Reader('console')
        self.writer = cf.Writer('./accounts.txt')
        self.printer = cf.Writer('console')

    def create_account(self):
        client =  self.reader.read('First Name'), \
                self.reader.read('Last Name'), \
                self.reader.read('Address'), \
                self.reader.read('Balance')
        request = api.TupleRequest(client)

        create_account = banking.CreateAccount()
        account = create_account.execute(request)

        response = api.TextResponse([account])
        self.writer.write(response.data)
        self.printer.write(response.data)

    def run(self):
        self.create_account()

if __name__ == '__main__':
    Bank().run()