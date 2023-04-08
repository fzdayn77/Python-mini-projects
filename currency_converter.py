from requests import get
from pprint import PrettyPrinter

# API: URL and KEY
# Note that the free KEY expires after 3-5 working days and is only used for testing purposes
# website:  https://free.currencyconverterapi.com/
BASE_URL = "https://free.currconv.com/"
API_KEY = ""

printer = PrettyPrinter()

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    
    data = list(data.items())
    data.sort()   # sorting currencies based on their id

    return data


def print_currencies(currencies_list):
    for name, currency in currencies_list:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get('currencySymbol', 'No symbol provided')
        print(f'{_id} - {name} - {symbol}')


def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print('Invalid currencies.')
        return
    
    rate = list(data.values())[0]
    print(f'{currency1} --> {currency2} = {rate}')

    return rate


def convert_currencies(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None: return

    try:
        amount = float(amount)
    except:
        print('Invalid amount.')
        return

    converted_amount = amount * rate
    print(f'{amount} {currency1} = {converted_amount} {currency2}')

    return converted_amount


def main():
    currencies_list = get_currencies()

    print('--------------- Currency Converter ---------------')
    print('Commands: list -> lists all currencies.')
    print('          rate -> returns the exchange rate from currency 1 to currency 2.')
    print('          convert -> converts an amount from currency 1 to currency 2.')
    print()

    while True:
        command = input('Enter a command (or q to quit): ').lower()
        
        if command == 'q':
            break
        elif command == 'list':
            print_currencies(currencies_list)
        elif command == 'rate':
            currency1 = input('Enter currency 1: ').upper()
            currency2 = input('Enter currency 2: ').upper()
            exchange_rate(currency1, currency2)
        elif command == 'convert':
            currency1 = input('Enter currency 1: ').upper()
            amount = input(f'Enter an amount in {currency1}: ')
            currency2 = input('Enter currency 2: ').upper()
            convert_currencies(currency1, currency2, amount)
        else:
            print('Invalid command! PLease choose one of the written commands.')

    
    pass


main()