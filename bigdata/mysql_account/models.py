# coding:utf-8
from django.db import models

# Create your models here.
from django.db import models


class MysqlAccounts(models.Model):
    __tablename__ = 'mysql_account'
    id = models.IntegerField(u'ID')
    loginUser = models.CharField(u'认证用户名', max_length=100)
    loginPassword = models.CharField(u'认证用户密码', max_length=255)
    name = models.CharField(u'用户名', max_length=100)
    password = models.CharField(u'密码',max_length=255)
    host=models.CharField(u'授权数据库IP',max_length=100)
    priv=models.CharField(u'权限',max_length=200)
    remoteHost=models.CharField(u'来源IP',max_length=100)
    database=models.CharField(u'数据库名',max_length=100)
    tableName=models.CharField(u'表名',max_length=100)

    # id = db.Column(db.Integer(), primary_key=True)
    # loginUser = db.Column('login-user', db.String(100))
    # loginPassword = db.Column('login-password', db.String(255))
    # name = db.Column(db.String(100))
    # password = db.Column(db.String(255))
    # host = db.Column(db.String(255))
    # priv = db.Column(db.String(100))
    # remoteHost = db.Column('remote-host', db.String(100))
    # database = db.Column(db.String(100))
    # tableName = db.Column('table-name', db.String(255))

    def __init__(self, host, name, password, priv, remoteHost, database, tableName):
        self.loginUser = 'dbmanager'
        self.loginPassword = '15cac1c0748acf5d0783d7c2f19aa6ab17ee7129f1a7e25724c1def36911f3e4'
        self.name = name
        self.password = password
        self.host = host
        self.priv = priv
        self.remoteHost = remoteHost
        self.database = database
        self.tableName = tableName

    def __repr__(self):
        return "<Host '{}'>".format(self.host)
