

import json
import os
from config.conf import BASE_DIR
import yaml


class Assertation:
    @staticmethod
    def assert_status_code(response,expected_code):
        assert response.status_code == expected_code
class JsonUtil:
    @staticmethod
    def parse(json_string):
        """解析 JSON 字符串并返回字典"""
        try:
            return json.loads(json_string)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")

    @staticmethod
    def dump(obj):
        """将 Python 对象转换为 JSON 字符串"""
        try:
            return json.dumps(obj, ensure_ascii=False, indent=4)
        except TypeError as e:
            raise ValueError(f"Object cannot be serialized to JSON: {e}")

    @staticmethod
    def pretty_print(json_obj):
        """打印格式化的 JSON 字符串"""
        try:
            print(json.dumps(json_obj, ensure_ascii=False, indent=4))
        except TypeError as e:
            raise ValueError(f"Object cannot be pretty printed to JSON: {e}")

    @staticmethod
    def from_file(file_path):
        """从文件中读取并解析 JSON"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            raise ValueError(f"Error reading JSON from file: {e}")

    @staticmethod
    def to_file(obj, file_path):
        """将 Python 对象写入 JSON 文件"""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(obj, file, ensure_ascii=False, indent=4)
        except (TypeError, IOError) as e:
            raise ValueError(f"Error writing JSON to file: {e}")


import os
import yaml

import os
import yaml


class LoadData:
    @staticmethod
    def load_data_from_yml(filename=None):

        # 读取 YAML 文件并返回测试数据
        with open(filename, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)['test_case']


if __name__ == '__main__':
    yml = LoadData.load_data_from_yml(r"D:\python\apiauto\data\lease.yaml")

