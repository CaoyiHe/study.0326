from test_case.test_qifu import StartServer
from common.config.config import Config
from common.send_method import SendMethod
from test_case.test_get_task import GetTask


class TestStart:
    def __init__(self):
        self.qifu = StartServer()
        self.config = Config()
        self.areaId = int(self.config.get_conf("areaId"))

    def test_qifu(self):
        data = {
            "rangeData": [
                {
                    "areaId": self.areaId,
                    "worlds": [
                        7319
                    ]
                }
            ],
            "extraIds": [],
            "gameId": 2117,
            "regionId": "TJZYY",
            "executeTime": None,
            "specId": None,
            "specName": None,
            "versionId": None,
            "versionName": None,
            "isFileupdate": 1
        }
        response = self.qifu.test_start(data)
        task_id = response["data"]["taskId"]
        return task_id

    def test_guanfu(self):
        data = {
            "rangeData": [
                {
                    "areaId": self.areaId,
                    "worlds": [
                        3752
                    ]
                }
            ],
            "extraIds": [],
            "gameId": 2117,
            "regionId": "TJZYY",
            "isForceKill": 1,
            "executeTime": None
        }
        response = self.qifu.test_guanfu(data)
        task_id = response["data"]["taskId"]
        return task_id


if __name__ == '__main__':
    task_id = TestStart().test_guanfu()
    GetTask.test_code(task_id)
