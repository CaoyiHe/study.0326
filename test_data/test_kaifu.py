from test_case.test_open import TestOpen
import datetime
from common.session import SendMethod
from test_case.test_get_task import GetTask


class OpenService:
    def __init__(self):
        self.code = -1
        self.kaifu = TestOpen()

    def test_service(self):
        data = {
            "areaId": 12,
            "groupId": 1,
            "versionId": 15,
            "paramId": 44,
            "gameId": 2117,
            "regionId": "TJZYY",
            "list": [
                {
                    "isPublic": 1,
                    "worldId": 3754,
                    "executeTime": None,
                    "openTime": datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat(),
                    "preCreateTime": None,
                    "specId": 43,
                    "worldName": "${date}-自动化-公共${__time(Hms,)}"
                }
            ]
        }
        response = self.kaifu.test_open_service(data)
        # print(type(SendMethod.format_response(response)))
        print(response['taskIds'])
        self.code = response['taskIds']
        return

    def test_get(self):
        data = {
            "remark": "接口执行通过",
            "status": 1
        }
        response = self.kaifu.get_open_service(data, self.code)


if __name__ == '__main__':
    test = OpenService()
    taskId = test.test_service()
    task = GetTask(taskId)
    task.test_check()
    task.test_task_particulars()
    test.test_get()
