"""
@File    : test01
@Time    : 2024/12/15 下午6:02
@Author  : 86182
"""
import pytest
import yaml
from myApi import api_client
from common.myUtils import Assertation

import yaml

import yaml

# 加载 YAML 文件
with open(r'D:\python\apiauto\data\lease.yaml', 'r') as file:
    config = yaml.safe_load(file)
print(config)



