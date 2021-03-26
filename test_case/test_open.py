from common.session import SendMethodEntity
from common.config.config import Config


class TestOpen:

    def __init__(self):
        self.config = Config()
        self.url = self.config.get_conf('url')
        print(self.config.get_conf('url'))
        self.method = "post"

    def test_open_service(self, data):
        response = SendMethodEntity.send_method(self.method, self.url, data=data)
        return response

if __name__ == '__main__':
    TestOpen()