import urllib.request, json

def get_all_market_summaries():
    markets = []
    with urllib.request.urlopen("https://bittrex.com/api/v1.1/public/getmarketsummaries") as url:
        data = json.loads(url.read().decode())
        for entry in data['result']:
            markets.append(entry['MarketName'])
    return markets

def get_market_history(market):
    prices = []
    try:
        with urllib.request.urlopen('https://bittrex.com/api/v1.1/public/getmarkethistory?market={0}'.format(market)) as url:
            data = json.loads(url.read().decode())
            for entry in data['result']:
                prices.append(entry['Price'])
    except:
        print('Could not get market {0}'.format(market))
    return prices

