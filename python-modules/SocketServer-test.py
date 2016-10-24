# coding:utf-8

from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler

#创建多线程   允许多个客户端同时访问
class  server(TCPServer,ThreadingMixIn):
    pass

#该函数    对接收的数据进行处理加工
def changData(x):
    z=x.upper()
    return z

#继承StreamRequestHandler类   ，改写handle 函数
class dataHandle(StreamRequestHandler):
    def handle(self):
        cliend_ip=self.request.getpeername()  #得到访问服务器的ip 返回的是一个元组  ，包含 ip ，port
        print "client_ip:",cliend_ip
        data=self.request.recv(2048)#接收数据
        print "receive data:",data
        r='jkljll'
        self.wfile.write(changData(data))#向客服端发送数据
        self.wfile.write('\n')
        self.wfile.write(data)#向客服端发送数据

servers=server(('192.168.30.100',8888),dataHandle)#server()需要两个参数，一个是（ip，port）,另一个是继承StreamRequestHandler后的类
servers.serve_forever() # 服务器无限循环运行
