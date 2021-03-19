class Checker:
    def __init__(self, gecko_prices, coins, quantities, current_prices):
        self.gecko_prices = gecko_prices
        self.coins = coins
        self.quantities = quantities
        self.current_prices = current_prices
        self.count = len(gecko_prices)

    def has_increased(self):
        bool_lst = []
        for i in range(self.count):
            if int(self.current_prices[i]) < int(self.gecko_prices[i]):
                bool_lst.append(True)
            else:
                bool_lst.append(False)

        return bool_lst

    def get_diff(self, index):
        return int(self.gecko_prices[index]) - int(self.current_prices[index])
