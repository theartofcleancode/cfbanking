import banking
import pythonapi as api
import consolefile as cf
class Bank:

    def receive_client(self):
        firstname = input('Enter your first name: ')
        lastname = input('Enter your last name: ')
        address = input('Enter your address: ')
        return ('firstname', firstname), ('lastname', lastname), ('address', address)

    def create_account(self):
        client = self.receive_client()
        balance = ('balance', input('Enter your balance: '))
        request = api.TupleRequest(client+(balance,))

        create_account = banking.CreateAccount()
        account = create_account.execute(request.data)

        response = api.TextResponse(account)
        with open('./accounts.txt', 'a+') as f:
            f.write(response.data)
        print(response.data)

    def delete_account(self):
        code = input('Enter your code: ')
        with open('./accounts.txt', 'r') as f:
            text = f.readlines()
        accounts = api.TextRequest(text).data
        for i, account in enumerate(accounts):
            if account['code'] == code:
                del accounts[i]
        new_accounts = api.TextResponse(accounts).data
        # print(new_accounts)
        with open('./accounts.txt', 'w') as f:
            f.write(new_accounts)

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
                with open('./accounts.txt', 'w+') as f:
                    f.write(transaction_response.data)
        else:
            print('Account not found')

    def run(self):
        # self.create_account()
        # self.make_transaction()
        self.delete_account()

if __name__ == '__main__':
    Bank().run()