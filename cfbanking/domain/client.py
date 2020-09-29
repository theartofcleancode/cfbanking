from consolefile.domain import Console

class Client(Console):
    def read(self):
        firstname = super().read('firstname')
        lastname = super().read('lastname')
        address = super().read('address')
        return firstname, lastname, address

    def read_balance(self):
        return super().read_float('balance')

    def read_code(self):
        return super().read_int('code')
