from common.session import SendMethodEntity
from common.config.config import Config
from test_case.test_get_task import GetTask


class TestOpen:

    def __init__(self):
        self.config = Config()
        self.url = self.config.get_conf('url') + "api/task/open-server"

    def test_open_gong(self, data):
        # 开公共区
        response = SendMethodEntity.send_method("post", self.url, data=data)
        task_id = response["data"]["taskIds"][0]
        GetTask.test_code(task_id)
        return response

    def test_open_pu(self, data):
        # 开普通区
        response = SendMethodEntity.send_method("post", self.url, data=data)
        task_id = response["data"]["taskIds"][0]
        GetTask.test_code(task_id)
        return response

    # def test_open_pu2(self, data):
    #     # 开普通二区
    #     response = SendMethodEntity.send_method("post", self.url, data=data)
    #     return response["data"]["taskIds"][0]


if __name__ == '__main__':
    TestOpen()
