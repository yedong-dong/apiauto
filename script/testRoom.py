"""
@File    : testRoom
@Time    : 2024/12/21 上午10:02
@Author  : 86182
"""
import pytest

from common.loadDataUtil import LoadData
from common.loggerUtil import logger
from common.loginUtils import getCookie
from config.ENV import BASE_DIR
from common.requestClient import APIClient


class TestLease:

    @pytest.fixture(scope="class")
    def base_api(self):
        """Fixture to initialize API client."""
        client = APIClient("http://localhost:8080/")
        yield client
        # 可在此添加清理工作，例如关闭连接等（如果需要）

    yml = LoadData.load_data_from_yml(rf'{BASE_DIR}\data\room.yaml')
    @pytest.mark.parametrize('roomcase', yml, ids=[case['id'] for case in yml])
    def test_lease_true(self, base_api, roomcase):
        """根据 YAML 文件中的数据执行 API 测试"""
        url = roomcase['url']
        method = roomcase['method']
        headers = roomcase['headers']
        headers['access-token']=getCookie()
        params = roomcase['params']
        expected_status_code = roomcase['response']['expected_status_code']

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
        print(response.json())
        print(response.status_code)
        logger.info(response.json())
        assert response.json()['code']==expected_status_code

