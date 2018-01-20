# -*- coding: utf-8 -*-
import requests
from lxml import html
from lxml import etree
import traceback
import time
import threading
from operate import sava_data
from config import configs

Blist= configs['Blist']
header= configs['headers']
proxies= {                     ###代理IP
        "http":'http://127.0.0.1:1080'
    }
len_limit = 70
def collect(type,timestamp):
	try:    
                global len_limit
		url = "https://otcbtc.com/sell_offers?currency=%s&fiat_currency=cny&payment_type=all"%type
		a = requests.get(url=url,headers=header,proxies=proxies)
		# print(a.text)
		tree = html.fromstring(a.text)
		# print(tree)
		price_market = tree.xpath("//div[@class='clearfix current-rate']/div[@class='box']/span[@class='price']/text()")
		sell_price = tree.xpath("//div[@class='clearfix current-rate']/div[@class='box']/span[@class='recent-average-price']/text()")#/span[@class='price']/text")
		if price_market and sell_price:
			sell_price = sell_price[0].replace("\n","").replace("CNY","").strip()
			price_market = price_market[0].replace("\n","").replace("CNY","").strip()
			type_name = type
			timestamp = timestamp
			sava_data([type_name,timestamp,sell_price,price_market])
                        if type =='eos' and float(sell_price) < len_limit:
                            len_limit-=1
                            #sendmail(len_limit)
			print(type,sell_price,price_market)
	except:
		traceback.print_exc()

def main():
	timestamp = time.time()
	for type in Blist:
		threading.Thread(target = collect,args =[type,timestamp]).start()
		time.sleep(0.1)

if __name__ == "__main__":
	while  True:
		threading.Thread(target=main).start()
		time.sleep(60)
