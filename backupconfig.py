from jnpr.junos import Device
from jnpr.junos.utils.scp import SCP
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
 
        
        with SCP(dev, progress=True) as scp:
         
         if value=='10.108.129.9':
            scp.get('/config/rescue.conf.gz', local_path='/home/jsadmin/Malabe_ENFVI_Backups/Malabe-DC-GW2')
        # code block 1

         elif value=='10.108.129.10':
           scp.get('/config/rescue.conf.gz', local_path='/home/jsadmin/Malabe_ENFVI_Backups/Malabe-DC-GW1')
    # code block 2
         elif value=='10.203.57.9':
            scp.get('/config/rescue.conf.gz', local_path='/home/jsadmin/Malabe_ENFVI_Backups/Pili-DC-GW1')

         elif value=='10.203.57.10':
             scp.get('/config/rescue.conf.gz', local_path='/home/jsadmin/Malabe_ENFVI_Backups/Pili-DC-GW2')

         else: 
             print("Backup Not Succeded")
    # code block 3

            
        
    except ConnectError as err:
        print ("Cannot connect to device: {0}".format(err))
        return
if __name__ == "__main__":
    main()