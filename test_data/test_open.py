from test_case.test_open import TestOpen
import datetime
from common.config.config import Config
from common.session import SendMethod
from test_case.test_get_task import GetTask
import time
import _thread
import threading


class OpenService:
    def __init__(self):
        self.code = -1
        self.open = TestOpen()
        self.config = Config()
        self.worldId_gong = int(self.config.get_conf("worldId_gong"))
        self.worldId_pu1 = int(self.config.get_conf("worldId_pu1"))
        self.worldId_pu2 = int(self.config.get_conf("worldId_pu2"))
        self.areaId = int(self.config.get_conf("areaId"))
        self.versionId = int(self.config.get_conf("versionId"))

    def test_open_gong(self):
        data = {
            "areaId": self.areaId,
            "groupId": 1,
            "versionId": self.versionId,
            "paramId": 44,
            "gameId": 2117,
            "regionId": "TJZYY",
            "list": [
                {
                    "isPublic": 1,
                    "worldId": self.worldId_gong,
                    "executeTime": None,
                    "openTime": datetime.datetime.utcnow().isoformat() + 'Z',
                    "preCreateTime": None,
                    "specId": 43,
                    "worldName": str(self.worldId_gong) + "-回归测试-公共区"
                }
            ]
        }
        response = self.open.test_open_gong(data)
        return response

    def test_open_pu(self):
        self.worldId_gong = str(self.worldId_gong)
        data1 = {
            "areaId": self.areaId,
            "groupId": 1,
            "versionId": self.versionId,
            "paramId": 4,
            "gameId": 2117,
            "regionId": "TJZYY",
            "list": [
                {
                    "isPublic": 0,
                    "worldId": self.worldId_pu1,
                    "publicId": self.worldId_gong,
                    "executeTime": None,
                    "openTime": datetime.datetime.utcnow().isoformat() + 'Z',
                    "preCreateTime": None,
                    "specId": 60,
                    "worldName": str(self.worldId_gong) + "-回归测试-普通区-1"
                }
            ]
        }
        threads = []
        # task_id1 = self.open.test_open_pu(data1)
        time.sleep(1)
        data2 = {
            "areaId": self.areaId,
            "groupId": 1,
            "versionId": self.versionId,
            "paramId": 4,
            "gameId": 2117,
            "regionId": "TJZYY",
            "list": [
                {
                    "isPublic": 0,
                    "worldId": self.worldId_pu2,
                    "publicId": self.worldId_gong,
                    "executeTime": None,
                    "openTime": datetime.datetime.utcnow().isoformat() + 'Z',
                    "preCreateTime": None,
                    "specId": 60,
                    "worldName": str(self.worldId_gong) + "-回归测试-普通区-2"
                }
            ]
        }
        t1 = threading.Thread(target=self.open.test_open_pu, args=(data1,))
        t2 = threading.Thread(target=self.open.test_open_pu, args=(data2,))
        threads.append(t1)
        threads.append(t2)
        for t in threads:
            t.start()
        for t in threads:
            t.join()

    # def test_open_pu2(self):
    #     self.worldId_gong = str(self.worldId_gong)
    #     data = dict(areaId=self.areaId, groupId=1, versionId=self.versionId, paramId=4, gameId=2117, regionId="TJZYY",
    #                 list=[
    #                     {
    #                         "isPublic": 0,
    #                         "worldId": self.worldId_pu2,
    #                         "publicId": self.worldId_gong,
    #                         "executeTime": None,
    #                         "openTime": datetime.datetime.utcnow().isoformat() + 'Z',
    #                         "preCreateTime": None,
    #                         "specId": 60,
    #                         "worldName": self.worldId_gong + "-自动化-公共" + time.strftime("%M:%S")
    #                     }
    #                 ])
    #     task_id = self.open.test_open_pu2(data)
    #     audit = GetTask(task_id)
    #     audit.test_check()
    #     audit.test_task_particulars()
    #     time.sleep(1)


if __name__ == '__main__':
    test = OpenService()
    test.test_open_pu()
