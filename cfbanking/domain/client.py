from consolefile.domain import Console

class Client(Console):
    def read_client(self):
        firstname = super().read('firstname')
        lastname = super().read('lastname')
        address = super().read('address')
        return firstname, lastname, address

    def read_balance(self):
        return super().read_float('balance')

    def read_code(self):
        return super().read_int('code')

    def read_action(self):
        var, val = super().read('action', info=' (deposit / d / withdraw / w) ')
        if val not in ['deposit', 'withdraw', 'd', 'w']:
            return self.read_action()
        else:
            return var, val


    def show(self, data):
        super().write(data)
