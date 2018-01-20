# -*- coding: utf-8 -*-
import web
from operate import get_data
import time
urls = (
  '/api/data', 'index'
)


class index:
    def GET(self):
        if 'time_section' in web.input():
            time_section = web.input()['time_section']
        else:
            time_section = u'86400'
        data={}
        data['code']=200
        data['info']=[]
        info=get_data(time.time()-int(time_section.decode()))
        for x in info:
            data['info'].append({'type_name':x[0], 'sell_price':x[1], 'market_price':x[2], 'timestamp':x[3] })
        return(data)
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
