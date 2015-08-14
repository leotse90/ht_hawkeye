#coding=utf-8

'''
    web page url monitor.
    
    @author: leotse
'''

import urllib
import datetime

from ht_hawkeye.models.hawkeye import WebMonitor
from ht_hawkeye.config import HealthStatus

# health http status code
ACTIVE_STATUS_CODE = 200

def web_monitor_controller():
    url_items = WebMonitor.objects.all()

    for item in url_items:
        page_url = item.url
        f = urllib.urlopen(page_url)
        rt_status_code = f.getcode()
        
        url_status = HealthStatus.HEALTH if rt_status_code == ACTIVE_STATUS_CODE else HealthStatus.SICK
        curr_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        WebMonitor.objects.filter(url=page_url).update(url_status=url_status, url_status_code=rt_status_code, last_report_timestamp=curr_timestamp)

if __name__ == "__main__":
    web_monitor_controller()

