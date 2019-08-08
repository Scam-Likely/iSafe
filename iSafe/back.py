class Account:
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

def view():
    account = Account('balance.txt')
    return account.balance
