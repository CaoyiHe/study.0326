from common.session import SendMethodEntity
from common.config.config import Config


class StartServer:
    def __init__(self):
        self.config = Config()
        self.url = self.config.get_conf("url")

    def test_start(self, data):
        url = self.url + "api/task/start-game-world"
        response = SendMethodEntity.send_method("post", url, data=data)
        return response

    def test_guanfu(self, data):
        url = self.url + "api/task/close-game-world"
        response = SendMethodEntity.send_method("post", url, data=data)
        return response