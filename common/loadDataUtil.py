"""
@File    : loadDataUtil
@Time    : 2024/12/17 下午7:13
@Author  : 86182
"""
import yaml


class LoadData:
    @staticmethod
    def load_data_from_yml(filename=None):
        # 读取 YAML 文件并返回测试数据
        with open(filename, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
