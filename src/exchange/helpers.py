
import requests


def get_exchange_rates():
    # Where USD is the base currency you want to use
    url = 'https://v6.exchangerate-api.com/v6/2c4750bcb38a08424d1f44ef/latest/USD'

    # Making our request
    response = requests.get(url)
    data = response.json()

    # Your JSON object
    print(data)
        