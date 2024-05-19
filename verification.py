import paramiko  
  
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
  
if ssh_connect_to_windows(ip, username=username, password=password):  
    print("SSH连接成功")  
else:  
    print("SSH连接失败")
    input()