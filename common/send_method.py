"""
封装请求方式
"""
import requests
import json
from common.config.config import Config, Default_Config


class SendMethod:
    session = None

    def __init__(self, session):
        self.session = session

    def send_method(self, method, url, params=None, data=None, headers=None):
        """封装请求方式"""

        if headers is None:
            headers = {"gameId": Default_Config["gameId"], "regionId": Default_Config["regionId"]}
        if method == "get" or method == "delete":
            # 如果
            response = self.session.request(method=method, url=url, params=params, headers=headers)
        elif method == "post" or method == "put":
            # 或者如果
            response = self.session.request(method=method, url=url, json=data, headers=headers)
        else:
            # 否则
            print("请求方式不正确")
            response = None

        if method == "delete":
            return response.status_code
        else:
            try:
                # 确保下面的语句能够正确，执行这个
                return json.loads(response.text)
            except:
                # 当上面执行失败的时候，执行这个
                return response.text

    @staticmethod
    def format_response(response):
        """格式化返回数据"""
        return json.dumps(response, indent=2, ensure_ascii=False)

    def login(self):
        url = "http://autoops-auth.q1.com/api/login/ldap"
        data = {
            'userName': 'hecaoyi',
            'password': 'Hecaoyi520.'
        }
        s = self.session.post(url=url, json=data)
        return s
