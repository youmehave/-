import pymysql

from datetime import datetime

"""
这个文件用于存储python与数据库的交互
"""
class DataBase():
    def __init__(self, user, pwd):
        self.host = 'localhost'
        self.user = user
        self.password = pwd
        self.dataBase = 'RUNOOB'
        self.db = pymysql.connect(host=self.host,
                             user=self.user,
                             password=self.password,
                             database=self.dataBase
                             )
        # 将数据库设置为可更新状态
        with self.db.cursor() as cursor:
            sql = 'SET SQL_SAFE_UPDATES = 0'
            cursor.execute(sql)
            print("当前数据库可更新")

    # 数据库获取指令并执行
    def execute(self, command):
        sql = command
        with self.db:
            with self.db.cursor() as cursor:
                cursor.execute(sql)

    # 展示数据表
    def showFiles(self):
        sql = "SELECT * FROM files"
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            files = cursor.fetchall()
        for file in files:
            file = list(file)
            file[-2] = str(file[-2])
            yield file

    # 显示用户表
    def showUsers(self):
        sql = "SELECT host, user, authentication_string, password_last_changed FROM mysql.user WHERE user NOT LIKE 'mysql.%'"
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            userDatas = cursor.fetchall()

        for user in userDatas:
            user = list(user)
            user[-1] = str(user[-1])
            yield user
    # 查找用户
    def findUser(self, username)->bool:
        sql = "SELECT host, user, authentication_string, password_last_changed FROM mysql.user WHERE user LIKE '%"+username+"%'"
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            userData = cursor.fetchall()

        for user in userData:
            user = list(user)
            user[-1] = str(user[-1])
            yield user

    # 查找文件
    def findFile(self, fileCode):
        sql = "SELECT * FROM files WHERE file_id LIKE '%"+fileCode+"%'"
        with self.db.cursor() as cursor:
            cursor.execute(sql)
            files = cursor.fetchall()

        for file in files:
            file = list(file)
            file[-2] = str(file[-2])
            yield file




    def creatUser(self, username, password)->bool:
        sql = "CREATE USER '%s'@'localhost' IDENTIFIED BY '%s'"%(username,password)
        try:
            with self.db.cursor() as cursor:
                cursor.execute(sql)
                # 赋予用户基本权限
                cursor.execute("GRANT SELECT ON Runoob.* to '%s'@'localhost'" % (username))
            return True
        except:
            print("Error: user has existed")
            return False





    def deleteUser(self, username)->bool:
        sql = "DROP USER '%s'@'localhost'" %(username)
        try:
            with self.db.cursor() as cursor:
                cursor.execute(sql)
                print("成功删除用户%s"%(username))
            return True
        except:
            print("ERROR: Fail to delete user")
            return False


    # 关闭数据库
    def close(self):
        self.db.close()



if __name__ == '__main__':
    db = DataBase("root", "1234567890")
    # db.creatUser("yunjnn",'1234567')
    # db.deleteUser("yunjnn")
    for i in db.findUser('yun'):
        print(i)
    db.close()
    print("ok")