from common.session import SendMethodEntity
from common.config.config import Config


class TestOpen:

    def __init__(self):
        self.config = Config()
        self.url = self.config.get_conf('url')
        # 获取请求默认值

    def test_open_service(self, data,):
        method = "post"
        Url = self.url + "api/task/open-server"
        # 查看拼接后的URL
        response = SendMethodEntity.send_method(method, Url, data=data)
        return response['code']

    def get_open_service(self, data, code):
        Url = self.url = "api/task/${code}/approve"
        response = SendMethodEntity.send_method("post", Url, data=data)
        return response


if __name__ == '__main__':
    TestOpen()
