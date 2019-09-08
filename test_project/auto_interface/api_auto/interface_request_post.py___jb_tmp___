#coding:utf-8

import requests
import json

class reqst_post():

    def __init__(self):
        pass

    def reqst_data(self,url,json = "", data = "", params="",header="",files ={}):

        print(data)
        htl = requests.post(url=url,params=params,json=json, data= data, headers=header,files=files)
        print(htl.status_code)
        print(htl.content.decode("utf-8"))
        pass



if __name__ == "__main__":
    url = "http://www.baidu.com"
    params= ""
    header = ""
    data = "data"
    boy = ""
    r = reqst_post()
    r.reqst_data(url,data,boy)
