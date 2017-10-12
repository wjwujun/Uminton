"""Uminton URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from host.views import index,excuteScript,change,sendFile,serverList,serverAdd,getServer,editServer,delServer,serverGroup,log,history,check,user
urlpatterns = [
    url(r'^$', index.as_view()),    #主页

    url(r'^user', user.as_view()),    #检验账号
    url(r'^check', check.as_view()),    #检验账号密码

    url(r'^excuteScript', excuteScript.as_view()),   #过去页面
    url(r'^change', change.as_view()),               #执行脚本

   #url(r'^sendFile', sendFile.as_view()),           #快速分发文件



    url(r'^serverList', serverList.as_view()),            #服务器列表
    url(r'^serverAdd', serverAdd.as_view()),              #添加服务器
    url(r'^getServer', getServer.as_view()),              #获取单台
    url(r'^editServer', editServer.as_view()),            #修改
    url(r'^delServer', delServer.as_view()),              #删除
    url(r'^serverGroup', serverGroup.as_view()),          #服务器分组


    url(r'^log', log.as_view()),                    #任务历史
    url(r'^history', history.as_view()),            #任务历史


]
