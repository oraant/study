# coding:utf-8

import daemon, socket
import sys, logging
    
def output(msg):
    with open('/var/log/oet/test.log', 'a')as file:
        file.write(msg+'\n')

def flush(msg):
    with open('/var/log/oet/test.log', 'w')as file:
        file.write(msg+'\n')

class SocketServer:

    def __init__(self, sock_host="0.0.0.0", sock_port=15521, sock_links=1, log_file='/var/log/oet/test.log'):
        self.sock_host = sock_host
        self.sock_port = sock_port
        self.sock_links = sock_links
        self.log_file = log_file

        logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s',filename=log_file)

    def create_server(self):
        '''开启一个Socket Server服务'''
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.sock_host, self.sock_port))
        self.server.listen(1)
        print 'create done'

    def handle_msg(self):
        '''处理基本的启、停、查请求'''
        output('in handle')
        while True:
            try:
                output('in try')
                connection, address = self.server.accept()
            except Exception , e:
                output('in exception')
                output(str(e))
            output('try done')
            req = connection.recv(1024)

            # 处理关闭请求
            if req == 'stop':
                res = 'Stoping Server'
                connection.send(res)
                connection.close()
                os.unlink(self.sock_file)
                exit(0)
            # 处理状态请求
            elif req == 'status':
                res = 'Server is running'
                connection.send(res)
            # 处理其他请求
            elif req != '':
                res = req
                connection.send(res)

    def send_msg2(self,req):
        '''创建一个Socket Client，并像服务器发送信息'''
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((self.sock_host, self.sock_port))
            client.send(req)
            res = client.recv(1024)
        except socket.error as e:
            res = str(e)
        return res

    def send_msg(self,req):
        '''创建一个Socket Client，并像服务器发送信息'''
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client.connect((self.sock_host, self.sock_port))
            client.send(req)
            res = client.recv(1024)
        except socket.error:
            res = 'Server is not running.'
        finally:
            client.close()
        return res

if __name__ == '__main__':

    flush('---')
    output('waiting')
    ss = SocketServer()

    try:
        msg = sys.argv[1]
    except Exception as e:
        msg = 'start'

    if msg == 'start':
        with daemon.DaemonContext():
            ss.create_server()
            ss.handle_msg()
            output(e)
    else:
        print ss.send_msg2(msg)
