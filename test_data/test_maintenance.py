# coding=gbk
from test_case.test_qifu import StartServer
from common.config.config import Config
from common.send_method import SendMethod
from test_case.test_get_task import GetTask
from datetime import timedelta
import datetime
import time


class Maintenance(object):
    def __int__(self):
        self.qifu = StartServer()
        self.config = Config()
        self.worldId_gong = int(self.config.get_conf("worldId_gong"))
        self.worldId_pu1 = int(self.config.get_conf("worldId_pu1"))
        self.worldId_pu2 = int(self.config.get_conf("worldId_pu2"))
        self.areaId = int(self.config.get_conf("areaId"))
        self.versionId = int(self.config.get_conf("versionId"))
        self.groupname = time.strftime("%m.%d %H:%M:%S")
        self.worldname_gong = str(self.worldId_gong) + "-�ع����-������"
        self.worldname_pu1 = str(self.worldId_gong) + "-�ع����-��ͨ��-1"
        self.worldname_pu2 = str(self.worldId_gong) + "-�ع����-��ͨ��-2"

    def test_maintenance_cq(self):
        # ��������
        data = {
            "gameId": 2117,
            "regionId": "TJZYY",
            "types": "4",
            "startTime": datetime.datetime.utcnow().isoformat() + 'Z',
            "endTime": (datetime.datetime.utcnow() + timedelta(hours=0.5)).isoformat() + 'Z',
            "data": {
                "restart": [
                    {
                        "worldId": self.worldId_gong,
                        "worldName": self.worldname_gong,
                        "areaId": self.areaId,
                        "areaName": "�Զ�����ά"
                    },
                    {
                        "worldId": self.worldId_pu1,
                        "worldName": self.worldname_pu1,
                        "areaId": self.areaId,
                        "areaName": "�Զ�����ά"
                    },
                    {
                        "worldId": self.worldId_pu2,
                        "worldName": self.worldname_pu2,
                        "areaId": self.areaId,
                        "areaName": "�Զ�����ά"
                    }
                ]
            },
            "countdown": 5,
            "openMode": 1
        }
        response = self.qifu.test_maintenance(data)
        return response

    def test_maintenance_gg(self):
        # �޸Ĺ��
        data = {
            "gameId": 2117,
            "regionId": "TJZYY",
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
                        "areaId": self.areaId,
                        "areaName": "�Զ�����ά",
                        "groupIndex": 0
                    },
                    {
                        "specsId": 60,
                        "specsName": None,
                        "worldId": self.worldId_pu2,
                        "worldName": self.worldname_pu2,
                        "areaId": self.areaId,
                        "areaName": "�Զ�����ά",
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
        # �汾����
        data = {
            "gameId": 2117,
            "regionId": "TJZYY",
            "types": "1",
            "startTime": datetime.datetime.utcnow().isoformat() + 'Z',
            "endTime": (datetime.datetime.utcnow() + timedelta(hours=0.5)).isoformat() + 'Z',
            "data": {
                "versionUpdate": {
                    "areaId": self.areaId,
                    "gameWorldList": [
                        {
                            "worldId": self.worldId_gong,
                            "worldName": self.worldname_gong,
                            "areaId": self.areaId,
                            "areaName": "������"
                        },
                        {
                            "worldId": self.worldId_pu1,
                            "worldName": self.worldname_pu1,
                            "areaId": self.areaId,
                            "areaName": "��ͨ��"
                        },
                        {
                            "worldId": self.worldId_pu2,
                            "worldName": self.worldname_pu2,
                            "areaId": self.areaId,
                            "areaName": "��ͨ��"
                        }
                    ],
                    "version": self.versionId
                }
            },
            "countdown": 5,
            "openMode": 1
        }
        response = self.qifu.test_maintenance(data)
        return response

    def test_maintenance_hq_gx(self):
        # ����+�汾����
        data = {
            "gameId": 2117,
            "regionId": "TJZYY",
            "types": "1,2",
            "startTime": datetime.datetime.utcnow().isoformat() + 'Z',
            "endTime": (datetime.datetime.utcnow() + timedelta(hours=0.5)).isoformat() + 'Z',
            "data": {

                "versionUpdate": {
                    "areaId": None,
                    "version": self.versionId,
                    "gameWorldList": [
                        {
                            "worldId": self.worldId_gong,
                            "worldName": self.worldname_gong,
                            "areaId": self.areaId,
                            "areaName": "������"
                        },
                        {
                            "worldId": self.worldId_pu1,
                            "worldName": self.worldname_pu1,
                            "areaId": self.areaId,
                            "areaName": "��ͨ��"
                        },
                        {
                            "worldId": self.worldId_pu2,
                            "worldName": self.worldname_pu2,
                            "areaId": self.areaId,
                            "areaName": "��ͨ��"
                        }
                    ]
                },
                "mergeArea": [
                    {
                        "toWorldId": self.worldname_pu1,
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
        # ���ӻ�
        data = {
            "gameId": 2117,
            "regionId": "TJZYY",
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
                            "areaId": self.areaId,
                            "areaName": "�Զ�����ά"
                        }
                    ],
                    "version": self.versionId
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
                        "areaId": self.areaId,
                        "worldId": self.worldId_pu1,
                        "newName": self.worldname_pu1 + "-����"
                    }
                ],
                "editSpecs": [
                    {
                        "specsId": 46,
                        "specsName": None,
                        "worldId": self.worldId_pu1,
                        "worldName": self.worldname_pu1,
                        "areaId": self.areaId,
                        "areaName": "�Զ�����ά",
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
        # ����
        data = {
            "gameId": 2117,
            "regionId": "TJZYY",
            "types": "3",
            "startTime": datetime.datetime.utcnow().isoformat() + 'Z',
            "endTime": (datetime.datetime.utcnow() + timedelta(hours=0.5)).isoformat() + 'Z',
            "data": {
                "editName": [
                    {
                        "areaId": self.areaId,
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
    Maintenance().test_maintenance_gm()
