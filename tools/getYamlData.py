# -*- coding: utf-8 -*-
# @File : getYamlData.py
# _author_=feng
# date: 2021/5/18
# import yaml
#
# def get_yaml_data(fileDir):
#     '''
#     思路：原则：尽量少动代码
#         目标：函数的返回的结果与之前的excel方案数据一致
#         1- 获取什么数据
#             data
#             resp
#         2- 数据该如何组装返回
#             分析：框架pytest需要什么格式数据
#                 1- 列表格式 [(),()]
#                 2- 要求是字典格式：
#                     回顾：以前的读取excel的数据，记得在excel的函数里做了一步
#                     操作：json---转化---字典
#     :param fileDir:
#     :return: [(字典1，字典2),(字典1，字典2)]
#     '''
#     # 1-打开yaml文件
#     resList = []
#     fo = open(fileDir, 'r', encoding='utf-8')
#     # 2- 使用第三方库去获取
#     res = yaml.load(fo, Loader=yaml.FullLoader)  # 处理警告
#     for one in res:
#         resList.append((one['data'], one['resp']))
#     return resList

# if __name__ == '__main__':
#
#     print(get_yaml_data('../data/test_data.yml'))
#     # print(type(get_yaml_data('../data/test_data.yml')))

import os
import yaml


def get_yaml_data(yaml_path):
    """获取yaml文件数据"""
    f = open(yaml_path, "r", encoding="utf-8")
    yamldata = f.read()
    # print(yamlpath)

    # 把yaml文件数据转字典
    # d = yamldata
    d = yaml.load(yamldata)
    f.close()
    # print(d['test_info_params'])
    return d

def get_really_yamldata(dataname, data):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml_path = os.path.join(os.path.dirname(cur_path), "data",
                             dataname)  # F:\PythonProject\pytest_demo_api\test_data\uesrinfo_data.yml
    a = tuple(get_yaml_data(yaml_path)[data])
    return a

if __name__=='__main__':
    print([get_really_yamldata("test_data.yml","用户名正确，密码为空")])
    print(type([get_really_yamldata("test_data.yml","用户名正确，密码为空")]))

# if __name__ == '__main__':
#     cur_path = os.path.dirname(os.path.realpath(__file__))
#     print(cur_path)  # F:\PythonProject\pytest_demo_api\common
#     print(os.path.dirname(cur_path))  # F:\PythonProject\pytest_demo_api
#     yaml_path = os.path.join(os.path.dirname(cur_path), "data","test_data.yml")  # F:\PythonProject\pytest_demo_api\test_data\uesrinfo_data.yml
#     print(yaml_path)
#     # a = get_yaml_data(yaml_path)["login_data"]
#     a = tuple(get_yaml_data(yaml_path)["login_data"])
#     print([a])
#     print(type([a]))