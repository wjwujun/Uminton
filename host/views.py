from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views import View
import  json,threading,paramiko
from host import models
from plugins.threading import task

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.


#登录页面
class login(View):
    def get(self,request):
        return render(request, 'login.html')


#账号验证
class user(View):
    def post(self, request):
        name = request.POST.get('name', '')
        data = models.user.objects.filter(name=name)
        if len(data) == 0:
            return HttpResponse(1)
        else:
            return HttpResponse(2)

#密码验证
class check(View):
    def post(self,request):
        name=request.POST.get('username','')
        pwd=request.POST.get('pwd','')
        data=models.user.objects.filter(name=name)

        if data[0].pwd==pwd:
            request.session['name'] = str(data[0].name)
            request.session['id'] = str(data[0].id)
            return render(request, 'host/index.html')
        else:
            return render(request, 'login.html')


#host主页
class index(View):
    def get(self,request):
        return render(request, 'host/index.html')

""""
作业管理
"""
#获取页面脚本执行页面
class excuteScript(View):
    def get(self,request):
        re = models.log.objects.filter().order_by('-date')[:6]
        version=request.GET.get('version',0)
        version=int(version)


        host=models.host.objects.filter(version=version)

        return render(request, 'host/task/excuteScript.html',{
            'active':'task',
            'liActive':'excute',
            're': re,
            'version':version,
            'host':host
        })

#脚本执行(版本更新)
class change(View):
    def post(self,request):
        execute = request.POST.get('execute')
        ip=request.POST.getlist('ip',[])
        version=request.POST.get('version')
        if len(ip)==0:
            all_ip=models.host.objects.filter(version=version)
            for i in all_ip:
                ip.append(i.ip)
        print(ip)
        #类型转换
        num=int(execute)
        thread = task()
        #执行操作
        if num==1:        #更新
            cmd = 'cd /opt && python demo.py && echo $?'
            #多线程(多台机器)同时执行命令
            for  i in ip:
                a = threading.Thread(target=thread.ssh2, args=(i,cmd))
                a.start()
                a.join()

            re=thread.list
            return HttpResponse(re)

        elif num==2:      #偏移时间
            cmd = 'cd /opt && sh start_freestyle_tw.sh logchange && echo $?'
            for i in ip:
                a = threading.Thread(target=thread.ssh2, args=(i, cmd))
                a.start()
                a.join()

            re = thread.list
            return HttpResponse(re)

        elif num==3:    #重启
            cmd = 'cd /opt && sh start_freestyle_tw.sh restart && echo $?'
            for i in ip:
                a = threading.Thread(target=thread.ssh2, args=(i, cmd))
                a.start()
                a.join()

            re = thread.list
            return HttpResponse(re)
        elif num==4:    #重读
            cmd = 'cd /opt && sh start_freestyle_tw.sh reload && echo $?'
            for i in ip:
                a = threading.Thread(target=thread.ssh2, args=(i, cmd))
                a.start()
                a.join()

            re = thread.list
            return HttpResponse(re)

        elif num==5:        #热更
            cmd = 'cd /opt && sh start_freestyle_tw.sh update && echo $?'
            for i in ip:
                a = threading.Thread(target=thread.ssh2, args=(i, cmd))
                a.start()
                a.join()
            re = thread.list

            return HttpResponse(re)
        else:
            pass



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
        re = models.log.objects.filter().order_by('-date')[:6]


        #sort = request.GET.get('sort', "")
        # if sort:
        #     if sort == "version":
        #         server = server.order_by("-version")
        #     elif sort == "group":
        #         server = server.order_by("-group")

        return render(request, 'host/server/serverList.html', {
            'active':'server',
            'liActive': 'serverList',
            're': re,
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

#日志管理
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
        re = models.log.objects.filter().order_by('-date')[:10]
        return render(request, 'host/history/history.html',{
            're': re,
            'active':'history'
        })





