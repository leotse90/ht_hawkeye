#coding=utf-8

'''
    configuration for hawkeye.

    @author: leotse
'''

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'ht_hawkeye.settings'

# default database for django
class DjangoDatabase:
    HOST = '0.0.0.0'
    NAME = 'django'
    USER = 'user'
    PASSWORD = 'pwd'
    PORT = 3306
    ROUTERNAME = 'default'

# database for monitor information
class HawkeyeDatabase:
    HOST = '0.0.0.0'
    NAME = 'hawk_eye'
    USER = 'user'
    PASSWORD = 'pwd'
    PORT = 3306
    ROUTERNAME = 'hawk_eye'

# server or service status
class HealthStatus:
    HEALTH = 'HEALTH'
    SICK = 'SICK'

# report maximum delay(minutes)
class Timedelta:
    SERVICE = 2
    SERVER = 2

# alert strategy
class AlertStrategy:
    SMS = 1
    WECHAT = 2
    EMAIL = 3

# alert priority
class AlertPriority:
    NOTICE = 1
    ALERT = 2
    CRITICAL = 3

# init contact developer
URGENT_DEVELOPER = 'leotse'

