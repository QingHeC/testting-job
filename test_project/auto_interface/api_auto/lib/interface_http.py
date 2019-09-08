#coding:utf-8

from .read_json import str_con_json
import requests, json


class interface_http():

    def __init__(self):
        pass

    def req_get(self,url, params, header=""):
        print(type(params))
        try:
            if type(params).__name__ != "dict":
                sj = str_con_json(params)
                if sj:
                    params = sj
        except:
            pass

        htt = requests.get(url=url,params=params ,headers=header)
        print(htt.content,htt.status_code)

    def req_post(self,url, params,request_data, header=""):
        htt = requests.post(url=url, params=params,data=request_data, headers=header)
        print(htt.content, htt.status_code)
        print("post")
        pass

    def req_requests(self,method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            timeout=None,proxies=None,json=None):

        print(files)
        hrm = requests.request(method,
                               url = url,
                               params = params or {},
                               data = data or {},
                               headers = headers, cookies=None, files=files,
                               timeout=None, allow_redirects=True, proxies=None,
                               json=None
                               )
        # print(hrm.content.decode())
        return hrm


if __name__ == "__main__":
    htm = interface_http().req_requests("get","https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query=2019%E5%B9%B44%E6%9C%88&co=&resource_id=6018&t=1553993862251&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu")
    print(htm.content.decode("ISO-8859-1"))
    print(htm.headers["Content-Type"])
    data = {"da":htm.content.decode("gbk")}
    h = json.dumps(data)
    print(h)