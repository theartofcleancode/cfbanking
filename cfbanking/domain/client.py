class Client:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def read(self):
        firstname = self.endpoint.read('firstname')
        lastname = self.endpoint.read('lastname')
        address = self.endpoint.read('address')
        return firstname, lastname, address