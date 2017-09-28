# -*- coding: utf-8 -*-
import linecache
import os,re


#获取zip的最新的版本号
def zip_num():
	a=os.listdir('./zip')
	a.sort(key= lambda x:int(x[10:-4]))
	last_num=a[-1]
	return last_num[8:-4]

zip_num()

#获取xml的最新版本号
def xml_num():
	count = len(open('serverversion.xml', 'rb').readlines())
	line = linecache.getline('serverversion.xml', count-2)
	info=re.findall(r'\d+',line)
	#print(line)

	xml=[info[4],info[5]]
	return xml
	# f=open('serverversion.xml','rb')
	# for i in f:
	# 	print(i)
	# f.close()
xml_num()


#比较zip和xml的版本号，如果zip大，就向xml文件中插入一行数据
def compare(num):
	zip_version=zip_num()
	xml_version=xml_num()
	if int(zip_version)>int(xml_version[1]):			##如果zip的版本号大于xml的，就向xml中插入最新的版本好记录
		count = len(open('serverversion.xml', 'rb').readlines())
		line = linecache.getline('serverversion.xml', count - 2)
		aa = line.replace(xml_version[1], zip_version)
		aa = line.replace(xml_version[0], zip_version[5:])
		print(aa)
		aa = aa.replace("md5=\"\"","md5=\""+str(num)+"\"")
		print(aa)
		ee=re.findall(r"md5=\"(.*?)\"",aa)
		print(ee[0])



#		fp = open("serverversion.xml", "rb")
#		lines=fp.readlines()
#		lines[-2:-2] =['  '+aa]
#		open('serverversion.xml', 'w+').writelines(str(v) for v in lines)

	else:
		print(2)

compare(num)





