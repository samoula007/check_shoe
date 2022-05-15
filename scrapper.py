import requests
import json
from bs4 import BeautifulSoup
import re
import pandas as pd
from sendMail import send


def check_shoe_size(link, size, sender, password, target):
    # Headers are highly recommended
    headers = headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0',
        'Accept': 'image/webp,*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }
    page = requests.get(link, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    targetSkuId = ""
    available = False

    # The web page is populated with data contained in a script tag which we will look for
    # It is json data
    data = json.loads(soup.find('script', text=re.compile(
        'INITIAL_REDUX_STATE')).text.replace('window.INITIAL_REDUX_STATE=', '')[0:-1])

    # The id we are searching for (more user friendly)
    product_id = ""
    for char in link[::-1]:
        if char == '/':
            break
        else:
            product_id = char + product_id

    # In the json file, the following will give us the possible SKUs list
    skus = data['Threads']['products'][product_id]['skus']
    # And the following their availability
    available_skus = data['Threads']['products'][product_id]['availableSkus']

    # Let's use pandas to cross both tables
    df_skus = pd.DataFrame(skus)
    df_available_skus = pd.DataFrame(available_skus)

    # find the skuId of the wanted size
    for sku in skus:
        if sku["nikeSize"] == size:
            targetSkuId = sku["skuId"]
            break
    # check whether the size is available
    for available_sku in available_skus:
        if available_sku["skuId"] == targetSkuId:
            available = True
            break

    if available:

        send(sender, password, target, "Subject: WANTED SHOE AVAILABILITY", "(>^_^)><(^_^<)\n\n" +
             "The size " + size + " is now available at:\n\n" + link)
    # else:
    #     print("The size " + size + " is not available")
