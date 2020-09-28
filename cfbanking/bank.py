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
                self.reader.read('address')
        return client
        

    def prepare_transaction(self):
        client =  'client', self.receive_client()
        code = self.reader.read('code')
        amount = self.reader.read('amount')
        action = self.reader.read('action')
        balance = self.reader.read('balance')
        return action, ('account', (client, code, balance)), amount

    def create_account(self):
        client = self.receive_client()
        balance = self.reader.read('balance')
        request = api.TupleRequest(client+(balance,))

        create_account = banking.CreateAccount()
        account = create_account.execute(request.data)

        response = api.TextResponse(account)
        self.writer.write(response.data)
        self.printer.write(response.data)

    def make_transaction(self):
        make_transaction = banking.MakeTransaction()

        # get code from client
        console_reader = cf.Reader('console')
        console_writer = cf.Writer('console')
        code = console_reader.read('code')

        # search the corresponding account into the database
        with open('./accounts.txt') as f:
            text = f.readlines()
        accounts = api.TextRequest(text).data
        for i, account in enumerate(accounts):
            if account['code'] == str(code[1]): # found account
                action = console_reader.read('action')
                amount = console_reader.read('amount')
                data = action, amount, ('account', account)
                client_request = api.TupleRequest(data)
                transaction = make_transaction.execute(client_request.data)
                # update account balance
                account['balance'] = transaction['new_balance']
                accounts[i] = account
                # save to database
                transaction_response = api.TextResponse(accounts)
                file_writer = cf.Writer('./accounts.txt')
                file_writer.write(transaction_response.data, mode='w+')
        else:
            console_writer.write('Account not found', 'w+')

    def run(self):
        # self.create_account()
        self.make_transaction()

if __name__ == '__main__':
    Bank().run()