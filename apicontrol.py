# -*- coding: utf-8 -*-
import web
from operate import get_data
import time
urls = (
  '/api/data', 'index'
)


class index:
    def GET(self):
        data={}
        data['code']=200
        data['info']=get_data(time.time()-3600)
        return(data) 
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
