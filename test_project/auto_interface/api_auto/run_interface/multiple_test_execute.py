# coding:utf-8

import requests
import unittest
import sys, time, json, os
# from nose_parameterized import parameterized as paramed
from parameterized import parameterized
# import nose_parameterized
from auto_interface.api_auto.lib.central_controls import central_control
from auto_interface.api_auto.configs.config import basedir ,run_lis ,file_save_path
from auto_interface.api_auto.lib import HTMLTestRunner
from BeautifulReport import BeautifulReport as bfr
from auto_interface.api_auto.lib.interface_http import interface_http
from auto_interface import models
from desk_center import models as desk_models

from test_project.settings import BASE_DIR
import copy

# import paramunittest
run_name = ''  # 执行名字
run_work_lis = []
interfase_run_listid = []


class Testinterfexec(unittest.TestCase):

    def itest_(self):
        # print(run_name)
        print("run_name :%s" %run_name)
        # print(id)
        print("运行的任务：%s" % run_work_lis)
        task1 = models.Req_list_data.objects.values().filter(id__in=run_work_lis)

        print("task : %s" % task1)

        for task_i in task1:
            print(task_i)
            get_files = task_i.file
            get_file = []

            if get_files:
                for file in get_files.keys():
                    get_file.append(("name", (file, open(os.path.join(BASE_DIR, file_save_path, file), "rb"))))
            else:
                get_file = ""
            way_body = task_i.way_body
            body_s = {}
            if "form_data" in way_body:

                req_bods = models.req_body.objects.values().filter(req_body_id_id=task_i.id)

                for bodys in req_bods:
                    body_s[bodys.keys] = bodys.values

            elif "application_x_w" in way_body:
                body_s = task_i.body
            else:
                pass

            # t = central_control().control_inter_http()
            t = interface_http().req_requests(task_i["req"], task_i["url"],
                                              params=task_i["params"],
                                              headers=task_i["headers"],
                                              data=body_s,
                                              files=get_file
                                              )

            autoin_assert_lists = models.autoin_asserts.objects.values("right_contrast_int",
                                                                       "assert_name",
                                                                       "left_contrast",
                                                                       "right_contrast").filter(
                Req_list_data_id=task_i["id"])
            print("autoin_assert_lists :%s" % autoin_assert_lists)
            # getattr(self, "assertEqual")(t.json()["headers"], {'Accept-Encoding': 'identity', 'Content-Length': '0', 'Host': 'httpbin.org'})
            # print("T : %s" % (t.json()["headers"]))
            if autoin_assert_lists.count() != 0:
                print("进入断言")
                for autoin_assert_list in autoin_assert_lists:
                    print(" autoin_assert_list ： %s" % autoin_assert_list)
                    if autoin_assert_list["right_contrast_int"] == '':
                        getattr(self, autoin_assert_list["assert_name"])(
                            getattr(t, autoin_assert_list["left_contrast"]), autoin_assert_list["right_contrast"])

                    elif autoin_assert_list["right_contrast_int"] == 'int':
                        print("int 判断")
                        getattr(self, autoin_assert_list["assert_name"])(
                            getattr(t, autoin_assert_list["left_contrast"]), int(autoin_assert_list["right_contrast"]))

                    elif autoin_assert_list["right_contrast_int"] == 'json':
                        print("json 判断")
                        dat_json1 = json.loads(autoin_assert_list["right_contrast"])
                        print(type(dat_json1))
                        # print(type(t.json()["headers"]))
                        # print(dat_json1)
                        # 解决 获取字符串json() 不认识的问题 方法eval
                        getattr(self, autoin_assert_list["assert_name"])(
                            eval("t." + autoin_assert_list["left_contrast"]), dat_json1)


                    elif autoin_assert_list["right_contrast_int"] == 'str':
                        getattr(self, autoin_assert_list["assert_name"])(
                            getattr(t, autoin_assert_list["left_contrast"]), str(autoin_assert_list["right_contrast"]))
                    else:
                        getattr(self, autoin_assert_list["assert_name"])(
                            eval("t." + autoin_assert_list["left_contrast"]), autoin_assert_list["right_contrast"])

                    # getattr(self,autoin_assert_list["assert_name"])(getattr(t,autoin_assert_list["left_contrast"]),autoin_assert_list["right_contrast"])
            # getattr(self, "assertEqual")(t.status_code, 200)
            # getattr(self, "assertEqual")(t.title, 200)
            # getattr(self, "assertEqual")(t.content, 200)
            # r= self.asserteq(t.status_code,200)
            # print("r: %s" %r)
            # print(self.asserteq(t.status_code,201))
        # t = requests.get("https://www.baidu.com/")
        #     getattr(self, "assertEqual")(t.status_code,200)
        # self.assertEqual(t.status_code,200)
        # self.assertEqual(t.status_code,t["id"])
        # print(t.content.decode())

    def setUp(self):

        pass

    def tearDown(self):
        # errors = self._outcome.errors
        # for test, exc_info in errors:
        #     if exc_info:
                # dosomething
        pass


class mul_run_word():
    def run_reqerst_http(self, run_request_id,t_name):
        """ http请求"""
        print("run_request_id: %s" %run_request_id)
        global run_name
        global run_work_lis
        run_work_lis = []
        control_num = 1
        if control_num:
            control_num = 0
            global run_name
            run_name = t_name
            for run_id in run_request_id:
                print(run_id)
                run_work_lis = run_id
                units = unittest.TestSuite()
                units.addTest(Testinterfexec("itest_"))
                ht = unittest.TextTestRunner(verbosity=2).run(units)
                print("----------")
                print("ht %s: " %ht.errors)
                ret_resu = {}
                if ht.failures:
                    print("这是错误0: %s---" % (ht.failures[0][1].split("getattr")[-1]))
                    ret_resu["ret_resu"] = "Fail"
                    ret_resu["result"] = ht.failures[0][1].split("getattr")[-1]
                    # ret_resu = ht.failures[0][1].split("getattr")[-1]
                    # print(ht.failures[0][1].split("getattr")[-1])
                    # print("=============")
                elif ht.errors:
                    ret_resu["ret_resu"] = "Error"
                    ret_resu["result"] = ht.errors[0][1].split("getattr")[-1]
                    # ret_resu = ht.errors[0][1].split("getattr")[-1]
                    print("这是错误:%s ---" % (ht.errors[0][1].split("getattr")[-1]))
                    # print(ht.errors)
                else:
                    ret_resu["ret_resu"] = "OK"
                    ret_resu["result"] = ""
                    # ret_resu = "OK"
                print(ret_resu)

                print("这是： %s" % ht.stream)
                # if ht.printErrors:
                #     print("这是错误2:%s" %(ht.printErrors.printErrorList))
                #     print(ht.printErrors.printErrorList)
                # print(ht.printErrors.printErrorList)
                # print(ht.printErrors)
                # print(ht.printErrors())
                # print(ht.stream)
                # print("--------")
                # print(ht.startTestRun)
                # print(ht.buffer)
                desk_models.work_historys.objects.filter(
                    execute_sign = t_name,
                    task_name = run_id,
                ).update(
                    task_state = ret_resu["ret_resu"],
                    execute_situation = ret_resu["result"]
                )
                # return ret_resu




if __name__ == "__main__":
    # unittest.main()
    # run_word().run_word_interf()
    run_word().run_reqerst_http("2")
    # run_word().run_word_interf()

    # suite1 = unittest.TestLoader().loadTestsFromTestCase(interf_exec)
    # suite = unittest.TestSuite([suite1])
    #
    # unittest.TextTestRunner(verbosity=1).run(suite)
    # if __name__ == '__main__':
    #     unittest.main()
