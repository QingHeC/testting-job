
#coding:utf-8

from auto_interface import models

def ret_left_interface_listname():
    list_inter_name = models.Left_name_data.objects.values("id", "name_data").distinct()

    data = []
    for lis in list_inter_name:

        # print(lis)
        list_name_data = models.Left_name_data_lists.objects.values("data_list_name", "id").filter(
            left_name_data_id_id=lis["id"]).distinct()
        # print(list_name_data)
        list_data = []
        left_list_name_data = {}
        for list_name in list_name_data:
            li = []
            li.append(list_name["data_list_name"])
            li.append(list_name["id"])
            # list_data[list_name["id"]] = list_name["data_list_name"]
            list_data.append(li)
            # print(list_data)
        left_list_name_data[lis["name_data"]] = list_data

        data.append(left_list_name_data)
    print("data: %s" %data)
    return data