from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views import View
import  paramiko
from host import models
# Create your views here.


#登录页面
class login(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        username=request.POST.get('username','')
        pwd=request.POST.get('pwd','')
        if username=='admin' and pwd=='110120':
            return render(request, 'host/index.html')
        else:
            print("你的账号或者密码有错误")



#host主页
class index(View):
    def get(self,request):
        return render(request, 'host/index.html')



""""
作业管理
"""

#脚本执行(版本更新)
class excuteScript(View):
    def get(self,request):
        re = models.log.objects.all().order_by('-date')[:6]

        return render(request, 'host/task/excuteScript.html',{
            'active':'task',
            'liActive':'excute',
            're': re
        })

    def post(self,request):
        execute = request.POST.get('execute', 0)
        #远程ssh链接
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect("60.205.222.43", 22, "root", "wj@110120")

        #类型转换
        num=int(execute)
        md5="wrf5456szgs1"
        #执行更新操作
        if num==1:
            cmd="cd /application/tools && python insert.py " + md5
            stdin, stdout, stderr = client.exec_command(cmd)
        elif num==2:
            print(222)
        elif num==3:
            print(3333)
        elif num==4:
            print(4444)
        elif num==5:
            print(5555)
        else:
            pass
        client.close()
        return HttpResponseRedirect('/host/excuteScript')



#快速分发文件
class sendFile(View):
    def get(self,request):
        return render(request, 'host/task/sednFile.html',{
            'active':'task',
            'liActive': 'sendFile',
        })




"""
服务器管理
"""


#服务器列表
class serverList(View):
    def get(self,request):
        return render(request, 'host/server/serverList.html', {
            'active':'server',
            'liActive': 'serverList',
        })
#添加服务器
class serverAdd(View):
    def get(self,request):
        return render(request, 'host/server/serverAdd.html', {
            'active':'server',
            'liActive': 'serverAdd',
        })


#服务器分组
class serverGroup(View):
    def get(self,request):
        return render(request, 'host/server/serverGroup.html', {
            'active':'server',
            'liActive': 'serverGroup',
        })


""""
日志管理
"""

#任务历史
class log(View):
    def get(self,request):
        return render(request, 'host/log/log.html',{
            'active':'log'
        })


""""
任务历史
"""

#任务历史
class history(View):
    def get(self,request):
        return render(request, 'host/history/history.html',{
            'active':'history'
        })





