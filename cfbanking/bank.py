import banking
import pythonapi as api
from consolefile.domain import Console, File

class Bank:
    def __init__(self):
        self.input = Console()
        self.output = Console()
        self.client_output = File('./clients.txt')

    def create_account(self):
        client =  self.input.read('First Name'), \
                  self.input.read('Last Name'), \
                  self.input.read('Address'), \
                  self.input.read('Balance')
        request = api.TupleRequest(client)

        create_account = banking.CreateAccount()
        account = create_account.execute(request)

        response = api.Response(str(account))
        self.client_output.write(response.data)