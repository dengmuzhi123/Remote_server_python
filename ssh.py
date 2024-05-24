import paramiko  
  
def ssh_connect_and_get_os(ip, username, password):  
      
    ssh = paramiko.SSHClient()  
   
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
      
    try:  

        ssh.connect(ip, username=username, password=password)  

        stdin, stdout, stderr = ssh.exec_command('systeminfo | findstr /B /C:"OS Name')  
          

        output = stdout.read().decode().strip()  
          
  
        ssh.close()  
   
        return output  
    except paramiko.AuthenticationException:  
        print("Authentication failed, please verify your credentials")  
    except paramiko.SSHException as sshException:  
        print("Unable to establish SSH connection: %s" % sshException)  
    except paramiko.BadHostKeyException as badHostKeyException:  
        print("Unable to verify server's host key: %s" % badHostKeyException)  
    except Exception as e:  
        print("An error occurred: %s" % e)  
      
    return None  
  
ip = "192.168.0.2"  
username = "administrator"  
password = "123deng123/"  
os_name = ssh_connect_and_get_os(ip, username, password)  

print("The server's operating system is:", os_name)


