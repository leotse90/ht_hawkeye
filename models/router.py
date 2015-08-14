#coding=utf-8

'''
    router for database.

    @author: leotse
'''

from config import DjangoDatabase, HawkeyeDatabase

class Router:
    def db_for_read(self, model, **hints):
        from ht_hawkeye.models.hawkeye import ServerMonitor, ServiceMonitor, WebMonitor, DeveloperInfo
        if model in (ServerMonitor, ServiceMonitor, WebMonitor, DeveloperInfo):
            return HawkeyeDatabase.ROUTERNAME
        return DjangoDatabase.ROUTERNAME

    def db_for_write(self, model, **hints):
        #return HawkeyeDatabase.ROUTERNAME
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_syncdb(self, db, model):
        return None

