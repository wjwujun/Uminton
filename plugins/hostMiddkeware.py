from django.utils.deprecation import MiddlewareMixin
import pymysql
from host import models
import re
class Row1(MiddlewareMixin):
    def process_request(self,request):
        content = request.get_full_path()
        list=re.split(" |\/|\?",content)
        if list[2]== "change":
            num = request.POST.get('execute', 0)
            action = ""
            if int(num) == 1:
                action="更新"
            elif int(num) == 2:
                action = "偏移时间"
            elif int(num) == 3:
                action = "重启"
            elif int(num) == 4:
                action = "重读"
            elif int(num) == 5:
                action = "热更"
            else:
                action = " "

            if  action!= " ":
                models.log.objects.create(name=request.session['name'] , request=content,action=action)
        elif list[2] == "serverAdd":
            action = "添加服务器"
            models.log.objects.create(name=request.session['name'] , request=content, action=action)
        elif list[2] == "editServer":
            action = "修改服务器"
            models.log.objects.create(name=request.session['name'] , request=content, action=action)
        elif list[2] == "delServer":
            action = "删除服务器"
            models.log.objects.create(name=request.session['name'] , request=content, action=action)



