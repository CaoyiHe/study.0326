from common.session import SendMethodEntity
from common.config.config import Config
from test_case.test_get_task import GetTask
import logging
import time


class StartServer(Config):

    # def __init__(self):
    #     super(StartServer, self).__init__()

    def test_serverlist_add(self, data):
        # 添加serverlist
        url = self.url + "api/task/server-list"
        response = SendMethodEntity.send_method("post", url, data=data)
        logging.info(response)
        task_id = response["data"]["taskId"]
        GetTask.test_code(task_id)
        return response

    def test_groupid(self, groupname):
        # 查询groupid对外时用到
        url = self.url + "api/resource/server-list/11"
        response = SendMethodEntity.send_method("get", url)
        logging.info(response)
        return response

    def test_foreign(self, data):
        # 对外
        url = self.url + "api/task/foreign-world"
        response = SendMethodEntity.send_method("post", url, data=data)
        time.sleep(10)
        # task_id = response["data"]["taskId"]
        # GetTask.test_task_particulars(task_id)
        logging.info(response)
        return response

    def test_script(self, data):
        # 刷脚本
        url = self.url + "api/task/file-update"
        response = SendMethodEntity.send_method("post", url, data=data)
        task_id = response["data"]["taskId"]
        GetTask.test_code(task_id)
        return response

    def test_stop(self, data):
        # 关服
        url = self.url + "api/task/close-game-world"
        response = SendMethodEntity.send_method("post", url, data=data)
        task_id = response["data"]["taskId"]
        GetTask.test_revocation(task_id)
        response = SendMethodEntity.send_method("put", url + f"/{task_id}", data=data)
        GetTask.test_code(task_id)
        return response

    def test_start(self, data):
        # 启服
        url = self.url + "api/task/start-game-world"
        response = SendMethodEntity.send_method("post", url, data=data)
        task_id = response["data"]["taskId"]
        GetTask.test_revocation(task_id)
        response = SendMethodEntity.send_method("put", url + f"/{task_id}", data=data)
        GetTask.test_code(task_id)
        return response

    def test_clear(self, data):
        # 新区清数据
        url = self.url + "api/task/clear-data"
        response = SendMethodEntity.send_method("post", url, data=data)
        task_id = response["data"]["taskId"]
        GetTask.test_revocation(task_id)
        response = SendMethodEntity.send_method("put", url + f"/{task_id}", data=data)
        GetTask.test_code(task_id)
        return response

    def test_(self):
        upload_url = self.url + "/api/resource/file/upload"
        files = {'file': open(r'C:\Users\hecaoyi\Desktop\新建文件夹\ChatControl.csv', 'rb')}
        data = {
            "gameId": self.game_id,
            "regionId": self.region_id,
            "name": "ChatControl.csv"
        }
        response = SendMethodEntity.send_method("post", url=upload_url, data=data, files=files)
        filePath = response["data"]["filePath"]
        return filePath

    def test_container_upload(self, data):
        # 文件上传
        filePath = StartServer().test_()
        url = self.url + "api/task/container-upload"
        response = SendMethodEntity.send_method("post", url, data=data)
        task_id = response["data"]["taskId"]
        GetTask.test_revocation(task_id)
        response = SendMethodEntity.send_method("put", url + f"/{task_id}", data=data)
        GetTask.test_code(task_id)
        return response

    def test_stop_operate(self, data):
        # 停运
        url = self.url + "api/task/stop-operate"
        response = SendMethodEntity.send_method("post", url, data=data)
        task_id = response["data"]["taskId"]
        GetTask.test_revocation(task_id)
        response = SendMethodEntity.send_method("put", url + f"/{task_id}", data=data)
        GetTask.test_code(task_id)
        return response

    def test_maintenance(self, data):
        # 停服维护
        url = self.url + "api/task/maintenance"
        response = SendMethodEntity.send_method("post", url, data=data)
        task_id = response["data"]["taskId"]
        GetTask.test_revocation(task_id)
        response = SendMethodEntity.send_method("put", url + f"/{task_id}", data=data)
        GetTask.test_code(task_id)
        return response
