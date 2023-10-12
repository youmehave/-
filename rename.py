"""
用于执行重命名操作：
"""
import os
import sys
from tkinter import filedialog
from tkinter import *
from gui import *
"""
执行重命名操作：
input：文件路径 file_path,
      新文件名 dst
output: 新的文件路径
"""
def rename(file_path, dst):
    # 从file_path中获取文件名
    src = ''
    path_list = list(file_path)
    n = len(path_list)
    for i in range(n):
        if path_list[n-i-1] == '/' or path_list[n-i-1] == "\\":
            break
        src = path_list[n-i-1] + src
        path_list.pop()
    # 重命名
    path = ''.join(path_list)
    new_file_path = path+dst
    os.rename(file_path, new_file_path)

    return new_file_path, src

"""
    获取旧文件地址。选择本地文件夹，通过点击文件获取用户选择的文件路径，以便后续处理
    input: Null
    output: file_path
"""
def getPath():
    root = Tk()
    root.withdraw()
    file_path = ''
    while(file_path == ''):
        file_path = filedialog.askopenfilename()
        if file_path == '':
            print("选择文件")
    return file_path

"""
    获取文件名
    input:文件地址path
    output:文件名name
"""
def getName(path):
    path_list = list(path)
    l = len(path_list)
    name = ''
    for i in range(l):
        if path_list[l-i-1] == '\\' or path_list[l-i-1] == '/':
            break
        name = path_list.pop()+ name
    return name

"""
获取文件格式
input: f_name文件名
output: f_format 文件格式
"""
def getFormat(f_name):
    name_list = list(f_name)
    l = len(name_list)
    f_format = ''
    for i in range(l):
        if name_list[l-i-1] == '.':
            break
        f_format = name_list.pop()+f_format
    return f_format

"""
字符串拼接
input:name文件名
      format格式
output:file_name存在格式的文件名
"""
def concat(name, format):
    return name+'.'+format


if __name__ == '__main__':
    file_path = getPath()
    print(file_path)
    name = getName(file_path)
    print(name)
    format = getFormat(name)
    print(format)
    dst = input("输入新的文件名：")
    n_file_path, old_name = rename(file_path, concat(dst,format))
    print("重命名完成")
    print("new_file_path:{}".format(n_file_path))
    print(old_name)