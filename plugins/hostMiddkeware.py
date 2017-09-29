from django.utils.deprecation import MiddlewareMixin
import pymysql
from host import models

class Row1(MiddlewareMixin):
    def process_request(self,request):
        content = request.get_full_path()
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
            models.log.objects.create(name="root", request=content,action=action)



