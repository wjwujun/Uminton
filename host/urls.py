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
from host.views import index,excuteScript,sendFile,executeSql,executeTask,newTask,crondTask,account,script,DBaccount,sql,history
urlpatterns = [
    url(r'^$', index.as_view()),    #主页

    url(r'^excuteScript', excuteScript.as_view()),   #快速脚本执行
    url(r'^sendFile', sendFile.as_view()),           #快速分发文件
    url(r'^executeSql', executeSql.as_view()),      #快速执行sql脚本
    url(r'^executeTask', executeTask.as_view()),     #常用作业执行
    url(r'^newTask', newTask.as_view()),            #新建作业
    url(r'^crondTask', crondTask.as_view()),        #定时作业



    url(r'^account', account.as_view()),            #账户管理
    url(r'^script', script.as_view()),              #脚本管理
    url(r'^DBaccount', DBaccount.as_view()),        #DB账户管理
    url(r'^sql', sql.as_view()),                    #SQl管理

    url(r'^history', history.as_view()),            #任务历史


]
