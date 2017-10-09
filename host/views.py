from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views import View
import  paramiko,json
from host import models
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
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
        re = models.log.objects.filter().order_by('-date')[:6]
        version=request.GET.get('version',1)
        print(version)
        host=models.host.objects.filter(version=version)
        for i in host:
            print(i.ip)
            print(i.version)
            print(i.group)

        return render(request, 'host/task/excuteScript.html',{
            'active':'task',
            'liActive':'excute',
            're': re,
            'host':host
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

        server=models.host.objects.all()
        sort = request.GET.get('sort', "")

        # if sort:
        #     if sort == "version":
        #         server = server.order_by("-version")
        #     elif sort == "group":
        #         server = server.order_by("-group")

        return render(request, 'host/server/serverList.html', {
            'active':'server',
            'liActive': 'serverList',
            'all_server':server
        })

#添加服务器
class serverAdd(View):
    def post(self,request):
        ip=request.POST.get('ip','')
        group=request.POST.get('group','')
        version=request.POST.get('version','')
        models.host.objects.create(ip=ip,group=group,version=version)

        return HttpResponseRedirect('/host/serverList')

#获取单台服务器信息
class getServer(View):
    def get(self,request):
        id = request.GET.get('id','')
        host = models.host.objects.filter(id=id)

        if len(host)==1:
            list = {}
            list['ip'] = host[0].ip
            list['version'] = host[0].version
            list['group'] = host[0].group
            list['id'] = host[0].id
            return HttpResponse(json.dumps(list))
        else:
            list={}
            return HttpResponse(list)

#修改单台服务器信息
class editServer(View):
    def post(self,request):
        id = request.POST.get('id', '')
        print(id)
        ip = request.POST.get('ip', '')
        group = request.POST.get('group', '')
        version = request.POST.get('version', '')
        re=models.host.objects.filter(id=id).update(ip=ip,group=group,version=version)
        return HttpResponseRedirect('/host/serverList')

#删除单台服务器信息
class delServer(View):
    def get(self,request):
        id = request.GET.get('id','')
        re = models.host.objects.filter(id=id).delete()
        if re:
            return HttpResponse(1)
        else:
            return HttpResponse(2)

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





