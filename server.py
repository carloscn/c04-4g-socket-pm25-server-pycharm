#coding=utf-8


import socket
import select
import SocketServer
from multiprocessing import Process
import os
import os.path
import sys
import time

reload(sys);
sys.setdefaultencoding('utf-8');


localIp = "172.19.134.27";

class SocketServer:

    def __init__(self, port):
        self.port = port;
        self.srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.srvsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
        self.srvsock.bind( (localIp, port));
        self.srvsock.listen(10);
        self.descripors = [self.srvsock];
        print("*Server init finish!");

    def run(self):
        while True:
            c, addr = self.srvsock.accept();
            print('*Join address: ' + addr);
            strRecv = c.recv(1024).decode('gbk');
            current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()));
            current_time = current_time + "#";
            if strRecv.__contains__("#"):
                str_s = strRecv.split("#");
                saveStr = current_time + "PM2.5 : " + str_s[1] + "\n";
                fileHandle = open("mem.txt", 'a');
                fileHandle.write(saveStr);
                fileHandle.close();
            print("存入数据:" + saveStr + "  --- save ok!");

if __name__ == '__main__':
    SocketServer(8001).run();