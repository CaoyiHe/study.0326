from selenium import webdriver
import time
import json
import requests


class TestTaPd:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(
            'https://www.tapd.cn/44506107/bugtrace/bugreports/stat_general/general/customreport-1144506107001000072')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.ding_url = "https://oapi.dingtalk.com/robot/send?access_token=040304fa7f88fdfa1e305519580fb75917208c2be77b35db56a79e72ac60ee88"
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    def test_upload_image(self, file_path):
        # �ϴ��ļ�
        url = "http://59.110.63.111:5000/api/upload/file"
        files = {'file': open(file_path, 'rb')}
        r = requests.post(url=url, files=files)
        png_url = r.json()["url"]
        return png_url

    def test_tapd(self):
        # �����¼ҳ���¼
        self.driver.find_element_by_id('username').send_keys('hecaoyi@q1.com')
        self.driver.find_element_by_id('password_input').send_keys('Hecaoyi520.')
        self.driver.find_element_by_id('tcloud_login_button').click()
        time.sleep(10)
        # ��ÿ������BUG���н�ͼ
        everyday = "C:\\Users\\hecaoyi\\Desktop\\���ð�\\��������BUG.png"
        self.driver.get_screenshot_as_file(everyday)
        # �����ϴ��ӿڣ��õ�ͼƬ����
        png_url = TestTaPd().test_upload_image(file_path=everyday)
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "��������BUG",
                "text": f"## ![image]({png_url})\n ## ��������BUG\n > https://www.tapd.cn/44506107/bugtrace/bugreports/my_view?conf_id=1144506107001108601&query_token=2021042786e525af8f67b4b3d2c89c802a0a990e",
            }
        }
        response = requests.post(url=self.ding_url, headers=self.headers, data=json.dumps(data), verify=False)
        time.sleep(3)
        # self.driver.get(
        #     'https://www.tapd.cn/44506107/bugtrace/bugreports/stat_general/general/customreport-1144506107001000073')
        self.driver.find_element_by_link_text('��������BUG').click()
        time.sleep(3)
        everyday_prod = "C:\\Users\\hecaoyi\\Desktop\\���ð�\\��������BUG.png"
        self.driver.get_screenshot_as_file(everyday_prod)
        png_url = TestTaPd().test_upload_image(file_path=everyday_prod)
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "��������BUG",
                "text": f"## ![image]({png_url})\n ## ��������BUG\n > https://www.tapd.cn/44506107/bugtrace/bugreports/my_view?conf_id=1144506107001109309&query_token=2021042750f9c73beed7aed7c6c43a646cda3b34",
            }
        }
        response = requests.post(url=self.ding_url, headers=self.headers, data=json.dumps(data), verify=False)
        time.sleep(3)
        # self.driver.get(
        #     'https://www.tapd.cn/44506107/bugtrace/bugreports/stat_general/general/customreport-1144506107001000074')
        self.driver.find_element_by_link_text('��ǰδ���BUG').click()
        time.sleep(3)
        all_bug = "C:\\Users\\hecaoyi\\Desktop\\���ð�\\Ŀǰʣ��BUG.png"
        self.driver.get_screenshot_as_file(all_bug)
        png_url = TestTaPd().test_upload_image(file_path=all_bug)
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "Ŀǰʣ��BUG",
                "text": f"## ![image]({png_url})\n ## Ŀǰʣ��BUG\n > https://www.tapd.cn/44506107/bugtrace/bugreports/my_view?conf_id=1144506107001109095&query_token=20210427c0320a08057dd99920437b1088712039",
            }
        }
        response = requests.post(url=self.ding_url, headers=self.headers, data=json.dumps(data), verify=False)
        time.sleep(3)
        self.driver.quit()
        # url = 'https://riyugo.com/file.php'
        #
        # files = {'file': open('C:\\Users\\hecaoyi\\Desktop\\���ð�\\baidu.png', 'rb')}
        # values = {"name": "baidu.png", "uuid": uuid.uuid4()}
        #
        # r = requests.post(url, files=files, data=values)
        # png = r.json()["url"]
        # print(r.text)
        # print(png)
        # with open(imagePath, "rb") as f:  # תΪ�����Ƹ�ʽ
        #     base64_data = base64.b64encode(f.read())  # ʹ��base64���м���

    def test_ding(self, png_url):
        url = "https://oapi.dingtalk.com/robot/send?access_token=040304fa7f88fdfa1e305519580fb75917208c2be77b35db56a79e72ac60ee88"
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "xxxxxxx",
                "text": "## ![image](png_url)\n ## ����ʧ��\n > www.baidu.com",
            }
        }
        # data = {
        #     "msgtype": "markdown",
        #     "markdown": {
        #         "title": "xxxxxxx",
        #         "text": f"## ![image](data:image/jpeg;base64,{base64_data})\n ## ����ʧ��\n > [www.baidu.com]"
        #     }
        # }
        response = requests.post(url=url, headers=headers, data=json.dumps(data), verify=False)
        print(response.text)
