class Writer:
    def __init__(self, filename='config.txt'):
        self.textfile = open(filename, 'a')
        self.separator = '||'

    def write(self, currency, duration, current_prices, quantities, coins):
        self.textfile.write('CURRENCY=' + currency + '\n')
        self.textfile.write('DURATION=' + duration + '\n')
        self.__write_coins(coins)
        self.__write_quantities(quantities)
        self. __write_current_price(current_prices)

    def __write_coins(self, coins):
        self.textfile.write('COIN=')
        for coin in coins:
            self.textfile.write(
                coin + self.separator if coin != coins[-1] else coin + '\n')

    def __write_quantities(self, quantities):
        self.textfile.write('QUANTITY=')
        for quantity in quantities:
            self.textfile.write(
                quantity + self.separator if quantity != quantities[-1] else quantity + '\n')

    def __write_current_price(self, current_prices):
        self.textfile.write('CURRENT_PRICE=')
        for current_price in current_prices:
            self.textfile.write(
                current_price + self.separator if current_price != current_prices[-1] else current_price + '\n')


class Reader:
    def __init__(self, filename='config.txt'):
        self.textfile = open(filename, 'r')
        self.separator = '||'
        self.dictionary = {}

    def get_content(self):
        self.__read_textfile()
        return self.dictionary

    def __read_textfile(self):
        contents = self.textfile.readlines()

        for content in contents:
            if 'CURRENCY' in content:
                self.dictionary['CURRENCY'] = content.split('=')[1]
            elif 'DURATION' in content:
                self.dictionary['DURATION'] = content.split('=')[1]
            elif 'CURRENT_PRICE' in content:
                self.__populate_current_price(content)
            elif 'COIN' in content:
                self.__populate_coins(content)
            elif 'QUANTITY' in content:
                self.__populate_quantities(content)
            else:
                continue

    def __populate_coins(self, content):
        lst = content.split('=')[1].split(self.separator)
        self.dictionary['COIN'] = lst

    def __populate_quantities(self, content):
        lst = content.split('=')[1].split(self.separator)
        self.dictionary['QUANTITY'] = lst

    def __populate_current_price(self, content):
        lst = content.split('=')[1].split(self.separator)
        self.dictionary['CURRENT_PRICE'] = lst
