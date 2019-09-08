#coding;utf-8
import unittest
# import paramunittest
from parameterized import parameterized
import time
from .lib import HTMLTestRunner
from BeautifulReport import BeautifulReport as bfr
def custom_name_func(testcase_func, param_num, param):
    return "%s_%s" %(
        testcase_func.__name__,
        parameterized.to_safe_name("_".join(str(x) for x in param.args)),
    )

dat = [["22"],["23"]]
# @paramunittest.parametrized(*zp)
class TestDemo(unittest.TestCase):
    # def setParameters(self, task_name):
    #     '''这里注意了，user, psw, result三个参数和前面定义的字典一一对应'''
    #     self.user = task_name

    @parameterized.expand([["1", 22], ["2", 23]], testcase_func_name=custom_name_func)
    def testinterf(self, name , dat):
    # def testcase(self):
        print("开始执行用例：--------------")
        time.sleep(0.5)
        print("输入用户名：%s" % dat)
        # print("输入密码：%s" % self.user)
        # print("期望结果：%s " % self.result)
        # time.sleep(0.5)
        # self.assertTrue(self.result == "true")


if __name__ == "__main__":
    # unittest.main(verbosity=2)
    testu = unittest.TestSuite()
    testu.addTest(TestDemo("testinterf"))
    t_name = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
    t_name = t_name + '.html'
    filename = "./reports/" + '1.html'
    file = t_name
    # print("这是文件；路径：")
    # print(file)
    fp = open("1.html", "wb+")
    runner = bfr(testu)
    runner.report(filename='te.html', description='这个描述参数是必填的',report_dir='d:/')
    # ru = runner.run(testunit)
    # fp.close()
