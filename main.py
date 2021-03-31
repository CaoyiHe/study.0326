from test_data.test_kaifu import OpenService
from test_data.test_qifu import TestStart

if __name__ == '__main__':
    go_open = OpenService()
    # go_open.test_open_gong()      # 开公共区
    # go_open.test_open_pu()        # 开普通区
    go_qifu = TestStart()
    # go_qifu.test_serverlist_add()     # 修改serverlist
    # go_qifu.test_script()     # 刷脚本
    # go_qifu.test_stop()   # 关服
    go_qifu.test_start()    # 启服
    go_qifu.test_clear()    # 新区清数据
