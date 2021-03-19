from filewr import Reader, Writer
from req import CoinGeckoAPI
from win10toast import ToastNotifier
from checker import Checker
import os
import time

CONFIG_TEXTFILE = 'config.txt'
filesize = os.path.getsize(CONFIG_TEXTFILE)

coin_gecko = CoinGeckoAPI()

writer = Writer()
reader = Reader()

if filesize < 1:
    coin_lst = coin_gecko.get_coin_list()
    currency_lst = coin_gecko.get_currency_list()
    coin_id_lst = []

    for coin in coin_lst:
        coin_id_lst.append(coin['id'])

    while True:
        # THE CURRENCY YOU USED TO BUY A COIN e.g (PHP, US DOLLARS etc..)
        currency = input('ENTER THE ID OF CURRENCY: ')

        # EVERY WHAT SECONDS YOU WANT THE SYTEM TO CHECK THE COINS
        duration = input('ENTER THE DURATION(SECONDS): ')

        # NUMBER OF COINS YOU HAVE (XRP, BITCOIN = 2)
        num_coins = int(input('ENTER THE NUMBER OF COINS(XRP, BITCOIN = 2): '))

        lst_c = []
        lst_q = []
        lst_cp = []

        for i in range(num_coins):
            # EXAMPLE OF COIN ID IS ripple
            coin_id = input('Enter the coin id: ')
            lst_c.append(coin_id)

            # NUMBER OF COINS YOU BOUGHT FOR THIS PARTICULAR CURRENCY
            quantity = input('Enter the quantity: ')
            lst_q.append(quantity)

            # THE PRICE WHEN YOU BOUGHT THE COIN
            current_price = input('ENTER THE PRICE WHEN YOU BOUGHT IT: ')
            lst_cp.append(current_price)

        # CHECK IF THE CURRENCY ID EXISTS
        if(currency not in currency_lst):
            continue

        for id in lst_c:
            if id not in coin_id_lst:
                continue

        writer.write(currency, duration, lst_cp, lst_q, lst_c)
        break

while True:
    content = reader.get_content()
    coin_gecko_prices = []

    for i in content['COIN']:
        coin_id_trimmed = i.rstrip()
        currency_id_trimmed = content['CURRENCY'].rstrip()
        coin_geck_req = coin_gecko.get_price(
            coin_id_trimmed, currency_id_trimmed)
        coin_gecko_prices.append(
            coin_geck_req[coin_id_trimmed][currency_id_trimmed])

    checker = Checker(
        coin_gecko_prices, content['COIN'], content['QUANTITY'], content['CURRENT_PRICE'])

    bools = checker.has_increased()
    toaster = ToastNotifier()

    for i in range(len(content['COIN'])):
        if bools[i]:
            toaster.show_toast(
                "PRICE HAS INCREASED!", content['COIN'][i] + "price has increased by " + str(checker.get_diff(i)) + " " + content['CURRENCY'].rstrip())

    time.sleep(int(content['DURATION']))
