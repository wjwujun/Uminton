import  paramiko

class task(object):
    list={}
    def ssh2(self,ip,cmd):
        try:
            # 远程ssh链接,执行命令
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            #在每一台机器上执行脚本
            client.connect(ip, 22, "root", "uminton")
            stdin, stdout, stderr = client.exec_command(cmd)

            #获取每个脚本执行后的返回值
            channel = stdout.channel
            result = channel.recv_exit_status()
            self.list[ip]=result
            client.close()

        except:
            print('%s\tError\n'%(ip))








