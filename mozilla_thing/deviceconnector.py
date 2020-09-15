'''
Created on 2020. szept. 15.

@author: pepot
'''
import sys

from pyairctrl.airctrl import HTTPAirCli

class DeviceConnector(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    
    def connect(self):
        #devices = HTTPAirCli.ssdp()
        #if not devices:
        #    print(
        #        "Air purifier not autodetected. Try --ipaddr option to force specific IP address."
        #    )
        #    sys.exit(1)
        #for device in devices:
            c = HTTPAirCli("192.168.0.143")
            print(
                c.get_status()
            )