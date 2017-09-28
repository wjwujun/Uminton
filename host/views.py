from django.shortcuts import render,HttpResponse
from django.views import View
import  paramiko
from host import models
# Create your views here.

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
            'liActive':'active',
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

        re=models.log.objects.all().order_by('-date')[:6]
        return render(request, 'host/task/excuteScript.html', {
            'active': 'task',
            'liActive': 'active',
            're':re
        })




















#快速分发文件
class sendFile(View):
    def get(self,request):
        return render(request, 'host/task/sednFile.html',{
            'active':'task'
        })

#快速执行sql脚本
class executeSql(View):
    def get(self,request):
        return render(request, 'host/task/executeSql.html',{
            'active':'task'
        })
#常用作业执行
class executeTask(View):
    def get(self,request):
        return render(request, 'host/task/executeTask.html',{
            'active':'task'
        })
#新建作业
class newTask(View):
    def get(self,request):
        return render(request, 'host/task/newTask.html',{
            'active':'task'
        })
#定时作业
class crondTask(View):
    def get(self,request):
        return render(request, 'host/task/crondTask.html',{
            'active':'task'
        })



"""
业务管理

"""


#账户管理
class account(View):
    def get(self,request):
        return render(request, 'host/admin/account.html',{
            'active':'active'
        })
#脚本管理
class script(View):
    def get(self,request):
        return render(request, 'host/admin/script.html',{
            'active':'active'
        })


#DB账户管理
class DBaccount(View):
    def get(self,request):
        return render(request, 'host/admin/DBaccount.html',{
            'active':'active'
        })



#SQl管理
class sql(View):
    def get(self,request):
        return render(request, 'host/admin/sql.html',{
            'active':'active'
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





