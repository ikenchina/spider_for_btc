# -*- coding: utf-8 -*-
import web
from operate import get_data
import time
urls = (
  '/api/data', 'index'
)


class index:
    def GET(self):
        time_section = 3600*24 if not web.input()['time_section'] else web.input()['time_section']
        data={}
        data['code']=200
        data['info']=get_data(time.time()-int(time_section.decode()))
        return(data)
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
