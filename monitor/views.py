#coding=utf-8

'''
    views of monitor.
	
    @author:leotse
'''

import json
import datetime

from django.http import HttpResponse

from ht_hawkeye.models.hawkeye import ServerMonitor
from ht_hawkeye.config import URGENT_DEVELOPER


'''
    API: health_report
    method: POST
    request: {'server_ip':server ip address, 'server_status':sick or health, 'server_symptom':null or reason of sick}
    response: {'status':success or failed}
'''
def health_report_api(request):
    server_name = request.REQUEST.get("server_name").encode("utf-8")
    server_ip = request.REQUEST.get("server_ip").encode("utf-8")
    server_status = request.REQUEST.get("server_status").encode("utf-8")
    server_symptom = request.REQUEST.get("server_symptom").encode("utf-8")

    store_result = store_server_health_info(server_name, server_ip, server_status, server_symptom)
    status = 'success' if store_result else 'failed'
    response_data = {'status':status}

    return HttpResponse(json.dumps(response_data), 'text/plain')


def store_server_health_info(server_name, server_ip, server_status, server_symptom):
    curr_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # check if ip exists
    server_ip_items = ServerMonitor.objects.filter(server_ip=server_ip)
    if server_ip_items:
        server_ip_items.update(server_status=server_status, server_symptom=server_symptom, last_report_timestamp=curr_timestamp)
    else:
        ServerMonitor(server_name=server_name, server_ip=server_ip, server_status=server_status, server_symptom=server_symptom, notice_developers=URGENT_DEVELOPER, last_report_timestamp=curr_timestamp).save()

    return True

