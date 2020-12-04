from django.db import models
'''
orm与数据库对应关系：
类--->表
对象--->数据行（记录）
属性--->字段
'''
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=32)  # varchar(32) 可变字符串32位长
    password = models.CharField(max_length=32)  # varchar(32) 可变字符串32位长
