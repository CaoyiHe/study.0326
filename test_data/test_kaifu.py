from test_case.test_open import TestOpen
from common.session import SendMethod

from datetime import datetime

datetime.utcnow()
openTime = datetime.utcnow()
print(openTime)


class OpenService:
    def __init__(self):
        self.kaifu = TestOpen()
        self.openTime = datetime.utcnow()

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
                    "worldId": "7400",
                    "executeTime": "null",
                    "openTime": datetime.utcnow().timestamp(),
                    "preCreateTime": "null",
                    "specId": 43,
                    "worldName": "${date}-自动化-公共${__time(Hms,)}"
                }
            ]
        }
        response = self.kaifu.test_open_service(data)
        print(SendMethod.format_response(response))


if __name__ == '__main__':
    OpenService().test_service()
