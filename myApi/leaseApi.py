"""
@File    : testLease
@Time    : 2024/12/17 下午7:29
@Author  : 86182
"""

from common.requestClient import APIClient
class LeaseApi(APIClient):
    def __init__(self,base_url="http://localhost:8080/"):
        super().__init__(base_url=base_url)

    def delete(self, endpoint, params=None, headers=None):
        return super().delete(endpoint, params, headers)

    def put(self, endpoint, json=None, headers=None):
        return super().put(endpoint, json, headers)

    def post(self, endpoint, json=None, headers=None):
        return super().post(endpoint, json, headers)

    def get(self, endpoint, params=None, headers=None):
        return super().get(endpoint, params, headers)



