import requests
import json
from urllib import request
from urllib3.exceptions import InsecureRequestWarning
#requests.package.urllib3.disable_warnings(category=InsecureRequestWarning)

var_device_ip = "192.168.1.100"
username1 = 'root'
password = 'batvv@123'

data = {
    "username":"admin",
    "password":"batvv@123",
    "loginProviderName": "tmos"
}


f5_auth_endpoint = "https://"+var_device_ip+"/mgmt/shared/authn/login"

f5_auth_endpoint_response =  requests.post(f5_auth_endpoint, json= data, verify = False).json()

print(f5_auth_endpoint_response)
f5_auth_token = f5_auth_endpoint_response["token"]["token"]
print(f5_auth_token)

heads = {
    "Content-Type": "application/json",
    "X-F5-Auth-Token": f5_auth_token
}

f5_version_endpoint = "https://"+var_device_ip+"/mgmt/tm/sys/version"

f5_version_endpoint_response =  requests.get(f5_version_endpoint, headers = heads,verify = False).json()
print(f5_version_endpoint_response)

var_f5_version = f5_version_endpoint_response["entries"]["https://localhost/mgmt/tm/sys/version/0"]["nestedStats"]["entries"]["Version"]["description"]

print(var_f5_version)



