import banking
import pythonapi as api
import consolefile as cf
class Bank:
    def __init__(self):
        self.reader = cf.Reader('console')
        self.writer = cf.Writer('./accounts.txt')
        self.printer = cf.Writer('console')

    def receive_client(self):
        client =  self.reader.read('firstname'), \
                self.reader.read('lastname'), \
                self.reader.read('address'), \
                self.reader.read('balance')
        return client

    def create_account(self):
        client = self.receive_client()
        request = api.TupleRequest(client)

        create_account = banking.CreateAccount()
        account = create_account.execute(request)

        response = api.TextResponse([account])
        self.writer.write(response.data)
        self.printer.write(response.data)

    def make_transaction(self):
        make_transaction = banking.MakeTransaction()
        client =  self.receive_client()
        balace = 0
        request = api.TupleRequest(client)
        # request = {
        #     'account':{
        #         'client': client_request
        #     }
        # }
        transaction = make_transaction.execute(request)
        response = api.TextResponse(transaction)
        self.printer.write(response)

    def run(self):
        self.create_account()
        # self.make_transaction()

if __name__ == '__main__':
    Bank().run()