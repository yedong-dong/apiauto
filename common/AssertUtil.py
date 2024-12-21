"""
@File    : AssertUtil
@Time    : 2024/12/17 下午7:12
@Author  : 86182
"""


class Assertation:
    @staticmethod
    def assert_status_code(response, expected_code):
        assert response.status_code == expected_code
