#coding=utf-8

'''
    table information in hawkeye.

    @author:leotse
'''

from django.db import models

class ServiceMonitor(models.Model):
    class Meta:
        db_table = 't_service_monitor'

    id = models.IntegerField()
    service_name = models.CharField(max_length=50)
    service_ip = models.CharField(max_length=20)
    service_port = models.IntegerField()
    service_status = models.CharField(max_length=20)
    notice_developers = models.CharField(max_length=255)
    last_report_timestamp = models.DateTimeField()

class ServerMonitor(models.Model):
    class Meta:
        db_table = 't_server_monitor'
    
    id = models.IntegerField()
    server_name = models.CharField(max_length=50)
    server_ip = models.CharField(max_length=20)
    server_status = models.CharField(max_length=20)
    server_symptom = models.TextField()
    notice_developers = models.CharField(max_length=255)
    last_report_timestamp = models.DateTimeField()

class WebMonitor(models.Model):
    class Meta:
        db_table = 't_web_monitor'
    
    id = models.IntegerField()
    url_name = models.CharField(max_length=50)
    url = models.TextField()
    url_status = models.CharField(max_length=20)
    url_status_code = models.IntegerField()
    notice_developers = models.CharField(max_length=255)
    last_report_timestamp = models.DateTimeField()

class DeveloperInfo(models.Model):
    class Meta:
        db_table = 't_developer_info'

    id = models.IntegerField()
    developer = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    app_key = models.CharField(max_length=100)
