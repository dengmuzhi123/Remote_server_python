from ipaddress import ip_address
import paramiko  
import platform    # For getting the operating system name
import subprocess  # For executing a shell command



def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    如果主机 （str） 响应 ping 请求，则返回 True。
    请记住，即使主机名有效，主机也可能不响应 ping （ICMP） 请求。
    """
  
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0


def ssh_connect_to_windows(ip, port=22, username='username', password='password'):  
    try:  
        # 创建一个SSH客户端  
        ssh = paramiko.SSHClient()  
          
        # 自动添加服务器的SSH key（注意：这在生产环境中是不安全的）  
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
          
        # 尝试连接到服务器  
        ssh.connect(ip, port=port, username=username, password=password)  
          
        # 如果连接成功，输出1并关闭连接  
        print("1")  
        ssh.close()  
        return True  
    except paramiko.AuthenticationException:  
        print("0")  # 认证失败  
        return False  
    except paramiko.SSHException as sshException:  
        print("0")  # SSH连接问题  
        return False  
    except Exception as e:  
        print("0")  # 其他异常  
        print(f"An error occurred: {e}")  
        return False  
# 示例用法  
ip = '192.168.0.2'
username = 'adminstrator'  
password = '123deng123/'  
 
'''
if ssh_connect_to_windows(ip, username=username, password=password):  
    print("SSH连接成功")  
else:  
    print("SSH连接失败")
    input()
'''

