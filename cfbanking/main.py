from bank import Bank

class Main:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        self.bank.create_account()


if __name__ == '__main__':
    Main().run()