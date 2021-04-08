# coding=gbk
from test_case.test_qifu import StartServer
from common.config.config import Config, Default_Config
from common.send_method import SendMethod
from test_case.test_get_task import GetTask
from datetime import timedelta
import datetime
import time


class Maintenance(Config):
    def __init__(self):
        super().__init__()
        self.qifu = StartServer()
        # self.config = Config()
        # self.worldId_gong = int(self.config.worldId_gong)
        # self.game_id = int(self.config.game_id)
        # self.region_id = self.config.region_id
        # self.worldId_pu1 = int(self.config.worldId_pu1)
        # self.worldId_pu2 = int(self.config.worldId_pu2)
        # self.area_id = int(self.config.get_conf("areaId"))
        # self.versionId = int(self.config.get_conf("versionId"))
        self.groupname = time.strftime("%m.%d %H:%M:%S")
        self.worldname_gong = str(self.worldId_gong) + "-回归测试-公共区"
        self.worldname_pu1 = str(self.worldId_gong) + "-回归测试-普通区-1"
        self.worldname_pu2 = str(self.worldId_gong) + "-回归测试-普通区-2"

    def test_maintenance_cq(self):
        # 例行重启
        data = {
            "gameId": self.game_id,
            "regionId": self.region_id,
            "types": "4",
            "startTime": datetime.datetime.utcnow().isoformat() + 'Z',
            "endTime": (datetime.datetime.utcnow() + timedelta(hours=0.5)).isoformat() + 'Z',
            "data": {
                "restart": [
                    {
                        "worldId": self.worldId_gong,
                        "worldName": self.worldname_gong,
                        "areaId": self.area_id,
                        "areaName": "自动化运维"
                    },
                    {
                        "worldId": self.worldId_pu1,
                        "worldName": self.worldname_pu1,
                        "areaId": self.area_id,
                        "areaName": "自动化运维"
                    },
                    {
                        "worldId": self.worldId_pu2,
                        "worldName": self.worldname_pu2,
                        "areaId": self.area_id,
                        "areaName": "自动化运维"
                    }
                ]
            },
            "countdown": 5,
            "openMode": 1
        }
        response = self.qifu.test_maintenance(data)
        return response

    def test_maintenance_gg(self):
        # 修改规格
        data = {
            "gameId": self.game_id,
            "regionId": self.region_id,
            "types": "5",
            "startTime": datetime.datetime.utcnow().isoformat() + 'Z',
            "endTime": (datetime.datetime.utcnow() + timedelta(hours=0.5)).isoformat() + 'Z',
            "data": {
                "editSpecs": [
                    {
                        "specsId": 60,
                        "specsName": None,
                        "worldId": self.worldId_pu1,
                        "worldName": self.worldname_pu1,
                        "areaId": self.area_id,
                        "areaName": "自动化运维",
                        "groupIndex": 0
                    },
                    {
                        "specsId": 60,
                        "specsName": None,
                        "worldId": self.worldId_pu2,
                        "worldName": self.worldname_pu2,
                        "areaId": self.area_id,
                        "areaName": "自动化运维",
                        "groupIndex": 0
                    }
                ]
            },
            "countdown": 5,
            "openMode": 1
        }
        response = self.qifu.test_maintenance(data)
        return response

    def test_maintenance_bb(self):
        # 版本更新
        data = {
            "gameId": self.game_id,
            "regionId": self.region_id,
            "types": "1",
            "startTime": datetime.datetime.utcnow().isoformat() + 'Z',
            "endTime": (datetime.datetime.utcnow() + timedelta(hours=0.5)).isoformat() + 'Z',
            "data": {
                "versionUpdate": {
                    "areaId": self.area_id,
                    "gameWorldList": [
                        {
                            "worldId": self.worldId_gong,
                            "worldName": self.worldname_gong,
                            "areaId": self.area_id,
                            "areaName": "公共区"
                        },
                        {
                            "worldId": self.worldId_pu1,
                            "worldName": self.worldname_pu1,
                            "areaId": self.area_id,
                            "areaName": "普通区"
                        },
                        {
                            "worldId": self.worldId_pu2,
                            "worldName": self.worldname_pu2,
                            "areaId": self.area_id,
                            "areaName": "普通区"
                        }
                    ],
                    "version": self.version_id
                }
            },
            "countdown": 5,
            "openMode": 1
        }
        response = self.qifu.test_maintenance(data)
        return response

    def test_maintenance_hq_gx(self):
        # 合区+版本更新
        data = {
            "gameId": self.game_id,
            "regionId": self.region_id,
            "types": "1,2",
            "startTime": datetime.datetime.utcnow().isoformat() + 'Z',
            "endTime": (datetime.datetime.utcnow() + timedelta(hours=0.5)).isoformat() + 'Z',
            "data": {

                "versionUpdate": {
                    "areaId": None,
                    "version": self.version_id,
                    "gameWorldList": [
                        {
                            "worldId": self.worldId_gong,
                            "worldName": self.worldname_gong,
                            "areaId": self.area_id,
                            "areaName": "公共区"
                        },
                        {
                            "worldId": self.worldId_pu1,
                            "worldName": self.worldname_pu1,
                            "areaId": self.area_id,
                            "areaName": "普通区"
                        },
                        {
                            "worldId": self.worldId_pu2,
                            "worldName": self.worldname_pu2,
                            "areaId": self.area_id,
                            "areaName": "普通区"
                        }
                    ]
                },
                "mergeArea": [
                    {
                        "toWorldId": self.worldId_pu1,
                        "toPublicId": self.worldId_gong,
                        "fromWorldId": self.worldId_pu2,
                        "fromCountryId": 1,
                        "fromPublicId": self.worldId_gong,
                        "toCountryId": 1
                    },
                    {
                        "toWorldId": self.worldId_pu1,
                        "fromWorldId": self.worldId_pu2,
                        "fromCountryId": 2,
                        "toPublicId": self.worldId_gong,
                        "fromPublicId": self.worldId_gong,
                        "toCountryId": 2
                    }
                ]
            },
            "countdown": 5,
            "openMode": 1
        }
        response = self.qifu.test_maintenance(data)
        return response

    def test_maintenance_zh(self):
        # 大杂烩
        data = {
            "gameId": self.game_id,
            "regionId": self.region_id,
            "types": "1,2,3,5",
            "startTime": datetime.datetime.utcnow().isoformat() + 'Z',
            "endTime": (datetime.datetime.utcnow() + timedelta(hours=0.5)).isoformat() + 'Z',
            "data": {
                "versionUpdate": {
                    "areaId": None,
                    "gameWorldList": [
                        {
                            "worldId": self.worldId_pu1,
                            "worldName": self.worldname_pu1,
                            "areaId": self.area_id,
                            "areaName": "自动化运维"
                        }
                    ],
                    "version": self.version_id
                },
                "mergeArea": [
                    {
                        "toWorldId": self.worldId_pu1,
                        "toPublicId": self.worldId_gong,
                        "toCountryId": 1,
                        "fromWorldId": self.worldId_pu1,
                        "fromCountryId": 2,
                        "fromPublicId": self.worldId_gong
                    }
                ],
                "editName": [
                    {
                        "areaId": self.area_id,
                        "worldId": self.worldId_pu1,
                        "newName": self.worldname_pu1 + "-改名"
                    }
                ],
                "editSpecs": [
                    {
                        "specsId": 46,
                        "specsName": None,
                        "worldId": self.worldId_pu1,
                        "worldName": self.worldname_pu1,
                        "areaId": self.area_id,
                        "areaName": "自动化运维",
                        "groupIndex": 0
                    }
                ]
            },
            "countdown": 5,
            "openMode": 1
        }
        response = self.qifu.test_maintenance(data)
        return response

    def test_maintenance_gm(self):
        # 改名
        data = {
            "gameId": self.game_id,
            "regionId": self.region_id,
            "types": "3",
            "startTime": datetime.datetime.utcnow().isoformat() + 'Z',
            "endTime": (datetime.datetime.utcnow() + timedelta(hours=0.5)).isoformat() + 'Z',
            "data": {
                "editName": [
                    {
                        "areaId": self.area_id,
                        "worldId": self.worldId_pu1,
                        "newName": self.worldname_pu1 + "1"
                    }
                ]
            },
            "countdown": 5,
            "openMode": 1
        }
        response = self.qifu.test_maintenance(data)
        return response


if __name__ == '__main__':
    test = Maintenance()
    test.test_maintenance_cq()
