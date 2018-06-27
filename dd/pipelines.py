# -*- coding: utf-8 -*-

import pymysql

class DdPipeline(object):
    def process_item(self, item, spider):
        #创建连接
        conn = pymysql.connect(host="127.0.0.1",user="root",passwd="654321",db="dd",charset='utf8')
        cursor = conn.cursor()
        cursor.execute('set names utf8')  # 固定格式
        cursor.execute('set autocommit=1')  # 设置自动提交
        for i in range(0,len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            now_price = item["now_price"][i]
            comment_num = item["comment_num"][i]
            detail = item["detail"][i]
            sql = "insert into books(title,link,now_price,comment_num,detail) VALUES (%s,%s,%s,%s,%s)"
            param = (title,link,now_price,comment_num,detail)
            cursor.execute(sql,param )
            conn.commit()
        cursor.close()
        #关闭连接
        conn.close()
        return item
