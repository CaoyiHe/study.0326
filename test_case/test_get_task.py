from common.session import SendMethodEntity
# from common.config.config import Config, Default_Config
from common.config.config import Config
import json
from threading import Timer
import time
import logging


class GetTask(object):
    def __init__(self, taskId):
        self.config = Config()
        self.url = self.config.get_conf('url')
        self.taskId = taskId

    def test_check(self):
        # 对提交的任务进行审核
        url = self.url + f"api/task/{self.taskId}/approve"
        data = {
            "remark": "接口执行通过",
            "status": 0
        }
        response = SendMethodEntity.send_method("post", url, data=data)
        logging.info(response)
        return response

    def test_task_particulars(self):
        # 查看任务详情
        count = 0
        while True:
            url = self.url + f"api/task/{self.taskId}/detail"
            response = SendMethodEntity.send_method("get", url, )
            status = response["data"]["status"]
            logging.info(response)
            if status == 7 or status == 4:
                logging.info(response)
                break
            if status == 8 or status == 30 or status == 20:
                # 失败后对任务进行重试，重试三次后跳出循环
                if count >= 3:
                    raise ValueError("重试失败")
                count += 1
                response = SendMethodEntity.send_method("post", self.url + f"api/task/{self.taskId}/retry-skip", data={
                    "action": 1
                })
            time.sleep(10)

    @staticmethod
    def test_code(task_id):
        Get_Task = GetTask(task_id)
        Get_Task.test_check()
        Get_Task.test_task_particulars()


if __name__ == '__main__':
    GetTask(8821).test_code(8821)
