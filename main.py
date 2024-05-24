from sqlite3 import connect
from verification import *
import telnet
import argparse
import sys

#文件传参

connect_mode = sys.argv[1]





ip_address = input("输入要ping的ip地址")
ping(ip_address)


input("Press any key to continue . . .")



host_ip = '192.168.0.2'
username = 'administrator'
password = '123deng123/'
command = 'powershell'
telnet_client = telnet.TelnetClient()
# 如果登录结果返加True，则执行命令，然后退出
if telnet_client.login_host(host_ip,username,password):
    telnet_client.execute_some_command(command)
    telnet_client.logout_host()
    
input()