#!./venv/bin/python

import json
import requests

i = 'https://erau.unba.org.ua/search?limit=65167&offset=0&order[surname]=ASC&addation[probono]=0&addation[military_probono]=0&foreigner=0'

h = requests.get(i)

data = h.json()

with open('data.json', 'w') as f:
    json.dump(data, f)
