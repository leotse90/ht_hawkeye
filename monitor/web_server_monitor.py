#coding=utf-8

from ht_hawkeye.config import URGENT_DEVELOPER, AlertPriority
from ht_hawkeye.models.hawkeye import DeveloperInfo
from ht_hawkeye.utils.http_utils import port_available
from ht_hawkeye.utils.sms_utils import send_wechat_sms

# web server settings
HOST = "0.0.0.0"
PORT = 8000

def monitor():
    admin_items = DeveloperInfo.objects.filter(developer=URGENT_DEVELOPER)
    admin_app_key = admin_items[0].app_key
    admin_alert_name = "Web Server Notification"

    # monitor web server
    active = port_available(HOST, PORT)
    admin_alarm_content = "Web Server is Active." if active else "Web Server is DEAD!!!!"
    admin_priority = AlertPriority.NOTICE if active else AlertPriority.CRITICAL

    # send wechat message
    send_wechat_sms(admin_app_key, admin_alert_name, admin_priority, admin_alarm_content)

if __name__ == "__main__":
    monitor()
