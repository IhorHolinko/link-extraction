#!./venv/bin/python

# import python packages

import json
import lxml.html
import requests


# open the json file and assign to variable
with open('data.json', 'r') as f:
    jd = f.read()


# parse content of variable and convert to json format
jd_parsed = json.loads(jd)


# check if size of items is not equal 0
if len(jd_parsed) != 0:

    # loop through each item
    for p in jd_parsed['items']:

        # get id of current loop
        p_id = p['id']

        # prepare url string
        i = 'https://erau.unba.org.ua/profile/{}'.format(p_id)

        # make an http request
        r = requests.get(i)

        # get content from response
        root = lxml.html.fromstring(r.content)

        # query for the telephone number with xpath
        adr = root.xpath('//div[@class="column-right__inner"]/text()')

        # open a file to write extracted inforamation
        with open('{}'.format(p_id), 'w') as f:
            f.write(str(adr))
