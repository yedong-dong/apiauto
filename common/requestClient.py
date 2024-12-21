import requests


class APIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers if headers else {}

    def send_request(self, method, endpoint, params=None, json=None, headers=None):
        # 拼接完整的 URL
        url = self.base_url + endpoint
        # 发送 HTTP 请求
        return requests.request(method, url, params=params, json=json, headers={**self.headers, **(headers or {})})

    def get(self, endpoint, params=None, headers=None):
        return self.send_request('get', endpoint, params=params, headers=headers)

    def post(self, endpoint, json=None, headers=None):
        return self.send_request('post', endpoint, json=json, headers=headers)

    def put(self, endpoint, json=None, headers=None):
        return self.send_request('put', endpoint, json=json, headers=headers)

    def delete(self, endpoint, params=None, headers=None):
        return self.send_request('delete', endpoint, params=params, headers=headers)
