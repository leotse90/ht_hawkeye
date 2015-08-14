#coding=utf-8

'''
    tools for http.
    
    @author:leotse
'''

import socket

# check if port is accessible
def port_available(ip, port):
    try:
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sc.settimeout(2) # timeout
        sc.connect((ip, port))
        sc.close()
        return True
    except:
        sc.close()
        return False
