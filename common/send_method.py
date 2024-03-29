"""
封装请求方式
"""
import requests
import json
from json import JSONDecodeError
from common.config.config import Config, Default_Config
# from common.config.config import Config
import logging
import getpass
logging.basicConfig(level='INFO', filename="G:\study\log\log.txt",
                    format='[%(asctime)s: %(levelname)s/%(filename)s:%(lineno)d] %(message)s')


class SendMethod:
    session = None

    def __init__(self, session):
        self.session = session
        self.config = Config()
        self.game_id = self.config.game_id
        self.region_id = self.config.region_id

    def send_method(self, method, url, params=None, data=None, headers=None, files=None):
        """封装请求方式"""

        if headers is None:
            # headers = {"gameId": Default_Config["gameId"], "regionId": Default_Config["regionId"]}
            headers = {"gameId": str(self.game_id), "regionId": self.region_id}
        if method == "get" or method == "delete":
            # 如果
            response = self.session.request(method=method, url=url, params=params, headers=headers, files=files)
        elif method == "post" or method == "put":
            # 或者如果
            response = self.session.request(method=method, url=url, json=data, headers=headers, files=files)
        else:
            # 否则
            print("请求方式不正确")
            response = None

        if method == "delete":
            return response.status_code
        else:
            try:
                # 确保下面的语句能够正确，执行这个
                response = json.loads(response.text)
                if response["code"] != 0:
                    raise ValueError(f"接口请求失败: {response['message']}")
                logging.info(response)
                return response
            except JSONDecodeError:
                # 当上面执行失败的时候，执行这个
                return response.text

    @staticmethod
    def format_response(response):
        """格式化返回数据"""
        return json.dumps(response, indent=2, ensure_ascii=False)

    def login_user(self):
        pass

    def login(self,):
        # username = input("请输入账号:")
        # password = input("请输入密码:")
        url = "http://autoops-auth.q1.com/api/login/ldap"
        data = {
            'userName': "hecaoyi",
            'password': "Hecaoyi520."
        }
        s = self.session.post(url=url, json=data)
        return s


if __name__ == '__main__':
    SendMethod(None).login()
