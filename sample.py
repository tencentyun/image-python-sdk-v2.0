#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from qcloud_image import Client
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers

appid = 'APPID'
secret_id = 'SECRETID'
secret_key = 'SECRETKEY'
bucket = 'BUCKET'

client = Client(appid, secret_id, secret_key, bucket)
client.use_http()
client.set_timeout(30)

#图片鉴黄
#单个或多个图片Url
print (client.porn_detect(CIUrls(['http://jiangsu.china.com.cn/uploadfile/2015/1102/1446443026382534.jpg','http://n.sinaimg.cn/fashion/transform/20160704/flgG-fxtspsa6612705.jpg'])))
#单个或多个图片File
print (client.porn_detect(CIFiles(['./test.jpg',])))

# 图片标签
#单个图片url
print (client.tag_detect(CIUrl('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png')))
#单个图片file
print (client.tag_detect(CIFile('./hot2.jpg')))

#OCR-身份证识别
#单个或多个图片Url,识别身份证正面
print (client.idcard_detect(CIUrls(['http://imgs.focus.cn/upload/sz/5876/a_58758051.jpg']), 0))
#单个或多个图片file,识别身份证正面
print (client.idcard_detect(CIFiles(['./id4_zheng.jpg','./id1_zheng.jpg']), 0))
#单个或多个图片Url,识别身份证反面
print (client.idcard_detect(CIUrls(['http://www.csx.gov.cn/cwfw/bszn/201403/W020121030349825312574.jpg', 'http://www.4009951551.com/upload/image/20151026/1445831136187479.png']), 1))
#单个或多个图片file,识别身份证反面
print (client.idcard_detect(CIFiles(['./id5_fan.jpg']), 1))
#单个或多个图片内容,识别身份证反面
if os.path.exists('id5_fan.jpg'):
    print (client.idcard_detect(CIBuffers([open("id5_fan.jpg",'rb').read()]), 1))

#OCR-名片识别    
#单个或多个图片Url
print (client.namecard_detect(CIUrls(['http://pic1.nipic.com/2008-12-03/2008123181119306_2.jpg', 'http://pic.58pic.com/58pic/12/49/04/80k58PICzYP.jpg']), 0))
#单个或多个图片file
print (client.namecard_detect(CIFiles(['./name1.jpg']), 1))
#单个或多个图片内容,识别名片
if os.path.exists('name1.jpg'):
    print (client.namecard_detect(CIBuffers([open("name1.jpg",'rb').read()]), 1))
	
#人脸检测
#单个图片Url, mode:1为检测最大的人脸 , 0为检测所有人脸
print (client.face_detect(CIUrl('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png')))
#单个图片file,mode:1为检测最大的人脸 , 0为检测所有人脸
print (client.face_detect(CIFile('./hot2.jpg')))

#五官定位
#单个图片Url,mode:1为检测最大的人脸 , 0为检测所有人脸
print (client.face_shape(CIUrl('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png'),1))
#单个图片file,mode:1为检测最大的人脸 , 0为检测所有人脸
print (client.face_shape(CIFile('./hot2.jpg'),1))

#创建一个Person, 使用图片url
print (client.face_newperson('person111', ['group2',], CIUrl('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png'), 'xiaoxin'))
#创建一个Person, 使用图片file
print (client.face_newperson('person211', ['group2',], CIFile('./hot2.jpg')))

#将单个或者多个Face的url加入到一个Person中
print (client.face_addface('person111', CIUrls(['http://jiangsu.china.com.cn/uploadfile/2015/1102/1446443026382534.jpg','http://n.sinaimg.cn/fashion/transform/20160704/flgG-fxtspsa6612705.jpg'])))
#将单个或者多个Face的file加入到一个Person中
print (client.face_addface('person211', CIFiles(['./test.jpg',])))

#删除人脸,删除一个person下的face
print (client.face_delface('person111', ['person111',]))

#设置信息
print (client.face_setinfo('person111', 'hello'))

#获取信息
print (client.face_getinfo('person111'))

#获取组列表
print (client.face_getgroupids())

#获取人列表
print (client.face_getpersonids('group2'))

#获取人脸列表
print (client.face_getfaceids('person211'))

#获取人脸信息
print (client.face_getfaceinfo('1820307972625034938'))

#删除个人
print (client.face_delperson('person11'))

#人脸验证,单个图片Url
print (client.face_verify('person111', CIUrl('http://img3.a0bi.com/upload/ttq/20160814/1471155260063.png')))
#人脸验证,单个图片file
print (client.face_verify('person111', CIFile('./test.jpg')))

#人脸检索,单个文件url
print (client.face_identify('group1', CIUrl('http://www.5djiaren.com/uploads/2016-07/22-141354_227.jpg')))
##人脸检索,单个文件file
print (client.face_identify('group2', CIFile('./test.jpg')))

#人脸对比
#两个对比图片的文件url
print (client.face_compare(CIFile('./zhao1.jpg'), CIFile('./zhao2.jpg')))
#两个对比图片的文件file
print (client.face_compare(CIUrl('http://www.miexue.com/d/file/junshiyingshi/2016-12-05/60bce03aac7a57e4fc600ecee1591e1d.jpg'), CIUrl('http://img.mp.itc.cn/upload/20161118/ee6be67ec6fb4135b5d579ab05acd715_th.jpg')))
#一个是图片的文件url， 一个是对比图片的文件file
print (client.face_compare(CIFile('./zhao1.jpg'), CIUrl('http://www.miexue.com/d/file/junshiyingshi/2016-12-05/60bce03aac7a57e4fc600ecee1591e1d.jpg')))

#身份证识别对比
#身份证url
print (client.face_idcardcompare('420822198804266119', '李时杰', CIUrl('http://docs.ebdoor.com/Image/CompanyCertificate/1/16844.jpg')))
#身份证文件file
print (client.face_idcardcompare('420822198804266119', '李时杰', CIFile('./id4_zheng.jpg')))

#人脸核身
#活体检测第一步：获取唇语（验证码）
obj = client.face_livegetfour()
print (obj)
#验证码
validate_data =''
if 'date' in obj:
    if 'validate_data' in obj['data']:
        validate_data = obj['data']['validate_data']

print (validate_data)
#活体检测第二步：检测
print (client.face_livedetectfour(validate_data, CIFile('../dn.qlv'), False, CIFile('../wxb.jpg')))
#活体检测第二步：检测--对比指定身份信息
print (client.face_idcardlivedetectfour(validate_data, CIFile('../dnn.qlv'), '330782198802084329', '李时杰'))

