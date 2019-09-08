#coding:utf-8
import json


def json_con_str(c_json):

    try:
        if type(c_json).__name__ == "dict":
            jsd = json.dumps(c_json)
        else:
            return False
    except:
        pass

    return jsd

def str_con_json(c_str):

    try:
        if type(c_str).__name__ == "dict":
            jsd = c_str
        else:
            jsd = json.loads(c_str)
    except :
        return False

    return jsd

