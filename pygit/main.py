import paramiko
import logging
import time
import os

file_path1 = "aaaaaaaaaaa"
file_path2 = "aaaaaaaaaa"

target_path1 = "xxxxxxxxxxxx"
target_path2 = "ccccccccccccccccc"

#file_list = [xxxxxxxxxxxxxx]


class SSHConnection:
    def __init__(self, host="106.15.5.66", port=22, username="root", password="SEUgit123456"):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        transport = paramiko.Transport((self.host, self.port))
        transport.connect(username=self.username, password=self.password)
        self.__transport = transport

    def close(self):
        self.__transport.close()

    # def upload(self):
    #     sftp = paramiko.SFTPClient.from_transport(self.__transport)
    #     for i in file_list:
    #         if i != "知识库.txt":
    #             original_file = os.path.join(file_path1, i)
    #             target_file = os.path.join(target_path1, i)
    #             sftp.put(original_file, target_file)
    #         else:
    #             original_file = os.path.join(file_path2, i)
    #             target_file = os.path.join(target_path2, i)
    #             sftp.put(original_file, target_file)

    def sshconn(self):
        ssh = paramiko.SSHClient()
        # 允许连接不在know_hosts文件中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh._transport = self.__transport
        ssh.connect(hostname=self.host, port=self.port, username=self.username, password=self.password)
        # 执行服务器中的shell脚本
        stdin, stdout, stderr = ssh.exec_command('echo 2')
        result = stdout.read().decode()
        print(result)

    def run(self):
        self.connect()
        #self.upload()
        self.sshconn()
        self.close()


if __name__ == '__main__':
    test = SSHConnection()
    test.run()

