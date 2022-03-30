## import modules ##
import paramiko

## check if host can be reached ##
def ssh_check(host, user, password, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password, port=port)
        return True
    except Exception as e:
        return e

## read host ##
def read_ip():
    with open("../config/ip.cfg") as f:
        ip = f.read()
    ip = ip.split("\n")
    del ip[0]
    return ip

## read port ##
def read_port():
    with open("../config/port.cfg") as f:
        port = f.read()
    port = port.split("\n")
    del port[0]
    return port

## read credentials ##
def read_cred():
    with open("../config/cred.key") as f:
        cred = f.read()
    cred = cred.split("\n")
    return cred

## send command and get return ##

## parsing command output ##