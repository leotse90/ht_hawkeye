#coding=utf-8

'''
    message tools.

    @author:leotse
'''
import json
import urllib2
import random
import commands

# ensure you have a sms provider
def send_sms(telephones, sms):
	telephones_str = ','.join(telephones)

	sms_url = 'curl http://sdk.entinfo.cn:8061/mdsmssend.ashx?sn=your_sn&pwd=your_password'
	sms_url += '&mobile="{telephones_str}"'.format(telephones_str=telephones_str)
	sms_url += '&content="{content}"'.format(content=sms)

	rt, res = commands.getstatusoutput(sms_url)

	return rt == 0

# send wechat message by 110monitor
# website: www.110monitor.com
# one alert for one person once
def send_wechat_sms(app_key, alert_name, priority, alarm_content):
    '''
    url: "http://api.110monitor.com/alert/api/event"
    method: POST
    params:
        -app: must, application key
        -eventType: must, trigger or resolve
        -alarmName: must(trigger) optional(resolve), title of alert message
        -eventId: must, use it when you need close an alert
        -alarmContent: optional, details of alert
        -entityName: optional, name of alert object
        -entityId: optional, id of alert object
        -priority: optional, 1 for notice, 2 for alert, 3 for critical
    '''
    post_data = {}
    post_data["app"] = app_key
    post_data["eventId"] = unicode(random.randint(100000, 999999))
    post_data["eventType"] = "trigger"
    post_data["alarmName"] = alert_name
    post_data["entityName"] = ""
    post_data["entityId"] = ""
    post_data["priority"] = priority
    post_data["alarmContent"] = alarm_content

    url = "http://api.110monitor.com/alert/api/event"
    req = urllib2.Request(url=url, data=json.dumps(post_data))
    rep = urllib2.urlopen(req)
    res = rep.read()
    r = json.loads(res)
    return r["result"] == "success"    
