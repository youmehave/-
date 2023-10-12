"""主函数程序，按过程"""
#导入程序运行必须模块
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import *
from py2sql import *


if __name__ == '__main__':

# 开启登录界面
#固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
#初始化
    signWin = MyMainForm()
    #将窗口控件显示在屏幕上
    signWin.show()

    if signWin.enterMan is True:
        ManWin = managerForm(signWin.db)
        # 关闭登录页面
        signWin.newClose()
        # 开启管理员页面
        ManWin.show()
# 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
    # 进入管理员页面






