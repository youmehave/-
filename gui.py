# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHBoxLayout
#导入designer工具生成的login模块
from system import Ui_MainWindow
# 导入数据库控制模块
from py2sql import DataBase
import rename


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.qt_Buttom.clicked.connect(self.newClose)
        self.register_PButton.clicked.connect(self.connect_sql)
        # 指明当前是否进入管理页面
        self.enterMan = ''


    # 连接数据库
    def connect_sql(self):
        # 验证密码
        password = self.pwd_LineEdit.text()
        self.user = self.user_LineEdit_2.text()
        try:
            self.db = DataBase(self.user,password)
            if self.isRoot():
                self.pos_TextBrowser.setText("管理员"+self.user+"登录成功")
                # 进入管理员窗口
                self.enterMan = "Manager"
            else:
                self.pos_TextBrowser.setText("用户" + self.user + "登录成功")
                print("用户"+self.user+"登录成功")
                self.enterMan = "User"

        except:
            self.pos_TextBrowser.setText("密码错误，请重新输入密码")
            #清空密码栏
            self.pwd_LineEdit.clear()

    # 是否为管理员
    def isRoot(self):

        return self.Manager_Button.isChecked()






    def newClose(self):
        self.enterMan = ''
        return self.close()













# 管理者Ui的逻辑实现

from manager_win import Ui_Manager_Form

class managerForm(Ui_Manager_Form, QMainWindow):
    def __init__(self, DataBase: DataBase , parent = None):
        super(Ui_Manager_Form, self).__init__(parent)
        self.setupUi(self)
        # 用户添加、删除按钮初始化
        self.pushButton_deleteUser.clicked.connect(self.deleteUser)
        self.signUp_Button.clicked.connect(self.addUser)

        # 打印按钮初始化
        self.pushButton_printFile.clicked.connect(self.printFiles) # 打印文件列表
        self.Button_printUser.clicked.connect(self.printUser) # 打印用户列表

        # 执行指令初始化
        self.pushButton_do.clicked.connect(self.doCommand)

        # 重命名按钮初始化
        self.pushButton_renamefile.clicked.connect(self.enterRename)

        # 初始化数据库
        self.db = DataBase

        self.layout = QHBoxLayout()
        self.pushButton_findUser.clicked.connect(self.findUser)
        self.pushButton_findFile.clicked.connect(self.findFile)


        """
        主要功能页面按钮初始化
        """
        self.pushButton_choseFile.clicked.connect(self.choseFile)


    def deleteUser(self):
        # 获取用户名和密码
        user = self.lineEdit_user.text()
        password = self.lineEdit_pwd.text()

        # 检查用户名是否存在，（密码匹配，用户名存在则删除用户）
        if self.db.deleteUser(user):
            # 从数据库中删除用户
            self.clearPrompt()
            self.textBrowser_con.setText("用户已删除")
        else:
            # 清空提示栏
            self.clearPrompt()
            # 在状态栏告知用户名不存在
            self.textBrowser_con.setText("用户名不存在")

    # 将运行信息打印至textCon中
    def printCon(self, s):
        self.clearPrompt()
        self.textBrowser_con.setText(s)

    # QTABLEWIDGET功能组件
    def printData(self, datas, tableWidget):

       for row, data in enumerate(datas):
           for  cul, subData in enumerate(data):
               newItem = QTableWidgetItem(subData)
               tableWidget.setItem(row,cul,newItem)
       # self.setLayout(self.verticalLayout_4)
       self.printCon("列表内容显示完成")



    def addUser(self):
        user = self.lineEdit_user.text()
        password = self.lineEdit_pwd.text()



        if self.db.creatUser(user, password):
            self.clearPrompt()
            self.textBrowser_con.setText("用户创建完成")
        else:
            self.clearPrompt()
            self.textBrowser_con.setText("用户已存在")
    # 打印文件数据表
    def printFiles(self):
        self.printData(self.db.showFiles(),self.tableWidget_file)

    # 打印用户数据表
    def printUser(self):

        self.printData(self.db.showUsers(),self.tableWidget_user)


    def findUser(self):
        try:
            txt = self.lineEdit_find.text()
            user = self.db.findUser(txt)
            # 清空用户列表
            self.tableWidget_user.clear()
            self.printData(user,self.tableWidget_user)
            self.printCon("用户名包含%s的用户已全部列出"%(txt))
        except:
            self.printCon("查询出错,请检查后重试")


    def findFile(self):
        try:
            txt = self.lineEdit_find.text()
            file = self.db.findFile(txt)
            # 清空用户列表
            self.tableWidget_file.clear()
            self.printData(file, self.tableWidget_file)
            self.printCon("文件编号名包含%s的文件已全部列出" % (txt))
        except:
            self.printCon("查询出错,请检查后重试")



    # 执行命令窗口
    def doCommand(self):
        # 获取指令
        command = self.textEdit_command.toPlainText()
        # 将指令传入数据库中执行
        try:
            self.db.execute(command)
            self.clearPrompt()
            self.textBrowser_con.setText("指令执行完毕")
        except:
            # 打印错误
            self.textBrowser_con.setText("指令有误，请重新输入")

    # 进入rename窗口 学一下先，下次写
    def enterRename(self):
        self.stackedWidget.setCurrentIndex(1)




    def clearPrompt(self):
        self.textBrowser_con.clear()


    """
    开始尝试设计主要功能页面
    """
    # 从文件夹中选择文件，并将路径显示在lineEdit中
    def choseFile(self):
        filePath = rename.getPath()
        newName = self.getNewName()

    # 根据用户选择生成新的文件名
    def getNewName(self):
        # 判断文件类型
        if self.radioButton_other.isChecked():
            # 定义一个字典存储文件名的各个组分
            notClinicalFile = {"fileID":'', "file":'', 'datetime':''}
            notClinicalFileID = {"fileType": '', "fileCon":'', 'sequence': 0, 'version':1.0, "isApp":False}

            if self.lineEdit_newName.text() != '':
                notClinicalFile["file"] = self.lineEdit_newName.text()
            else:
                # 弹出小窗口警告
                print("未输入文件名")
            if self.radioButton_CON.isChecked() or self.radioButton_SMP.isChecked() \
                or self.radioButton_SOP.isChecked() or self.radioButton_SRD.isChecked():













# 用户UI逻辑实现
from user_win import User_UI_Form

class userForm(User_UI_Form, QMainWindow):
    def __init__(self, DataBase: DataBase, parent=None):
        super(User_UI_Form, self).__init__(parent)
        self.setupUi(self)
        self.db = DataBase

        # 内部按钮初始化
        self.pushButton_findFile.clicked.connect(self.findFile)

        self.pushButton_printList.clicked.connect(self.printFiles)

    def printData(self, files, tableWidget):
        for row, file in enumerate(files):
            for cul, subData in enumerate(file):
                newItem = QTableWidgetItem(subData)
                tableWidget.setItem(row, cul, newItem)
        # self.setLayout(self.verticalLayout_4)
        print("列表内容显示完成")

    # 查找特定文件
    def findFile(self):
        try:
            txt = self.lineEdit_findFile.text()
            file = self.db.findFile(txt)
            # 清空用户列表
            self.tableWidget_file.clear()
            self.printData(file, self.tableWidget_printData)
            print("文件编号名包含%s的文件已全部列出" % (txt))
        except:
            print("查询出错,请检查后重试")
    # 打印已有文件列表
    def printFiles(self):
        self.printData(self.db.showFiles(),self.tableWidget_printData)

















# 用于实现各个页面的控制：从更高维度来传递各个页面的信息
"""
实现功能：
登录：从登录页面进入管理员页面和用户操作页面
退出：如果是登录页面，则直接关闭窗口；如果不是登录页面，则关闭窗口后返回至登录页面
返回：返回则是返回至上一个页面
"""
class controller():
    def __init__(self):
        pass
    # 用于展示登录界面
    def show_login(self):
        self.login = MyMainForm()
        self.login.register_PButton.clicked.connect(self.show_Main)
        self.login.show()

    # 展示管理员或用户窗口
    def show_Main(self):
        self.login.connect_sql()
        # 如果enterMan参数等于0，则弹出警告，连接数据库服务器失败
        if self.login.enterMan == "Manager":
            self.ManagerWin = managerForm(self.login.db)
            self.ManagerWin.pushButton_cancel.clicked.connect(self.back_login)
            self.ManagerWin.pushButton_cancel_2.clicked.connect(self.back_login)
            self.ManagerWin.pushButton_back.clicked.connect(self.func_back)
            self.login.close()
            self.ManagerWin.show()
            print("进入管理员窗口成功")
        elif self.login.enterMan == "User":
            # 进入使用者窗口
            print("正在进入使用者窗口")
            self.UserWin = userForm(self.login.db)
            self.UserWin.pushButton_cancel.clicked.connect(self.back_login)
            self.UserWin.pushButton_rename.clicked.connect(self.goRename)
            self.login.close()
            self.UserWin.show()



        else:
            # 弹出警告（连接数据库服务器失败）
            print("数据库连接失败")


    # 退出管理员或用户窗口
    def back_login(self):
        if self.login.enterMan == "Manager":
            self.show_login()
            self.ManagerWin.close()
            print("管理员退出")
        elif self.login.enterMan == "User":
            self.show_login()
            # 关闭用户窗口
            self.ManagerWin.close()
            print("用户退出")
        else:
            self.printError()

    # 从功能页面返回
    def func_back(self):
        if self.login.enterMan == "Manager":
            self.ManagerWin.stackedWidget.setCurrentIndex(0)
        elif self.login.enterMan == "User":
            # 关闭管理员窗口，打开用户窗口
            self.ManagerWin.close()
            # 开启用户窗口
            self.UserWin.show()
        else:
            self.printError()


    def printError(self):
        print("程序出错，self.login.enterMan为空")

    # 用于从用户界面到达重命名界面
    def goRename(self):
        # 关闭用户窗口
        self.UserWin.close()


        # 打开功能页面
        self.ManagerWin = managerForm(self.login.db)
        self.ManagerWin.pushButton_cancel.clicked.connect(self.back_login)
        self.ManagerWin.pushButton_cancel_2.clicked.connect(self.back_login)
        self.ManagerWin.pushButton_back.clicked.connect(self.func_back)
        self.ManagerWin.show()
        self.ManagerWin.enterRename()





if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    db = DataBase('root','1234567890')
    myWin = managerForm(db)

    myWin.show()
    #将窗口控件显示在屏幕上
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())