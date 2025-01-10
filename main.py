from locale import currency

import requests
from pprint import pprint as print

API_KEY = '8d155b29d9f40459f46dd501'

currency = 'USD'
url = f"https://v6.exchangerate=api.com/v6/{API_KEY}/pair{currency}/UZS"

r = requests.get(url)
print(r.status_code)
res = r.json()
print(res)
print(res['convertion_rate'])

