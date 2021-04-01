from test_data.test_maintenance import Maintenance
from test_data.test_open import OpenService
from test_data.test_qifu import TestStart
import logging

logging.basicConfig(level='INFO', filename="G:\study\log\log.txt",
                    format='[%(asctime)s: %(levelname)s/%(filename)s:%(lineno)d] %(message)s')
# 全部流程
if __name__ == '__main__':
    go_open = OpenService()     # 开服
    # go_open.test_open_gong()      # 开公共区
    # go_open.test_open_pu()        # 开普通区
    go_qifu = TestStart()   # 区服操作
    # go_qifu.test_serverlist_add()     # 修改serverlist
    # go_qifu.test_script()     # 刷脚本
    # go_qifu.test_stop()   # 关服
    # go_qifu.test_start()    # 启服
    # go_qifu.test_clear()    # 新区清数据
    go_maintenance = Maintenance()    # 停服维护
    # go_maintenance.test_maintenance_cq()    # 例行重启
    # go_maintenance.test_maintenance_gg()    # 修改规格
    # go_maintenance.test_maintenance_bb()    # 版本更新
    go_maintenance.test_maintenance_hq_gx()     # 合区+版本更新
    go_maintenance.test_maintenance_zh()    # 大杂烩
    go_maintenance.test_maintenance_gm()    # 改名
    go_qifu.test_foreign()  # 对外
    go_qifu.test_stop_operate()     # 停运

# 开服流程
if __name__ == '__main__':
    go_open = OpenService()     # 开服
    go_open.test_open_gong()      # 开公共区
    go_open.test_open_pu()        # 开普通区

# 区服操作
if __name__ == '__main__':
    go_qifu = TestStart()  # 区服操作
    go_qifu.test_serverlist_add()  # 修改serverlist
    go_qifu.test_script()  # 刷脚本
    go_qifu.test_stop()  # 关服
    go_qifu.test_start()  # 启服
    go_qifu.test_clear()  # 新区清数据

# 停服维护
if __name__ == '__main__':
    go_maintenance = Maintenance()    # 停服维护
    go_maintenance.test_maintenance_cq()    # 例行重启
    go_maintenance.test_maintenance_gg()    # 修改规格
    go_maintenance.test_maintenance_bb()    # 版本更新
    go_maintenance.test_maintenance_hq_gx()     # 合区+版本更新
    go_maintenance.test_maintenance_zh()    # 大杂烩
    go_maintenance.test_maintenance_gm()    # 改名
