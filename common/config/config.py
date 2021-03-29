from configparser import ConfigParser
# from Common import log
import os
import time


class Config:
    # TITLE_CONFIG = "config"
    VERSION_ID = "versionId"
    AREA_ID = "areaId"
    URL = "url"
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.default_title = "config"
        self.config = ConfigParser()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir + '\\Report\\xml'
        self.html_report_path = Config.path_dir + '\\Report\\html'
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')
        self.version_Id = self.get_conf(Config.VERSION_ID)
        self.area_id = self.get_conf(Config.AREA_ID)
        self.url = self.get_conf(Config.URL)

    def get_conf(self, value, title=None):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        title = title or self.default_title
        return self.config.get(title, value)

    def set_conf(self, value, text, title=None):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        title = title or self.default_title
        self.config.set(title, value, text)
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


Default_Config = {}
conf = Config()
Default_Config["gameId"] = conf.get_conf("gameId")
Default_Config["regionId"] = conf.get_conf("regionId")
Default_Config["url"] = conf.get_conf("url")
if __name__ == '__main__':
    conf = Config()
    print(conf.get_conf('url'))
