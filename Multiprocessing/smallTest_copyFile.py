# -*- coding: utf-8 -*-
import os
from multiprocessing import Pool, Manager
# Goal: 将一个含有大量文件的文件夹中的所有文件使用多进程方式复制至另一个新的文件夹
# Steps: Create a new directory -> Get all the files' name -> Copy to new directory by multiprocessing

def copyFile(old, new, name, q):
    # Copy one file from one folder to another folder
    fr = open(old + '/' + name)
    fw = open(new + '/' + name, 'w')

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    q.put(name)

def main():
    # 1. Create a new folder
    # raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收，返回字符串。 input() 接受合法python表达式
    # Consider using the raw_input() function for general input from users.
    oldFolder = raw_input("Name of File you want to copy:")
    newFolder = oldFolder + ' copy'
    os.makedirs(newFolder)

    # 2. Get all the files' name of old folder
    fileNames = os.listdir(oldFolder)

    # 3.Copy to new directory by multiprocessing
    pool = Pool(5)
    q = Manager().Queue()

    for name in fileNames:
        pool.apply_async(copyFile(), args=(oldFolder, newFolder, name, q))

    num, size = 0, len(fileNames)
    while num != size:
        # Can build a progress bar here
        q.get()
        num += 1
    print 'copy finished.'

if __name__ == '__main__':
    main()