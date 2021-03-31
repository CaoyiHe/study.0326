from test_case.test_qifu import StartServer
from common.config.config import Config
from common.send_method import SendMethod
from test_case.test_get_task import GetTask
import datetime
import time


class TestStart:
    def __init__(self):
        self.qifu = StartServer()
        self.config = Config()
        self.worldId_gong = int(self.config.get_conf("worldId_gong"))
        self.worldId_pu1 = int(self.config.get_conf("worldId_pu1"))
        self.worldId_pu2 = int(self.config.get_conf("worldId_pu2"))
        self.areaId = int(self.config.get_conf("areaId"))
        self.versionId = int(self.config.get_conf("versionId"))
        self.groupname = time.strftime("%m.%d %H:%M:%S")

    def test_serverlist_add(self):
        # serverlist修改完成后，对新区进行对外
        data = {
            "gameId": 2117,
            "regionId": "TJZYY",
            "areaId": None,
            "serverListId": 11,
            "data": [
                {
                    "opsType": 4,
                    "row": {
                        "name": self.groupname,
                        "channelId": 48,
                        "sort": 1
                    },
                    "info": {
                        "name": None
                    }
                }
            ],
            "opsType": 1
        }
        response = self.qifu.test_serverlist_add(data)
        grouplist = self.qifu.test_groupid(self.groupname)['data'][1]['groupList']
        group = next(x for x in grouplist if x['name'] == self.groupname)
        groupid = group["id"]
        data = {
            "rangeData": [
                {
                    "areaId": self.areaId,
                    "worlds": [
                        self.worldId_gong,
                        self.worldId_pu1,
                        self.worldId_pu2
                    ]
                }
            ],
            "extraIds": [],
            "gameId": 2117,
            "regionId": "TJZYY",
            "executeTime": None,
            "serverList": [
                {
                    "worldId": self.worldId_gong,
                    "channelId": 21,
                    "groupId": groupid,
                    "recommend": 1,
                    "channelName": "自动化测试",
                    "groupName": self.groupname,
                    "worldName": "自动化测试"
                },
                {
                    "worldId": self.worldId_pu2,
                    "channelId": 21,
                    "groupId": groupid,
                    "recommend": 1,
                    "channelName": "自动化测试",
                    "groupName": self.groupname,
                    "worldName": "自动化测试"
                }
            ]
        }
        response = self.qifu.test_foreign(data)
        return response

    def test_script(self):
        # 刷脚本
        data = {
            "range": 3,
            "rangeData": [
                {
                    "areaId": self.areaId,
                    "worlds": [
                        self.worldId_gong,
                        self.worldId_pu1,
                        self.worldId_pu2
                    ]
                }
            ],
            "gameId": 2117,
            "regionId": "TJZYY",
            "fileList": [
                {
                    "sort": 1,
                    "serverType": 3,
                    "repairFunction": "回归测试",
                    "fileName": "CreateRolesOpen(FixFunctionGuidePopWindowScript_2020_10_29.lua).lua",
                    "filePath": None,
                    "fileId": 64,
                    "restartRepair": 0,
                    "newRepair": 0,
                    "operationType": 1
                }
            ]
        }
        response = self.qifu.test_script(data)
        return response

    def test_stop(self):
        # 关服
        data = {
            "rangeData": [
                {
                    "areaId": self.areaId,
                    "worlds": [
                        self.worldId_gong,
                        self.worldId_pu1,
                        self.worldId_pu2
                    ]
                }
            ],
            "extraIds": [],
            "gameId": 2117,
            "regionId": "TJZYY",
            "isForceKill": 1,
            "executeTime": None
        }
        response = self.qifu.test_stop(data)
        return response

    def test_start(self):
        # 启服
        data = {
            "rangeData": [
                {
                    "areaId": self.areaId,
                    "worlds": [
                        self.worldId_gong,
                        self.worldId_pu1,
                        self.worldId_pu2
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
        return response

    def test_clear(self):
        # 新区清数据
        data = {
            "rangeData": [
                {
                    "areaId": self.areaId,
                    "worlds": [
                        self.worldId_pu1,
                        self.worldId_pu2
                    ]
                }
            ],
            "extraIds": [],
            "gameId": 2117,
            "regionId": "TJZYY",
            "clearTime": None,
            "isBook": 0,
            "preCreateTime": None,
            "openTime": datetime.datetime.utcnow().isoformat() + 'Z',
            "isForeign": 0,
            "foreignTime": None,
            "serverList": []
        }
        response = self.qifu.test_clear(data)
        return response

    def test_stop_operate(self):
        data = {
            "rangeData": [
                {
                    "areaId": self.areaId,
                    "worlds": [
                        self.worldId_gong,
                        self.worldId_pu1
                    ]
                }
            ],
            "extraIds": [],
            "gameId": 2117,
            "regionId": "TJZYY",
            "executeTime": None
        }
        response = self.qifu.test_stop_operate(data)
        worldId_gong = str(int(self.config.worldId_gong) + 1)
        print(worldId_gong)
        self.config.set_conf(self.config.WORLDID_GONG, worldId_gong)
        return response

        # def test_foreign(self):
        #     groupid = self.test_serverlist_add()
        #     data = {
        #         "rangeData": [
        #             {
        #                 "areaId": self.areaId,
        #                 "worlds": [
        #                     self.worldId_gong,
        #                     self.worldId_pu1,
        #                     self.worldId_pu2
        #                 ]
        #             }
        #         ],
        #         "extraIds": [],
        #         "gameId": 2117,
        #         "regionId": "TJZYY",
        #         "executeTime": None,
        #         "serverList": [
        #             {
        #                 "worldId": self.worldId_gong,
        #                 "channelId": 21,
        #                 "groupId": groupid,
        #                 "recommend": 1,
        #                 "channelName": "自动化测试",
        #                 "groupName": self.groupname,
        #                 "worldName": "自动化测试"
        #             },
        #             {
        #                 "worldId": self.worldId_pu2,
        #                 "channelId": 21,
        #                 "groupId": groupid,
        #                 "recommend": 1,
        #                 "channelName": "自动化测试",
        #                 "groupName": self.groupname,
        #                 "worldName": "自动化测试"
        #             }
        #         ]
        #     }
        #     response = self.qifu.test_foreign(data)
        #     return response


if __name__ == '__main__':
    test = TestStart()
    test.test_serverlist_add()
