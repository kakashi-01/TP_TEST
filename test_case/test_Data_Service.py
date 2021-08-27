# -*- coding: utf-8 -*-
# @File : test_Data_Service.py
# _author_=feng
# date: 2021/1/22
import json
import allure
import pytest
from ..Lib.Function_Module.Data_Service import DataService
from ..tools.getYamlData import get_really_yamldata
# from ..tools.getExcelData import get_excelData
from ..tools.logBasic import logger
log = logger()

@allure.epic('TP系统')
@allure.feature('数据服务模块')
@allure.story('数据服务接口')
@allure.severity('critical')
@pytest.mark.Data_Service(order=4)
class TestDataService:
    # @pytest.mark.parametrize('inData,respData',get_yaml_data('../data/test_data.yml'))  # param
    # def setup_class(self):
    @pytest.mark.接口调用查询
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData',
                             [get_really_yamldata("test_data.yml", "接口调用查询")])
    # @pytest.mark.parametrize('inData,respData', get_excelData('4数据服务模块', 2, 2))
    def test_Interface_query(self, login_fixture, inData, respData):
        res = DataService(login_fixture).Interface_query(inData)
        log.info('------##############------------')
        try:
            assert str(res) == respData["code"]
            # assert str(res) == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    @pytest.mark.接口管理列表
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData',
                             [get_really_yamldata("test_data.yml", "接口管理列表")])
    # @pytest.mark.parametrize('inData,respData', get_excelData('4数据服务模块', 3, 3))
    def test_Interface_management(self, login_fixture, inData, respData):
        res = DataService(login_fixture).Interface_management(inData)
        log.info('------##############------------')
        try:
            assert str(res) == respData["code"]
            # assert str(res) == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err

    # @pytest.mark.接口停用
    # @allure.title("测试输入：{inData}")
    # @pytest.mark.parametrize('inData,respData',
    #                              [get_really_yamldata("test_data.yml", "接口停用")])
    # @pytest.mark.parametrize('inData,respData', get_excelData('4数据服务模块', 4, 4))
    # def test_Interface_disabled(self, login_fixture, inData, respData):
    #     res = DataService(login_fixture).Interface_disabled(inData)
    #     log.info('------##############------------')
    #     try:
    #         assert str(res) == json.loads(respData)["code"]
    #     except Exception as err:
    #         log.error(err)
    #         raise err

    @pytest.mark.查看接口授权
    @allure.title("测试输入：{inData}")
    @pytest.mark.parametrize('inData,respData',
                             [get_really_yamldata("test_data.yml", "查看授权接口")])
    # @pytest.mark.parametrize('inData,respData', get_excelData('4数据服务模块', 5, 5))
    def test_Interface_authorization(self, login_fixture, inData, respData):
        res = DataService(login_fixture).Interface_authorization(inData)
        log.info('------##############------------')
        try:
            assert str(res) == respData["code"]
            # assert str(res) == json.loads(respData)["code"]
        except Exception as err:
            log.error(err)
            raise err
