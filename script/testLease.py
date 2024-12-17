"""
@File    : testLease
@Time    : 2024/12/17 下午7:49
@Author  : 86182
"""
import pytest

import myApi
from common import requestClient
from common.loadDataUtil import LoadData

from myApi.leaseApi import LeaseApi
class TestLease:

    @pytest.fixture
    def base_api(self):
        """Fixture to initialize API client."""
        client = LeaseApi()
        yield client
        # 可在此添加清理工作，例如关闭连接等（如果需要）


    @pytest.mark.parametrize('test_case', LoadData.load_data_from_yml(r'D:\python\apiauto\data\lease.yaml'))
    def test_lease(self, base_api, test_case):
        """根据 YAML 文件中的数据执行 API 测试"""
        url = test_case['url']
        method = test_case['method']
        headers = test_case['headers']
        params = test_case['params']
        expected_status_code = test_case['expected_status_code']
        test_id = test_case['id']  # 获取 test_case 的 id

        # 打印当前测试用例 ID
        print(f"Running test case: {test_id}")

        # 根据方法类型决定使用 GET、POST、DELETE
        if method.upper() == "GET":
            response = base_api.get(url, params=params, headers=headers)
        elif method.upper() == "POST":
            response = base_api.post(url, json=params, headers=headers)
        elif method.upper() == "DELETE":
            response = base_api.delete(url, params=params, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")
        # 输出响应内容和状态码
        assert response.json()['code']==expected_status_code


