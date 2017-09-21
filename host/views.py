from django.shortcuts import render,HttpResponse
from django.views import View
# Create your views here.

#host主页
class index(View):
    def get(self,request):
        return render(request, 'host/index.html')



""""
作业管理
"""

#快速脚本执行
class excuteScript(View):
    def get(self,request):
        return render(request, 'host/task/excuteScript.html',{
            'active':'task'
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





