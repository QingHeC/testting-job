# coding:utf-8

import requests
import unittest
import sys, time, json, os
# from nose_parameterized import parameterized as paramed
from parameterized import parameterized
# import nose_parameterized
from auto_interface.api_auto.lib.central_controls import central_control
from auto_interface.api_auto.configs.config import basedir, run_lis
from auto_interface.api_auto.lib import HTMLTestRunner
from BeautifulReport import BeautifulReport as bfr
from auto_interface.api_auto.lib.interface_http import interface_http
from auto_interface import models
from desk_center import models as desk_models

from test_project.settings import BASE_DIR
from auto_interface.api_auto.configs.config import run_lis, file_save_path

import copy

# import paramunittest
run_name = ''  # 执行名字
run_work_lis = []
interfase_run_listid = []


# zp = [
#     ["1", "23"],
#     ["2", "24"]
# ]

class Testinterfexec(unittest.TestCase):
    # @parameterized.expand(copy.copy(run_lis))
    def test_interfac(self):

        # Testinterfexec.__class__.__name__ = 'q123'
        print("interfase_run_listid:  %s" % interfase_run_listid)
        task_i = models.Req_list_data.objects.values().filter(id__in=interfase_run_listid)[0]
        print("task_i ：%s" % task_i)
        # task_i = models.Req_list_data.objects.values().filter(id=task1)[0]
        # print(task_i)
        t = interface_http().req_requests(task_i["req"],
                                          task_i["url"],
                                          params=task_i["params"],
                                          headers=task_i["headers"]
                                          )

        autoin_assert_lists = models.autoin_asserts.objects.values().filter(Req_list_data_id=task_i["id"])
        print("autoin_assert_lists :%s" % autoin_assert_lists)
        # getattr(self, "assertEqual")(t.json()["headers"], {'Accept-Encoding': 'identity', 'Content-Length': '0', 'Host': 'httpbin.org'})
        # print("T : %s" % (t.json()["headers"]))
        if autoin_assert_lists.count() != 0:
            print("进入断言")
            for autoin_assert_list in autoin_assert_lists:
                print(" autoin_assert_list ： %s" % autoin_assert_list)
                if autoin_assert_list["right_contrast_int"] == '':
                    fp = getattr(self, autoin_assert_list["assert_name"])(
                        getattr(t, autoin_assert_list["left_contrast"]), autoin_assert_list["right_contrast"])

                elif autoin_assert_list["right_contrast_int"] == 'int':
                    print("int 判断")
                    print(getattr(t, autoin_assert_list["left_contrast"]))
                    print(int(autoin_assert_list["right_contrast"]))
                    fp = getattr(self, autoin_assert_list["assert_name"])(
                        getattr(t, autoin_assert_list["left_contrast"]), int(autoin_assert_list["right_contrast"]))

                elif autoin_assert_list["right_contrast_int"] == 'json':
                    # getattr(self, "assertEqual")(t.json()["headers"],
                    #                              {'Accept-Encoding': 'identity', 'Content-Length': '0',
                    #                               'Host': 'httpbin.org'})
                    print("json 判断")
                    dat_json1 = json.loads(autoin_assert_list["right_contrast"])
                    print(type(dat_json1))
                    # print(type(t.json()["headers"]))
                    # print(dat_json1)
                    # 解决 获取字符串json() 不认识的问题 方法eval
                    fp = getattr(self, autoin_assert_list["assert_name"])(
                        eval("t." + autoin_assert_list["left_contrast"]),
                        dat_json1)


                elif autoin_assert_list["right_contrast_int"] == 'str':
                    fp = getattr(self, autoin_assert_list["assert_name"])(
                        getattr(t, autoin_assert_list["left_contrast"]), str(autoin_assert_list["right_contrast"]))
                else:
                    fp = getattr(self, autoin_assert_list["assert_name"])(
                        eval("t." + autoin_assert_list["left_contrast"]), autoin_assert_list["right_contrast"])
                print("fp: %s" % unittest.TextTestRunner.failfast)
                print("fp: %s" % unittest.failures)

    # @unittest.skip
    # def test_1(self):
    #     # setattr(self.__class__,'test_2', self.test_1)
    #
    #
    #
    #     # print(sys._getframe(0).f_code.co_name)
    #     # print(self.__delattr__())
    #
    #
    #     t = requests.get("https://www.baidu.com/")
    #     print(t.content.decode())
    def itest_(self):
        # print(run_name)
        print("run_name :%s" % run_name)
        # print(id)
        print("运行的任务：%s" % interfase_run_listid)
        task1 = models.Req_list_data.objects.values().filter(id__in=interfase_run_listid)

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
        errors = self._outcome.errors
        for test, exc_info in errors:
            if exc_info:
                # dosomething
                pass


class run_word():
    def run_reqerst_http(self, run_request_id):
        """ http请求"""
        print("run_request_id: %s" % run_request_id)
        global run_name
        global run_work_lis
        run_work_lis = []
        control_num = 1

        global interfase_run_listid
        interfase_run_listid = run_request_id
        if control_num:
            control_num = 0
            # global run_name
            # run_name = t_name

            run_work_lis = run_request_id
        units = unittest.TestSuite()
        units.addTest(Testinterfexec("itest_"))
        ht = unittest.TextTestRunner(verbosity=2).run(units)
        print("----------")
        print("ht %s: " % ht.errors)
        # print(ht.startTestRun)

        # print(ht.failures)
        # print("运行数量：%s" %(ht.testsRun))
        # print("1----1-----1")
        # if ht.testsRun:
        #     print("运行数量：")
        #     print(ht.testsRun)
        # print(ht.failures[0][1].split("getattr")[-1])
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

        return ret_resu

    def run_word_interf(self, sum_id, t_name):
        # 此用法可以同时测试多个类
        # for i in range(1,3):
        # print(i)
        # suite1 = unittest.TestLoader().loadTestsFromTestCase(interf_exec)
        # suite = unittest.TestSuite([suite1])
        #
        # unittest.TextTestRunner(verbosity=1).run(suite)
        #
        # if __name__ == '__main__':
        #
        #     unittest.main()
        # unittest.main()
        # global run_work_lis
        global interfase_run_listid
        interfase_run_listid = sum_id
        # run_word().read_liss()
        print("run_work_lis :: %s" % run_work_lis)
        print(__name__)
        print("sum_id: %s" % sum_id)
        global run_name

        control_num = 1
        # if control_num:
        #     control_num = 0
        global run_name
        run_name = t_name
        # run_work_lis.append(sum_id)_

        # print(run_work_lis)
        # unittest.main()

        # testunit = unittest.TestSuite(Testinterfexec)
        # print('0')
        # testunit.addTest(Testinterfexec("test_interfac"),param=2)
        print("1")
        # t_name = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
        t_name = t_name + '.html'
        # filename = './reports/' + now + 'result.html'
        # file = basedir + '\\reports\\' + t_name
        file = basedir + '\\reports\\'
        print("这是文件；路径：")
        print(file)

        # runht = bfr(testunit)
        runht = bfr(unittest.makeSuite(Testinterfexec, "test_interfac"))
        # runht = bfr(unittest.makeSuite(Testinterfexec, "test_interfac"))
        runht.report(description="执行接口", filename=t_name, report_dir=file)
        # fp = open(file, "wb+")
        # runner = HTMLTestRunner.HTMLTestRunner(
        #     stream=fp,
        #     title="test",
        #     description="ccc"
        # )
        # ru = runner.run(testunit)
        # print("ru: %s" % ru)
        # print("ru_: %s" % t_name)
        # fp.close()
        desk_models.work_historys.objects.filter(
            execute_sign=run_name,  # 执行标记--执行时的名字
            task_name='start_',  # 标记 和 用例id
        ).update(
            execute_situation=t_name,  # 执行报告名字
            execute_situation_path=file  # 执行报告或情况
        )


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
