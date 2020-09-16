from pyairctrl.http_client import HTTPAirClient
from builtins import staticmethod

class DeviceConnector(object):
    
    @staticmethod
    def toggleOnOff():
        device = HTTPAirClient("192.168.0.143")
        data = device.get_status()
        
        values = {}
        if data["pwr"] == "0" :
            values["pwr"] = "1"
        else :
            values["pwr"] = "0"
        
        device.set_values(values)