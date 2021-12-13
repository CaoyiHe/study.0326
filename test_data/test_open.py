from test_case.test_open import TestOpen
import datetime
from common.config.config import Config
from common.session import SendMethod
from test_case.test_get_task import GetTask
import time
from datetime import timedelta
import _thread
import threading


class OpenService(Config):
    def __init__(self):
        super().__init__()
        # self.code = -1
        self.open = TestOpen()
        # self.config = Config()
        # self.worldId_gong = int(self.config.get_conf("worldId_gong"))
        # self.worldId_pu1 = int(self.config.get_conf("worldId_pu1"))
        # self.worldId_pu2 = int(self.config.get_conf("worldId_pu2"))
        # self.areaId = int(self.config.get_conf("areaId"))
        # self.versionId = int(self.config.get_conf("versionId"))
        self.time =(datetime.datetime.utcnow() + timedelta(hours=0.005)).isoformat() + 'Z'

    def test_open_gong(self):
        # 远征2开公共区

        data = {
            "areaId": self.area_id,
            "groupId": 1,
            "versionId": None,
            "paramId": 4,
            "gameId": self.game_id,
            "regionId": self.region_id,
            "list": [
                {
                    "isPublic": 1,
                    "isAutoTest": 0,
                    "worldId": self.worldId_gong,
                    "executeTime": None,
                    "openTime": self.time,
                    "preCreateTime": None,
                    "specId": self.specsId_gong,   # K8S 改成43
                    "worldName": str(self.worldId_gong) + "-自动化-公共区",
                }
            ]
        }
        response = self.open.test_open_gong(data)
        return response

    def test_open_pu(self):
        # 远征2开普通区
        self.worldId_gong = str(self.worldId_gong)
        data1 = {
            "areaId": self.area_id,
            "groupId": 1,
            "versionId": None,
            "paramId": 4,
            "gameId": self.game_id,
            "regionId": self.region_id,
            "list": [
                {
                    "isPublic": 0,
                    "worldId": self.worldId_pu1,
                    "publicId": self.worldId_gong,
                    "executeTime": None,
                    "openTime": self.time,
                    "preCreateTime": None,
                    "specId": self.specsId_pu,   # K8S 改成60
                    "worldName": str(self.worldId_gong) + "-自动化-普通区-1"
                }
            ]
        }
        threads = []
        # task_id1 = self.open.test_open_pu(data1)
        time.sleep(1)
        data2 = {
            "areaId": self.area_id,
            "groupId": 1,
            "versionId": None,
            "paramId": 4,
            "gameId": self.game_id,
            "regionId": self.region_id,
            "list": [
                {
                    "isPublic": 0,
                    "worldId": self.worldId_pu2,
                    "publicId": self.worldId_gong,
                    "executeTime": None,
                    "openTime": self.time,
                    "preCreateTime": None,
                    "specId": self.specsId_pu,   # K8S 改成60
                    "worldName": str(self.worldId_gong) + "-自动化-普通区-2"
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

    def test_ss_open_gong(self):
        # 闪烁精灵开公共区
        data = {
            "areaId": self.area_id,
            "groupId": 1,
            "versionId": None,
            "gameId": self.game_id,
            "regionId": self.region_id,
            "list": [
                {
                    "isPublic": 1,
                    "worldId": self.worldId_gong,
                    "executeTime": None,
                    "openTime": self.time,
                    "preCreateTime": None,
                    "specId": 83,
                    "worldName": str(self.worldId_gong) + "-回归测试-公共区"
                }
            ]
        }
        response = self.open.test_open_gong(data)
        return response

    def test_ss_open_pu(self):
        # 闪烁精灵开普通区
        self.worldId_gong = str(self.worldId_gong)
        data1 = {
            "areaId": self.area_id,
            "groupId": 1,
            "versionId": None,
            "gameId": self.game_id,
            "regionId": self.region_id,
            "list": [
                {
                    "isPublic": 0,
                    "worldId": self.worldId_pu1,
                    "publicId": self.worldId_gong,
                    "executeTime": None,
                    "openTime": self.time,
                    "preCreateTime": None,
                    "specId": 82,
                    "worldName": str(self.worldId_gong) + "-回归测试-普通区-1"
                }
            ]
        }
        threads = []
        # task_id1 = self.open.test_open_pu(data1)
        time.sleep(1)
        data2 = {
            "areaId": self.area_id,
            "groupId": 1,
            "versionId": None if self.version_id == 'None' else self.version_id,
            "gameId": self.game_id,
            "regionId": self.region_id,
            "list": [
                {
                    "isPublic": 0,
                    "worldId": self.worldId_pu2,
                    "publicId": self.worldId_gong,
                    "executeTime": None,
                    "openTime": self.time,
                    "preCreateTime": None,
                    "specId": 82,
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


if __name__ == '__main__':
    test = OpenService()
    test.test_open_gong()


