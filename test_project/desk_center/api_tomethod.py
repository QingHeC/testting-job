# coding:utf-8

import json


def str_to_json(data):
    data_jso = json.loads(data.replace("'", "\""))
    data_lis = []
    for i_list in data_jso.keys():
        data_lis.append([i_list, data_jso[i_list]])
    return data_lis
