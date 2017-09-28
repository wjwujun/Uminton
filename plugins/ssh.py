import  paramiko


#远程ssh链接
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect("60.205.222.43",22, "wj", "110120")

while True:
    command=input("please input your cmd!\n")
    if command=='exit':
            exit()
    stdin, stdout, stderr = client.exec_command(command)
    aa=stdout.readlines()
    print(aa)
    print(stderr.readlines())


client.close()





