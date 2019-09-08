# -*- coding: utf-8 -*-
import unittest

from auto_interface.api_auto.lib.interface_http import interface_http
# from auto_interface import models
import json

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='test_', run_work_lis=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.run_work_lis = run_work_lis

    @staticmethod
    def parametrize(testcase_klass , defName=None, run_work_lis=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        # for i in param:
        #     setattr(TestOne, 'test_something_%s' % (i[0]),
        #             TestOne.test_something(*i))

        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        run_work_lis = run_work_lis
        print(run_work_lis)
        if defName != None:
            for name in testnames:
                if name == defName:
                    # setattr(TestOne, 'test_something_%s' % (param[0]),TestOne.test_something(param))
                    suite.addTest(testcase_klass(name, run_work_lis=run_work_lis))
        else:
            for name in testnames:
                # setattr(TestOne, 'test_something_%s' % (param[0]), TestOne.itest_(param))
                suite.addTest(testcase_klass(name, run_work_lis=run_work_lis))
        return suite



#用法-testcase
class TestOne(ParametrizedTestCase):
    def itest_(self):
        # print(run_name)
        print(self.run_work_lis)
        # print(id)
        print("运行的任务：%s" % self.run_work_lis)
        # task1 = models.Req_list_data.objects.values().filter(id__in=self.run_work_lis)
        #
        # print("task : %s" % task1)
        #
        # for task_i in task1:
        #     print(task_i)
        #     # t = central_control().control_inter_http()
        #     t = interface_http().req_requests(task_i["req"], task_i["url"],
        #                                       params=task_i["params"],
        #                                       headers=task_i["headers"])
        #
        #     autoin_assert_lists = models.autoin_asserts.objects.values("right_contrast_int",
        #                                                                "assert_name",
        #                                                                "left_contrast",
        #                                                                "right_contrast").filter(
        #         Req_list_data_id=task_i["id"])
        #     print("autoin_assert_lists :%s" % autoin_assert_lists)
        #     # getattr(self, "assertEqual")(t.json()["headers"], {'Accept-Encoding': 'identity', 'Content-Length': '0', 'Host': 'httpbin.org'})
        #     print("T : %s" % (t.json()["headers"]))
        #     if autoin_assert_lists.count() != 0:
        #         print("进入断言")
        #         for autoin_assert_list in autoin_assert_lists:
        #             print(" autoin_assert_list ： %s" % autoin_assert_list)
        #             if autoin_assert_list["right_contrast_int"] == '':
        #                 getattr(self, autoin_assert_list["assert_name"])(
        #                     getattr(t, autoin_assert_list["left_contrast"]), autoin_assert_list["right_contrast"])
        #
        #             elif autoin_assert_list["right_contrast_int"] == 'int':
        #                 print("int 判断")
        #                 getattr(self, autoin_assert_list["assert_name"])(
        #                     getattr(t, autoin_assert_list["left_contrast"]), int(autoin_assert_list["right_contrast"]))
        #
        #             elif autoin_assert_list["right_contrast_int"] == 'json':
        #                 print("json 判断")
        #                 dat_json1 = json.loads(autoin_assert_list["right_contrast"])
        #                 print(type(dat_json1))
        #                 # print(type(t.json()["headers"]))
        #                 # print(dat_json1)
        #                 # 解决 获取字符串json() 不认识的问题 方法eval
        #                 getattr(self, autoin_assert_list["assert_name"])(
        #                     eval("t." + autoin_assert_list["left_contrast"]), dat_json1)
        #
        #
        #             elif autoin_assert_list["right_contrast_int"] == 'str':
        #                 getattr(self, autoin_assert_list["assert_name"])(
        #                     getattr(t, autoin_assert_list["left_contrast"]), str(autoin_assert_list["right_contrast"]))
        #             else:
        #                 getattr(self, autoin_assert_list["assert_name"])(
        #                     eval("t." + autoin_assert_list["left_contrast"]), autoin_assert_list["right_contrast"])

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




# 在这里可以定义循环次数以及其他内容



# test_func_%s_%s 这里用来定义testcase名称


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(ParametrizedTestCase.test_something)
    suite.addTest(ParametrizedTestCase.parametrize(TestOne,"itest_", run_work_lis=["1","2"]))
    # suite.addTest(ParametrizedTestCase.parametrize(TestOne,"test_something_3", run_work_lis=["3","4"]))
    unittest.TextTestRunner(verbosity=2).run(suite)
