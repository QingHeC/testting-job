# coding:utf-8

import json
import time,os

from django.shortcuts import render, render_to_response, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from auto_interface.api_auto.configs.config import run_lis, file_save_path
from auto_interface.api_auto.lib.interface_http import interface_http
from auto_interface.api_auto.ret_list import *
from auto_interface.api_auto.run_interface.interfaces_execute import run_word
from auto_interface.api_auto.run_interface.multiple_test_execute import mul_run_word
from desk_center import models as desk_models
# 验证登录
from desk_center.views import Ver_cook_vr
from desk_center.api_tomethod import *

from test_project.settings import BASE_DIR

# Create your views here.

def auto_inters(request):
    dat = []
    return render(request, "", locals())


# auto_interface_list.html

def auto_inter(request):
    inter_list = models.Req_list_data.objects.all()
    # data = []
    # data = ret_left_interface_listname()
    # data.append(left_list_name_data)
    # print(data)
    # rnter_name_data = models.Left_name_data_lists.objects.select_related('left_name_data_id').all()

    list_inter_name = models.Left_name_data.objects.values("id", "name_data").distinct()
    # print("list_inter_name: %s" %list_inter_name)
    # list_name_data1 = models.Left_name_data_lists.objects.get()

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

    # data = [{' 百度': [['百度测试1', 1], ['百度测试2', 3]]}, {'网易': [['网易1', 2]]}]
    # data = [{'百度': [['百度测试1', '1'], ['百度测试2', '3']]},{'网易': [['网易1', '2']]}]

    return render(request, "auto_interface_list.html", locals())


def auto_inter_if():
    return render_to_response()


def auto_inter1(request):
    datas = [
        {"id": "0", "pId": "0", "name": "列表", "open": "false", "iconOpen": "/static/css/auto_in/img/diy/1_open.png",
         "iconClose": "/static/css/auto_in/img/diy/1_close.png"},
        {"id": 111, "pId": 1, "name": "新建1"},
        {"id": 121, "pId": 1, "name": "新建2"},
        {"id": 131, "pId": 1, "name": "新建3"},
        {"id": 2, "pId": 0, "name": "百度天气", "open": "false"},
        {"id": 211, "pId": 2, "name": "百度天气1"},
        {"id": 221, "pId": 2, "name": "百度天气2"},
        {"id": 21, "pId": 2, "name": "百度天气3"},
        {"id": 3, "pId": 0, "name": "百度图片", "open": "false"},
        {"id": 31, "pId": 3, "name": "百度图片1"},
        {"id": 32, "pId": 3, "name": "百度图片2"},
        {"id": 33, "pId": 3, "name": "百度图片3"}

    ]
    dat = json.dumps(datas)
    return render(request, "auto_interface.html", locals())


# 添加HTTP接口页面
def add_interface(request):
    # 验证
    Ver_cook = Ver_cook_vr(request)
    user = [Ver_cook["user_id"], Ver_cook["user_name"]]
    user_ = Ver_cook["user_name"]
    user_Id = Ver_cook["user_id"]

    if request.method == "GET":
        u1 = request.get_full_path()
        print("u1 : %s" % u1)
        inter_name = request.GET.get("list_name")
        project_id = request.GET.get("project")

        case_id = request.GET.get("ecdi")
        if case_id:

            # 后续需要验证是否有权限访问

            # 查询响应case id
            try:
                case_dat = models.Req_list_data.objects.values().get(id=case_id)

                print(case_dat)
                param = case_dat["params"]
                if param:
                    param_lis = str_to_json(param)
                    print(param_lis)
                else:
                    param_lis = []

                header_da = case_dat["headers"]
                print("header_da: %s" % header_da)
                if header_da:
                    header_lis = str_to_json(header_da)
                else:
                    header_lis = []
                body_lists = []
                if case_dat["way_body"] == 'form_data':
                    body_lists = models.req_body.objects.values().filter(req_body_id_id=case_id)
                elif case_dat["way_body"] == 'application_x_w':
                    print("case_dat['body'] :%s" %case_dat["body"])
                    if case_dat["way_body"]:
                        body_lists = str_to_json(case_dat["body"])
                    else:
                        body_lists = []
                else:
                    pass
                print(body_lists)

                # 添加文件 files_upload 数据
                get_files = case_dat["file"]
                if get_files:
                    get_files = str_to_json(get_files)
                    # print(get_files)
                else:
                    get_files = []

                # print(type(get_files))


                assert_list = models.autoin_asserts.objects.values().filter(Req_list_data_id_id=case_id)
                # print(assert_list)

            except BaseException as ex:

                print(" ex : %s" % ex)
        else:
            print("没有进入")

        # 显示属于哪个项目
        pro_name = desk_models.task_projects.objects.values("pro_name").get(id=project_id)["pro_name"]
        # print(inter_name)

        # 查找断言数据
        asser_ts = desk_models.desk_center_asserts.objects.values().all()
        asser_dat = ""
        for i in asser_ts:
            data = {"text": i["assert_name"], "value": i["assert_name"]}
            asser_dat += str(data)

        # asser_dat += ""
        # 传入断言数据
        asser_dat = asser_dat.replace("}{", "},{")
        # {'text': 'assertEqual', 'value': 'a'}
        # print("asser_dat:%s" % asser_dat)
    print("111")
    return render(request, "add_interface_data.html", locals())  # ,locals()


# 根据接口名字显示相应的数据
@csrf_exempt
def list_name(request):
    if request.method == "GET":

        # u = request.path  #路径
        # u =request.get_full_path()  #路径加参数
        # u = request.get_full_path_info() #路径加参数
        # u = request.get_raw_uri()   #全路径
        users = desk_models.list_user_info.objects.values("id", "name", "name_email")
        print(users)

        u1 = request.get_full_path()
        print("u1 : %s" % u1)
        project_number = request.GET.get("project")
        u_id = request.GET.get("id")
        u_name = request.GET.get("data")

        if u_id:
            # inter_lists = models.Left_name_data_lists.objects.get(id=u)
            # task_project_model_id = desk_models.task_project_model.objects.get(task_project_model_id = project_number)
            # print("task_project_model_id : %s" %task_project_model_id)
            inter_list = models.Req_list_data.objects.values().filter(of_big_model_id=project_number,
                                                                      of_big_on_small_model_id=u_id,
                                                                      of_big_on_small_model=u_name)
            print(inter_list)
            # print(inter_list)
        else:
            inter_list = models.Req_list_data.objects.values().filter(
                of_big_model_id=project_number).distinct()
            # inter_list = models.Req_list_data.objects.all()

    if request.method == "POST":
        # u = request.path()
        # print(u)
        # 左侧列表信息
        data = []
        left_list_name_data = ret_left_interface_listname()
        data.append(left_list_name_data)

        dat = json.loads(request.body)

        aga = dat["id"]
        # print("id是:%s" %aga)

        # inter_list = models.Req_list_data.objects.get(id=str(dat))
        inter_lists = models.Left_name_data_lists.objects.get(id=dat["id"])
        # print(inter_lists)
        inter_list = models.Req_list_data.objects.values().filter(
            data_list_name=inter_lists).distinct()
        # print(inter_list)

        # inter_list2 = models.Req_list_data.objects.get(data_list_name=inter_lists)
        # print(inter_list2)

    return render(request, "task_project_right_list.html", locals())
    # return render(request,"auto_interface_list_right.html",locals())
    # rse = {"success": inter_list}
    # return render_to_response("auto_interface_list_right.html",locals())


# 添加http接口
@csrf_exempt
def add_interface_add(request):
    if request.method == "POST":
        dat = json.loads(request.body)
        print(dat)

        para_url = dat["par_url"]
        print("para_url :%s" % para_url)
        para_url = para_url.rstrip("#")  # 去除后尾# 号
        print("para_url :%s" % para_url)
        prara_list = para_url.split("&")
        para_url_ = {}
        for lis in prara_list:
            li = lis.split("=")
            para_url_[li[0]] = li[1]
        print("para_url_ : %s" % para_url_)

        add_req_name = dat["add_req_name"]
        # add_id = dat["add_id"]
        if "ecdi" in para_url_.keys():
            add_id = para_url_["ecdi"]
        else:
            add_id = ""

        print("add_id : %s" % add_id)
        add_req_texts = dat["add_req_texts"]
        add_req_of = dat["add_req_of"]

        # 请求方法
        method = dat["method"]
        url = dat["url"]

        params = dat["data"]["Params"]
        # print(params.keys())
        if len(params) != 0:
            pass
        else:
            params = ""

        header = dat["data"]["tab_request_head"]
        if len(header) != 0:
            pass
        else:
            header = {}
        print("header : %s" % header)
        # form_data = dat["data"]["tab_request_head"]
        # print(dat["data"])
        # 判断body是哪个
        way_body = ''
        if "application_x_w" in dat["data"]["form_data"].keys():
            boy = dat["data"]["form_data"]["application_x_w"]
            way_body = 'application_x_w'

            if "Content-Type" in header.keys():
                print("header中有Content-Type")

            else:
                header["Content-Type"] = "application/x-www-form-urlencoded"
                print("header中没有Content-Type")
        elif 'form_data' in dat["data"]["form_data"].keys():
            way_body = 'form_data'
            boy = dat["data"]["form_data"]["form_data"]
            print("boy : %s" % boy)
        else:
            boy = ""
        # print()

        # print("boy是：%s" %boy)

        # if len(boy) != 0 and (len(boy) == 1 and '' not in boy.keys()):
        if boy:
            pass
        else:
            boy = ""
        print(" 验证： %s" % boy)

        #文件files
        # print(dat["files"])
        get_files = dat["data"]["files"]

        print(get_files)

        # 断言
        tab_req_assert = dat["tab_req_assert"]
        # print("tab_req_assert： %s" %tab_req_assert)

        try:
            # 哪个项目
            print("哪个项目")
            of_big_model_id = para_url_["project"]
            of_big_model = pro_name = desk_models.task_projects.objects.values("pro_name").get(id=of_big_model_id)[
                "pro_name"]

            # 哪个模块
            print("哪个模块")
            of_big_on_small_model_id = para_url_["small"].rstrip("#")
            of_big_on_small_model = \
                desk_models.task_project_model.objects.values("pro_name_model").get(id=of_big_on_small_model_id,
                                                                                    task_projects_id=of_big_model_id)[
                    "pro_name_model"]

            # 协议
            print("协议")
            agreement = "http"

            # print("发起访问")

            #
            if add_id == "" and add_req_of != "":
                print("----1-----")
                retd = models.Req_list_data.objects.create(name=add_req_name, req=method, url=url, params=params,
                                                           headers=header, body=boy, describe=add_req_texts,
                                                           file = get_files,
                                                           data_list_name=add_req_of,
                                                           of_big_model_id=of_big_model_id,
                                                           of_big_model=of_big_model,
                                                           of_big_on_small_model_id=of_big_on_small_model_id,
                                                           of_big_on_small_model=of_big_on_small_model,
                                                           agreement=agreement,
                                                           way_body=way_body
                                                           )
                ret_id = models.Req_list_data.objects.values('id').filter(url=url).order_by("-id")[0]["id"]

                succ = "添加成功"
                print("retd: %s" % ret_id)

                if way_body =="form_data":
                    for boy_dat in boy:
                        print(boy_dat)
                        models.req_body.objects.create(
                            req_body_id_id=ret_id,
                            keys=boy_dat["key"],
                            text_file=boy_dat["file_text"],
                            values=boy_dat["values"],
                            describe=''
                        )


                # 添加断言
                num = 1  # 判断断言右侧是否还需要填写值
                # if tab_req_assert:
                print("tab_req_assert : %s" %tab_req_assert)
                for data_ass in tab_req_assert:
                    # if data_ass[0] != "请选择" or (data_ass[1] != "" and data_ass[2] != ""):
                    ass_dat = models.autoin_asserts.objects.create(
                        Req_list_data_id_id=ret_id,
                        assert_name=data_ass[0],
                        lef_NO_num=1,
                        left_contrast=data_ass[1],
                        right_NO_num=num,
                        right_contrast=data_ass[2],
                        right_contrast_int=data_ass[3]
                    )
                    print("添加断言")

            elif add_id and add_req_of != "":
                print("-----2-----")
                print("修改 body :%s " % boy)
                print("修改 header :%s " % header)
                retd = models.Req_list_data.objects.filter(id=add_id).update(name=add_req_name, req=method, url=url,
                                                                             params=params,
                                                                             headers=header,
                                                                             body=boy,
                                                                             file=get_files,
                                                                             describe=add_req_texts,
                                                                             data_list_name=add_req_of,
                                                                             way_body=way_body)

                ret_id = add_id
                succ = "修改成功"
                if way_body == "form_data":
                    # 删除原来的body
                    body_data = models.req_body.objects.values().filter(req_body_id=add_id)
                    print("body_data: %s" % body_data)

                    if body_data.count() != 0:
                        print("进入判断")
                        models.req_body.objects.filter(req_body_id=add_id).delete()
                    for boy_dat in boy:
                        print(boy_dat)
                        models.req_body.objects.create(
                            req_body_id_id=ret_id,
                            keys=boy_dat["key"],
                            text_file=boy_dat["file_text"],
                            values=boy_dat["values"],
                            describe=''
                        )

                # 删除原来添加的断言
                data = models.autoin_asserts.objects.values().filter(Req_list_data_id_id=add_id)
                print("data: %s" % data)
                print(data == [])
                print(data.count() == '')
                print(data.count() == 0)
                if data:
                    print("进入判断1")
                    print(add_id)
                    delete_ass = models.autoin_asserts.objects.filter(Req_list_data_id_id=add_id).delete()
                    # print("删除之前关联的断言：%s" % delete_ass.count())

                # 添加新的断言
                num = 1  # 判断断言右侧是否还需要填写值

                # print(tab_req_assert)
                for data_ass in tab_req_assert:
                    # print("进入添加断言")
                    # if data_ass[0] != "请选择" and (data_ass[1] != "" and data_ass[2] != ""):
                    ass_dat = models.autoin_asserts.objects.create(
                        Req_list_data_id_id=ret_id,
                        assert_name=data_ass[0],
                        lef_NO_num=1,
                        left_contrast=data_ass[1],
                        right_NO_num=num,
                        right_contrast=data_ass[2],
                        right_contrast_int=data_ass[3]
                    )

                    print("添加新断言")

                # pass
                # print("检测")

            else:
                print("------3----")
                # pass
            # print(retd)
            # print("url: %s" %url)

            req_bodys = models.req_body.objects.values().filter(req_body_id_id=ret_id)
            boy = {}
            for req_bod in req_bodys:
                if req_bod["text_file"] == 'file':
                    pass
                else:
                    boy[req_bod["keys"]] = req_bod["values"]

            #文件 get_files
            get_file = []
            print(get_files)
            print("123456")
            print(type(get_files))
            if get_files:
                for file in get_files.keys():
                    get_file.append(("files",(file,open(os.path.join(BASE_DIR, file_save_path, file),"rb"))))
            else:
                get_file = ""
            print("get_file :%s" %get_file)

            # req_htm = interface_http().req_requests(method, url, params=params, data=boy, headers=header, files=get_file)
            # 调用http 请求
            print("ret_id : %s" % ret_id)

            # 断言访问 调试注释
            # run_word().run_reqerst_http(ret_id)
            get_req_data = run_word().run_reqerst_http(ret_id)
            print(" get_req_data : %s" % get_req_data)
            # print("req_htm: %s" %req_htm.content)

            if add_req_of == "":
                print("add_req_of 为空")
                ret = {"fail": "请选择接口类型"}
            else:
                print("-1-1-1-1-")
                req_htm = interface_http().req_requests(method,url,params=params, data=boy, headers=header,files=get_file)

                print("0")
                print(req_htm.text)
                # print(req_htm.content)
                # print(req_htm.headers)
                print("1")
                if req_htm.headers:
                    print("2")
                    header_data = req_htm.headers

                    print(header_data)
                else:
                    header_data = " "

                if req_htm.headers and 'gbk' in req_htm.headers["Content-Type"]:
                    ret = {"success": succ, "body": req_htm.content.decode('gbk'), "headers": "%s" % header_data,
                           "data_id": ret_id}  # .decode('utf-8'),"headers":req_htm.headers

                else:  # 'utf-8' in req_htm.headers["Content-Type"]:
                    ret = {"success": succ, "body": req_htm.content.decode('utf-8'), "headers": "%s" % header_data,
                           "data_id": ret_id}

                # 返回列表中加入断言访问情况
                # 断言访问 调试注释

                if get_req_data:
                    print("-1-1-")
                    ret["get_req_data"] = get_req_data

            # print(ret)

            # data = req_htm.content.decode('utf-8')
            # print(req_htm.json().decode('utf-8'))

        except BaseException as ex:
            print("进入错误")
            print(ex)
            ret = {"fail": "%s" % ex}

        # print(boy)
        # success

    return HttpResponse(json.dumps(ret))  # json.dumps(ret)


# http接口断言
@csrf_exempt
def req_assert(request):
    Ver_cook = Ver_cook_vr(request)
    print(Ver_cook)
    if Ver_cook:

        print("进入任务")

        if request.method == "POST":
            dat = json.loads(request.body)
            print("dat:%s" % dat)

            # 删除原来添加的断言
            data = models.autoin_asserts.objects.values().filter(Req_list_data_id=dat["add_id"])
            print("data: %s" % data)
            if data.count() != 0:
                print("进入判断")
                delete_ass = models.autoin_asserts.objects.filter(Req_list_data_id_id=dat["add_id"]).delete()

            num = 1
            for tab_req_assert_list in dat["tab_req_assert"]:
                print(tab_req_assert_list)
                print(tab_req_assert_list[1])
                if tab_req_assert_list[0] != "请选择" and (tab_req_assert_list[1] != "" and tab_req_assert_list[2] != ""):
                    ass_dat = models.autoin_asserts.objects.create(
                        Req_list_data_id_id=dat["add_id"],
                        assert_name=tab_req_assert_list[0],
                        lef_NO_num=1,
                        left_contrast=tab_req_assert_list[1],
                        right_NO_num=num,
                        right_contrast=tab_req_assert_list[2],
                        right_contrast_int=tab_req_assert_list[3]
                    )

            # 断言验证
            get_req_data = run_word().run_reqerst_http(dat["add_id"])
            print("get_req_data： %s" % get_req_data)
            print("dat[add_id]： %s" % dat["add_id"])

        if request.method == "GET":
            pass
        ret = {"success": "添加成功", "data": get_req_data}
        return HttpResponse(json.dumps(ret))
        # task_pro = models.task_projects.objects.all()
        # return render(request, "task_projects.html", locals())
    else:
        return HttpResponseRedirect(request.POST.get('next', '/') or '/')

    pass


# 运行接口 interface，运行选择的任务
@csrf_exempt
def run_interfaces(request):

    # 验证
    Ver_cook = Ver_cook_vr(request)
    user = [Ver_cook["user_id"], Ver_cook["user_name"]]
    user_ = Ver_cook["user_name"]
    user_Id = Ver_cook["user_id"]
    user_login = Ver_cook["user_login_name"]

    print("run_interface")
    if request.method == "POST":
        dat = json.loads(request.body)

        print("这是运行任务 %s" % dat)
        i = 0
        for lis in dat["work_run_lists"]:
            i += 1
            run_lis.append([[str(i), lis]])
        # 毫秒
        ms_f = time.time()
        ms = int((ms_f - int(ms_f)) * 1000)

        t_name = time.strftime("%Y-%m-%d_%H%M%S", time.localtime()) + "." + str(ms)
        # t_name = t_name + "." + str(ms)

        run_work_name = user_login
        run_work_fullname = user_

        # print("run_work_name %s" % run_work_name)
        # print("run_work_fullname %s" % run_work_fullname)
        #
        work_run_list = ""
        if dat["work_run_lists"][0]:
            work_run_lists = models.Req_list_data.objects.values("of_big_model").get(id=dat["work_run_lists"][0])
            work_run_list = work_run_lists["of_big_model"]
            # print("work_run_lists %s" %work_run_lists)
        desk_models.work_historys.objects.create(
            execute_sign=t_name,  # 执行标记--执行时的名字
            run_work_name=run_work_name,  # 执行人登录名
            run_work_fullname=run_work_fullname,  # 执行人名字
            task_module = work_run_list,
            task_name='start_',  # 标记 和 用例id
            task_state='0',  # 任务状态，是否执行成功   0默认未执行
            states='0',  # 是否执行，控制执行  0执行 ，1不执行
            execute_situation=''  # 执行报告或情况
        )
        for run_id in dat["work_run_lists"]:
            desk_models.work_historys.objects.create(
                execute_sign=t_name,  # 执行标记--执行时的名字
                run_work_name=run_work_name,  # 执行人登录名
                run_work_fullname=run_work_fullname,  # 执行人名字
                task_name=run_id,  # 标记 和 用例id
                req_id_id=run_id,
                task_state='',  # 任务状态，是否执行成功 0默认未执行
                states='0',  # 是否执行，控制执行 0执行 ，1不执行
                execute_situation=''  # 执行报告或情况
            )

        # 应提供该任务是谁的，执行哪些任务
        mul_run_word().run_reqerst_http(dat["work_run_lists"], t_name)
        # run_word().run_word_interf(dat["work_run_lists"], t_name)
        # run_word().run_reqerst_http(dat["work_run_lists"])

        # u1 = run_word().run_word_interf()
        # print("u: %s" %u)
        # print("u: %s" %u)
    ret = {"success": "已执行，详见运行任务"}
    return HttpResponse(json.dumps(ret))


# 删除
@csrf_exempt
def req_list_deletes(request):
    if request.method == "POST":
        data = json.loads(request.body)
        d_id = data["id"]
        print(data)
        reqrun = models.Req_list_data.objects.filter(id=d_id).delete()
        print(reqrun)
        print(d_id)
        ret = {"success": "删除成功"}

    return HttpResponse(json.dumps(ret))


def req_list_updates(request):
    ret = {"fail": "功能暂未实现"}

    return HttpResponse(json.dumps(ret))
