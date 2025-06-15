class list:
    def __init__(self):
        self.size = 0
        self.coins = 4

    def addSize(self):
        self.size += 1

    def subtractCoins(self):
        self.coins -= 1

    def __str__(self):
        size = str(self.size)
        coins = str(self.coins)
        return size + ' ' + coins

obj = list()
print(obj)
