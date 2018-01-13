# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
import traceback
from config import configs

def sava_data(data):
    try:
        conn= pymysql.connect(host=configs['host'],
                              port = configs['port'],
                              user=configs['user'],
                              passwd=configs['passwd'],
                              db =configs['db'],
                              charset=configs['charset'])
        cur = conn.cursor()
        sql = 'INSERT INTO history_message(type_name,timestamp,sell_price,market_price) VALUES(%s,%s,%s,%s)' 
        param = [] 
        param.append([data[0],data[1],data[2],data[3]])
        cur.executemany(sql,param)
        cur.close()
        conn.commit()           ###利用事务来提高插入性能
        conn.close()
    except:
    	traceback.print_exc()

def get_data(timestamp):
    try:
        timestamp=str(int(timestamp))
        conn= pymysql.connect(host=configs['host'],
                              port = configs['port'],
                              user=configs['user'],
                              passwd=configs['passwd'],
                              db =configs['db'],
                              charset=configs['charset'])
        cur = conn.cursor()
        sql = 'select type_name,sell_price,market_price,timestamp from history_message where timestamp > %s '
        cur = conn.cursor()
        date=cur.fetchmany(cur.execute(sql,(timestamp)))
        cur.close()
        conn.commit()
        conn.close()
        return date
    except:
        traceback.print_exc()
