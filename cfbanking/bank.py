import banking
import pythonapi as api
from cfbanking.domain import Client, Account
class Bank:
    def __init__(self):
        self.client = Client()
        self.accounts = Account('./accounts.txt')
    
    def create_account(self):
        client = self.client.read_client()
        balance = self.client.read_float('balance')
        request = api.TupleRequest(client+(balance,))

        create_account = banking.CreateAccount()
        account = create_account.execute(request.data)

        response = api.TextResponse(account)
        print(response.data)
        self.accounts.add(response.data)

    def delete_account(self):
        code = self.client.read_code()
        accounts = self.accounts.read()
        accounts = api.TextRequest(accounts).data
        for i, account in enumerate(accounts):
            if account['code'] == str(code[1]):
                print('ACCOUNT DELETED:\n')
                print(api.TextResponse(account).data)
                del accounts[i]
        new_accounts = api.TextResponse(accounts).data
        self.accounts.write(new_accounts)

    def find_account(self):
        code = self.client.read_code()

        # search the corresponding account into the database
        accounts = self.accounts.read()
        accounts = api.TextRequest(accounts).data
        for account in accounts:
            if account['code'] == str(code[1]): # found account
                response = api.TextResponse(account)
                self.client.show(response.data)
        return account['code']

    def make_transaction(self):
        make_transaction = banking.MakeTransaction()

        # get code from client
        code = self.client.read_code()

        # search the corresponding account into the database
        accounts = self.accounts.read()
        accounts = api.TextRequest(accounts).data
        for i, account in enumerate(accounts):
            if account['code'] == str(code[1]): # found account
                action = self.client.read_action()
                amount = self.client.read_int('amount')
                data = action, amount, ('account', account)
                client_request = api.TupleRequest(data)
                try:
                    transaction = make_transaction.execute(client_request.data)
                except Exception as e:
                    self.client.show(f"\n{e}")
                    return
                # update account balance
                account['balance'] = transaction['new_balance']
                accounts[i] = account
                # save to database
        transaction_response = api.TextResponse(accounts)
        self.accounts.write(transaction_response.data)


    def run(self):
        option = input("""
Choose an option between the following:
0. QUIT the Bank now !
1. CREATE a new account
2. FIND an existing account
3. DELETE an existing account
4. Make a TRANSACTION (deposit or withdraw)
""")
        try:
            option = int(option)
        except Exception:
            print('\nInput should be number!')
            self.run()
        if option == 0:
            return
        elif option == 1:
            self.create_account()
            self.run()
        elif option == 2:
            self.find_account()
            self.run()
        elif option == 3:
            self.delete_account()
            self.run()
        elif option == 4:
            self.make_transaction()
            self.run()
        else:
            print(f"\nOption {option} is not supported by our bank")
            self.run()

if __name__ == '__main__':
    print("\n---------------Welcome To our Bank---------------")
    Bank().run()