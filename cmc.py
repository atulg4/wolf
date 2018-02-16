#u'market_cap_usd': u'5656371921.0', u'price_usd': u'2.03501', u'last_updated': u'1518769150', u'name': u'IOTA', u'24h_volume_usd': u'65444300.0', u'percent_change_7d': u'14.89', u'symbol': u'MIOTA', u'price_btc': u'0.00020623', u'rank': u'10', u'percent_change_1h': u'-1.23', u'total_supply': u'2779530283.0', u'cached': False, u'max_supply': u'2779530283.0', u'available_supply': u'2779530283.0', u'percent_change_24h': u'-3.88', u'id': u'iota'}
from coinmarketcap import Market
coinmarketcap = Market()
coins = coinmarketcap.ticker(start=0, limit=100, convert='USD')
filtered_change_24 = list(filter(lambda coin:float(coin['percent_change_24h']) > 10, coins))
print filtered_change_24 
