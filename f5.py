import netmiko

net_device = "linux"
net_var_ip = ["192.168.1.100"]
net_var_username =  "root"
net_var_password =  "batvv@123"

for x in net_var_ip:
    
    ssh = netmiko.ConnectHandler(device_type = net_device, ip = x, username = net_var_username, password = net_var_password)

    output = ssh.send_command("tmsh show sys software")
    
    print("Response From: ", x)

    print(output)

    ssh.disconnect()

    


