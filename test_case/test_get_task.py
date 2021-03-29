from common.session import SendMethodEntity
from common.config.config import Config, Default_Config


class GetTask:
    def __init__(self, taskId):
        self.config = Config()
        self.url = self.config.get_conf('url')
        self.taskId = taskId

    def test_check(self):
        # 对提交的任务进行审核
        url = self.url + f"api/task/{self.taskId}/approve"
        data = {
            "remark": "接口执行通过",
            "status": 1
        }
        response = SendMethodEntity.send_method("post", url, data=data)
        print(response)
        return response

    def test_task_particulars(self):
        # 查看任务详情
        url = self.url + f"api/task/{self.taskId}/detail"
        print(url)
        response = SendMethodEntity.send_method("get", url, )
        print(response)
        return response

    @staticmethod
    def shenhe(taskId):
        Get_Task = GetTask(taskId)
        Get_Task.test_check()
        Get_Task.test_task_particulars()

# if __name__ == '__main__':
#     test = GetTask(7365)
#     test.test_check()
#     test.test_task_particulars()
