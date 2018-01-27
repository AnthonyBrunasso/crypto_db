import urllib.request, json

class TickResult:
    def __init__(self, base_volume, close_value, high_value, low_value, open_value, timestamp, volume):
        self.base_volume = base_volume
        self.close_value = close_value
        self.high_value = high_value
        self.low_value = low_value
        self.open_value = open_value
        self.timestamp = timestamp
        self.volume = volume

    def __str__(self):
        return "TickResult (O: {0}, H: {1}, L: {2}, C: {3}, V: {4}, T: {5}, BV: {6})".format(self.base_volume, self.close_value, self.high_value, self.low_value, self.open_value, self.timestamp, self.volume)

def get_all_market_summaries():
    markets = []
    with urllib.request.urlopen('https://bittrex.com/api/v2.0/pub/markets/GetMarketSummaries') as url:
        data = json.loads(url.read().decode())
        for entry in data['result']:
            markets.append(entry['Summary']['MarketName'])
    return markets

def get_ticks(market, tick_interval='hour'):
    prices = []
    try:
        with urllib.request.urlopen('https://bittrex.com/api/v2.0/pub/market/GetTicks?marketName={0}&tickInterval={1}'.format(market, tick_interval)) as url:
            data = json.loads(url.read().decode())
            for entry in data['result']:
                tr = TickResult(entry['BV'], 
                    entry['C'], 
                    entry['H'],
                    entry['L'],
                    entry['O'],
                    entry['T'],
                    entry['V'])
                prices.append(tr)
    except Exception as inst:
        print('Exception {0} type {1} args {2}'.format(inst, type(inst), inst.args))
        print('Could not get market {0}'.format(market))
    return prices

