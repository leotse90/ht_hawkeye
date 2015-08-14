#coding=utf-8

'''
    check all module status and send sms to related developers if something wrong.

    @author:leotse
'''

import datetime

from ht_hawkeye.models.hawkeye import ServiceMonitor, ServerMonitor, DeveloperInfo
from ht_hawkeye.utils.sms_utils import send_wechat_sms
from config import HealthStatus, Timedelta, AlertStrategy, AlertPriority

def notice_controller():
    # check service status
    check_service_status()
    # check server status
    check_server_status()

def check_service_status():
    # rule for alert:
    # 1.service_status is SICK
    # 2.service_status didn't update for more than Timedelta.SERVICE minute
    service_items = ServiceMonitor.objects.all()
    for item in service_items:
        service_status = item.service_status
        last_report_timestamp = str(item.last_report_timestamp)
        legal_report_timestamp = (datetime.datetime.now() - datetime.timedelta(minutes=Timedelta.SERVICE)).strftime("%Y-%m-%d %H:%M:%S")
        service_name = item.service_name if item.service_name else service_ip

        if last_report_timestamp <= legal_report_timestamp:
            alert_sms = "{service_name}(ip:{service_ip}, port:{service_port}) didn't report for more than {delay} minutes, please check!".format(service_name=service_name, service_ip=item.service_ip, service_port=item.service_port, delay=Timedelta.SERVICE)
            alert_developers = item.notice_developers.split(',')
            alert_wechats = get_developer_contacts(alert_developers, AlertStrategy.WECHAT)
            for app_key in alert_wechats:
                send_wechat_sms(app_key, "Service Alert", AlertPriority.CRITICAL, alert_sms)

        elif service_status == HealthStatus.SICK:
            alert_sms = "Alert: {service_name}(ip:{service_ip}, port:{service_port}) is not accessible, please check!".format(service_name=service_name, service_ip=item.service_ip, service_port=item.service_port)
            alert_developers = item.notice_developers.split(',')
            alert_wechats = get_developer_contacts(alert_developers, AlertStrategy.WECHAT)
            for app_key in alert_wechats:
                send_wechat_sms(app_key, "Service Alert", AlertPriority.CRITICAL, alert_sms)

def check_server_status():
    # rule for alert:
    # 1.server_status is SICK
    # 2.server_status didn't update for more than Timedelta.SERVER minute
    server_items = ServerMonitor.objects.all()
    for item in server_items:
        server_name = item.server_name if item.server_name else item.server_ip
        server_status = item.server_status
        last_report_timestamp = str(item.last_report_timestamp)
        legal_report_timestamp = (datetime.datetime.now() - datetime.timedelta(minutes=Timedelta.SERVER)).strftime("%Y-%m-%d %H:%M:%S")

        if last_report_timestamp <= legal_report_timestamp:
            alert_sms = "Alert:{server_name}(ip:{server_ip}) didn't report for more than {delay} minutes, please check!".format(server_name=server_name, server_ip=item.server_ip, delay=Timedelta.SERVER)
            alert_developers = item.notice_developers.split(',')
            alert_wechats = get_developer_contacts(alert_developers, AlertStrategy.WECHAT)
            for app_key in alert_wechats:
                send_wechat_sms(app_key, "Server Alert", AlertPriority.CRITICAL, alert_sms)

        elif server_status == HealthStatus.SICK:
            alert_sms = "Alert:{server_name}(ip:{server_ip}) is SICK({server_symptom}), please check!".format(server_name=server_name, server_ip=item.server_ip, server_symptom=item.server_symptom)
            alert_developers = item.notice_developers.split(',')
            alert_wechats = get_developer_contacts(alert_developers, AlertStrategy.WECHAT)
            for app_key in alert_wechats:
                send_wechat_sms(app_key, "Server Alert", AlertPriority.CRITICAL, alert_sms)

def get_developer_contacts(alert_developers, type):
    alert_contacts = []
    alert_items = DeveloperInfo.objects.filter(developer__in=alert_developers)
    if type == AlertStrategy.WECHAT:
        return [item.app_key for item in alert_items]
    elif type == AlertStrategy.SMS:
        return [item.telephone for item in alert_items]

if __name__ == '__main__':
    notice_controller()
