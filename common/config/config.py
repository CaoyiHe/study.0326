#coding=utf-8
from configparser import ConfigParser
# from Common import log
import os
import time


class Config:
    # TITLE_CONFIG = "config"
    VERSION_ID = "versionId"
    AREA_ID = "areaId"
    URL = "url"
    WORLDID_GONG = "worldId_gong"
    WORLDID_PU1 = "worldId_pu1"
    WORLDID_PU2 = "worldId_pu2"
    GAME_ID = "game_id"
    REGION_ID = "region_id"
    PARAMID = "paramId"
    SPECSID_GONG = "specsId_gong"
    SPECSID_PU = "specsId_pu"
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        # self.default_title = "config-SS"
        self.default_title = Config.default_title
        self.config = ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir + '\\Report\\xml'
        self.html_report_path = Config.path_dir + '\\Report\\html'
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")
        self.config.read(self.conf_path, encoding='utf-8')
        self.version_id = int(self.get_conf(Config.VERSION_ID))
        self.area_id = int(self.get_conf(Config.AREA_ID))
        self.url = self.get_conf(Config.URL)
        self.worldId_gong = int(self.get_conf("WORLDID_GONG"))
        self.worldId_pu1 = int(self.get_conf("WORLDID_PU1"))
        self.worldId_pu2 = int(self.get_conf("WORLDID_PU2"))
        self.game_id = int(self.get_conf(Config.GAME_ID))
        self.region_id = str(self.get_conf(Config.REGION_ID))
        self.param_id = self.get_conf(Config.PARAMID)
        self.specsId_pu = int(self.get_conf("SPECSID_PU"))
        self.specsId_gong = int(self.get_conf("SPECSID_GONG"))

    def get_conf(self, value, title=None):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        title = title or self.default_title
        return self.config.get(title, value, fallback=None)

    def set_conf(self, text, value, title=None):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        title = title or self.default_title
        self.config.set(title, text, value)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title=None):
        """
        配置文件添加
        :param title:
        :return:
        """
        title = title or self.default_title
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)
    default_title = input("(2117:远征2, 2107：远征, 2122：闪烁精灵, 2109：龙武手游, 2029：少女战争)请输入游戏：")

Default_Config = {}
conf = Config()
Default_Config["gameId"] = conf.get_conf("game_id")
Default_Config["regionId"] = conf.get_conf("region_id")
Default_Config["url"] = conf.get_conf("url")
if __name__ == '__main__':
    conf = Config()
    print(type(conf.get_conf('game_id')))
