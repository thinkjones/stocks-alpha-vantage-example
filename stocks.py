import requests
from jsonschema import validate
import sys

# To run -> python stocks.py API KEY
# See https://www.alphavantage.co/documentation/ to get API key

DIGITAL_CURRENCY_MONTHLY_SCHEMA = {
    "type": "object",
    "properties": {
        "Meta Data": {"type": "object"},
        "Time Series (Digital Currency Monthly)": {"type": "object"},
    },
    "required": ["Meta Data", "Time Series (Digital Currency Monthly)"]
}


class MonthlyPriceTransform:

    @staticmethod
    def store_this_key(full_key_name):
        search_for_keys = ['open', 'high', 'low', 'close', 'volume', 'market cap']
        is_valid_key = any(k for k in search_for_keys if full_key_name.find(k) >= 0)

        usd_keys = ['open', 'high', 'low', 'close', 'market cap']
        key_requires_usd = any(k for k in usd_keys if full_key_name.find(k) >= 0)

        return is_valid_key and full_key_name.lower().find('usd') >= 0 if key_requires_usd else is_valid_key

    @staticmethod
    def from_json(price_date, values_dict):
        dp = MonthlyPriceTransform(price_date)

        for k, v in {k: v for k, v in values_dict.items() if MonthlyPriceTransform.store_this_key(k)}.items():
            if k.find('open') >= 0:
                dp.open = v
            elif k.find('high') >= 0:
                dp.high = v
            elif k.find('low') >= 0:
                dp.low = v
            elif k.find('close') >= 0:
                dp.close = v
            elif k.find('volume') >= 0:
                dp.volume = v
            elif k.find('market cap') >= 0:
                dp.market_cap = v
            else:
                raise ValueError(f'Key not supported {k}')

        return dp

    def __init__(self, price_date):
        self.price_date = price_date
        self.open = None
        self.high = None
        self.low = None
        self.close = None
        self.volume = None
        self.market_cap = None

    def to_csv(self):
        # TODO: In prod code would use CSV library to do this.
        return f'{self.price_date},{self.open},{self.high},{self.low},{self.close},{self.volume},{self.market_cap}'


def request_monthly_prices(api_key):
    base_url = 'https://www.alphavantage.co/query'
    url_params = {
        'function': 'DIGITAL_CURRENCY_MONTHLY',
        'symbol': 'BTC',
        'market': 'CNY',
        'apikey': api_key
    }

    # Non stream json formatted version
    r = requests.get(base_url, url_params)

    # Validate response type
    print(f'Returned status: {r.status_code}')
    if r.status_code != 200:
        print(f'An error occurred [{r.status_code}]')
        r.raise_for_status()

    # Get Data
    json_response = r.json()

    # Validate Data Schema
    is_valid = validate(instance=json_response, schema=DIGITAL_CURRENCY_MONTHLY_SCHEMA) is None
    print(f'Schema is {"valid" if is_valid else "not valid"}')

    # Process Data to rough CSV output
    daily_prices = [MonthlyPriceTransform.from_json(k, v) for k, v in
                    json_response['Time Series (Digital Currency Monthly)'].items()]
    for dp in daily_prices:
        print(dp.to_csv())

    # WIP: Stream version for large json files. Would probably end up using ijson - https://pypi.org/project/ijson/
    # r = requests.get(base_url, url_params, stream=True)
    # for line in r.iter_lines():
    #    if line:
    #        print(line.decode('utf8'))


if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    if len(sys.argv) > 1:
        request_monthly_prices(sys.argv[1])
    else:
        print('Please supply the ALPHA_VANTAGE_API_KEY as the first argument')
