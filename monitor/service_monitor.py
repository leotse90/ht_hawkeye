#coding=utf-8

'''
    monitor all services in table.
    
    @author:leotse
'''

import datetime

from ht_hawkeye.utils.http_utils import port_available
from ht_hawkeye.models.hawkeye import ServiceMonitor
from ht_hawkeye.config import HealthStatus

def service_monitor_controller():
    # get all services information
    service_items = ServiceMonitor.objects.all()
    # check services
    service_check(service_items)


def service_check(service_items):
    # iterate services list and check port, then change table status
    for service_item in service_items:
        curr_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        service_ip = service_item.service_ip
        service_port = service_item.service_port

        access_result = port_available(service_ip, service_port)
        print access_result        
        service_status = HealthStatus.HEALTH if access_result else HealthStatus.SICK
        ServiceMonitor.objects.filter(service_ip=service_ip, service_port=service_port).update(service_status=service_status, last_report_timestamp=curr_timestamp)        


if __name__ == "__main__":
    service_monitor_controller()
