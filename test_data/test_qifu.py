from test_case.test_qifu import StartServer
from common.config.config import Config
from common.send_method import SendMethod
from test_case.test_get_task import GetTask
import datetime
import time
from datetime import timedelta


class TestStart(Config):
    def __init__(self):
        super().__init__()
        self.qifu = StartServer()
        self.config = Config()
        self.worldId_gong = int(self.config.get_conf("worldId_gong"))
        self.worldId_pu1 = int(self.config.get_conf("worldId_pu1"))
        self.worldId_pu2 = int(self.config.get_conf("worldId_pu2"))
        self.areaId = int(self.config.get_conf("areaId"))
        self.versionId = int(self.config.get_conf("versionId"))
        self.groupname = time.strftime("%m.%d %H:%M:%S")
        self.time = (datetime.datetime.utcnow() + timedelta(hours=0.005)).isoformat() + 'Z'

    def test_serverlist_add(self):
        # serverlist修改完成后，对新区进行对外
        data = {
            "gameId": self.game_id,
            "regionId": self.region_id,
            "areaId": None,
            "serverListId": 11,
            "data": [
                {
                    "opsType": 4,
                    "row": {
                        "name": self.groupname,
                        "channelId": 99,
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
        time.sleep(2)
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
            "gameId": self.game_id,
            "regionId": self.region_id,
            "executeTime": self.time,
            "serverList": [
                {
                    "worldId": self.worldId_pu1,
                    "channelId": 21,
                    "groupId": groupid,
                    "recommend": 1,
                    "channelName": "自动化测试",
                    "groupName": self.groupname,
                    "worldName": str(self.worldId_pu1) + "-自动化-普通区-1"
                },
                {
                    "worldId": self.worldId_pu2,
                    "channelId": 21,
                    "groupId": groupid,
                    "recommend": 1,
                    "channelName": "自动化测试",
                    "groupName": self.groupname,
                    "worldName": str(self.worldId_pu2) + "-自动化-普通区-2"
                }
            ]
        }
        response = self.qifu.test_foreign(data)
        return response

    def test_foreign(self):
        # 对外
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
            "extraIds": [
            ],
            "gameId": self.game_id,
            "regionId": self.region_id,
            "executeTime": self.time,
            "serverList": [],
            "serverRecommend": [],
            "channelRecommend": {}
        }
        response = self.qifu.test_foreign(data)
        return response

    def test_script(self):
        # 刷脚本
        data = {
            "range": 3,
            "executeTime": None,
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
            "gameId": self.game_id,
            "regionId": self.region_id,
            "fileList": [
                {
                    "sort": 1,
                    "repairFunction": "测试",
                    "fileName": "[Social]RefreshKeyWords.lua",
                    "uid": "",
                    "fileId": 73,
                    "restartRepair": 0,
                    "newRepair": 0,
                    "operationType": 1,
                    "serverType": 8
                }
            ],
            "includeProtected": 1
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
            "gameId": self.game_id,
            "regionId": self.region_id,
            "isForceKill": 1,
            "executeTime": self.time
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
            "gameId": self.game_id,
            "regionId": self.region_id,
            "executeTime": self.time,
            "specId": None,
            "specName": None,
            "versionId": None,
            "versionName": None,
            "isFileupdate": 1
        }
        # data = {
        #     "rangeData": [
        #         {
        #             "areaId": self.areaId,
        #             "worlds": [
        #                 self.worldId_gong,
        #                 self.worldId_pu1,
        #                 self.worldId_pu2
        #             ]
        #         }
        #     ],
        #     "extraIds": [],
        #     "gameId": self.game_id,
        #     "regionId": self.region_id,
        #     "executeTime": self.time,
        #     "specList": [
        #         {
        #             "specsId": self.specsId_pu,
        #             "worldId": self.worldId_pu1,
        #             "areaId": 13,
        #             "groupIndex": 0,
        #             "f_spec": {
        #                 "id": 96,
        #                 "name": "远征2普通区-1S-ECS"
        #             }
        #         },
        #         {
        #             "specsId": 98,
        #             "specsName": "远征2公共区-2S-ECS",
        #             "worldId": 3523,
        #             "worldName": "0806-公共一区-V2.2",
        #             "areaId": 13,
        #             "areaName": "自动化运维预演",
        #             "groupIndex": 1,
        #             "f_spec": {
        #                 "id": 98,
        #                 "name": "远征2公共区-2S-ECS"
        #             }
        #         }
        #     ],
        #     "versionId": 288,
        #     "versionName": "2021.06.03-HWAutoDel",
        #     "isFileupdate": 1
        # }
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
            "gameId": self.game_id,
            "regionId": self.region_id,
            "executeTime": self.time,
            "isBook": 0,
            "preCreateTime": None,
            "openTime": (datetime.datetime.utcnow() + datetime.timedelta(hours=24)).isoformat() + 'Z',
            "isForeign": 0,
            "foreignTime": None,
            "serverList": []
        }
        response = self.qifu.test_clear(data)
        return response

    def test_container_upload(self):
        # 文件上传
        filePath = self.qifu.test_()
        data = {
            "rangeData": [
                {
                    "areaId": self.areaId,
                    "worlds": [
                        self.worldId_pu1
                    ]
                }
            ],
            "extraIds": [],
            "gameId": self.game_id,
            "regionId": self.region_id,
            "fileList": [
                {
                    "id": 0,
                    "file": None,
                    "fileName": "ChatControl.csv",
                    "filePath": filePath,
                    "uploadPath": "C:\\app\\cluster\\data\\global\\scp"
                }
            ]
        }
        response = self.qifu.test_container_upload(data)
        return response

    def test_stop_operate(self):
        # 停运
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
            "gameId": self.game_id,
            "regionId": self.region_id,
            "executeTime": self.time
        }
        response = self.qifu.test_stop_operate(data)
        # 停运完成后增加区服ID。写入到config
        worldId_gong = str(int(self.config.worldId_gong) + 1)
        worldId_pu1 = str(int(self.config.worldId_pu1) + 1)
        worldId_pu2 = str(int(self.config.worldId_pu2) + 1)
        self.config.set_conf(self.config.WORLDID_GONG, worldId_gong)
        self.config.set_conf(self.config.WORLDID_PU1, worldId_pu1)
        self.config.set_conf(self.config.WORLDID_PU2, worldId_pu2)
        return response


if __name__ == '__main__':
    test = TestStart()
    test.test_container_upload()
