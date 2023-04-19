from jnpr.junos import Device
from pprint import pprint
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
import yaml
from lxml import etree

def main():

 input_file = '/home/jsadmin/Automation/RPC_EXE/hosts.yaml'

 for key, value in yaml.full_load(open(input_file)).items():

    print(value)
    dev = Device(host=value, user='menuka_08214', passwd='BIGcisco#1991$', port=22)
    # open a connection with the device and start a NETCONF session
    try:
        dev.open()
        #print (dev.display_xml_rpc('show route', format='text'))
        sw = dev.rpc.get_route_information(table='VRF_GI_FDD.inet.0')
        print(etree.tostring(sw, encoding='unicode'))
        sw_info_text = dev.rpc.get_software_information({'format':'text'})
        print(etree.tostring(sw_info_text)) 
        
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        return
if __name__ == "__main__":
    main()