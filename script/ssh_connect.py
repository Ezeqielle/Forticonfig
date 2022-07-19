## import modules ##
import paramiko
from pathlib import Path

## my module ##
import cleaner
import encode_cred

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

## send command and get return ##
def ssh_filtrage(host, user, password, port, repport):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password, port=port)
        bashScript = open('sh/filtrage.sh').read()
        stdin, stdout,stderr = ssh.exec_command(bashScript)
        output = stdout.readlines()
        outputClean = cleaner.parse_output(output)
        filePath = Path(__file__).parent.parent.resolve() / 'output' / repport / host / "filtrage_output.txt"
        file = open(filePath, 'w')
        for x in range(len(outputClean)):
            if x == (len(outputClean)-1):
                outputClean[x] = outputClean[x].lstrip(" ")
                outputClean[x] = outputClean[x].strip()
            else:
                outputClean[x] = outputClean[x].lstrip(" ")
            file.write(outputClean[x])
        file.close()
        cleaner.clean_filtrage(filePath, host)
    except Exception as e:
        return e
    ssh.close()

def ssh_groups(host, user, password, port, repport):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password, port=port)
        bashScript = open('sh/groups.sh').read()
        stdin, stdout,stderr = ssh.exec_command(bashScript)
        output = stdout.readlines()
        outputClean = cleaner.parse_output(output)
        filePath = Path(__file__).parent.parent.resolve() / 'output' / repport / host / "groups_output.txt"
        file = open(filePath, 'w')
        for x in range(len(outputClean)):
            if x == (len(outputClean)-1):
                outputClean[x] = outputClean[x].lstrip(" ")
                outputClean[x] = outputClean[x].strip()
            else:
                outputClean[x] = outputClean[x].lstrip(" ")
            file.write(outputClean[x])
        file.close()
        cleaner.clean_groups(filePath, host)
    except Exception as e:
        return e
    ssh.close()

def ssh_obj(host, user, password, port, repport):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password, port=port)
        objCommands = Path(__file__).parent.parent.resolve() / 'script' / 'sh' / 'obj'
        objFiles = [x for x in objCommands.iterdir() if x.is_file()]
        for x in range(len(objFiles)):
            bashScript = open(objFiles[x]).read()
            stdin, stdout,stderr = ssh.exec_command(bashScript)
            output = stdout.readlines()
            outputClean = cleaner.parse_output(output)
            filePath = Path(__file__).parent.parent.resolve() / 'output' / repport / host / "obj_output.txt"
            make_obj_file(outputClean,filePath,host)

    except Exception as e:
        return e
    ssh.close()
def make_obj_file(outputClean, filePath, host):
    file = open(filePath, 'a')
    for x in range(len(outputClean)):
        if x == (len(outputClean)-1):
            outputClean[x] = outputClean[x].lstrip(" ")
            outputClean[x] = outputClean[x].strip()
        else:
            outputClean[x] = outputClean[x].lstrip(" ")
        file.write(outputClean[x])
    file.close()
    cleaner.clean_obj(filePath, host)

## get usb devices ##
def get_usb_devices(host, user, password, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password, port=port)
        bashScript = open('sh/usb.sh').read()
        stdin, stdout, stderr = ssh.exec_command(bashScript, get_pty=True)
        output = stdout.readlines()
        outputClean = cleaner.parse_usb(output)
        return outputClean
    except Exception as e:
        return e
    ssh.close()

## get public ip ##
def get_public_ip(host, user, password, port, repport):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, username=user, password=password, port=port)
        bashScript = open('sh/public.sh').read()
        stdin, stdout,stderr = ssh.exec_command(bashScript)
        output = stdout.readlines()
        outputClean = cleaner.parse_output(output)
        filePath = Path(__file__).parent.parent.resolve() /'output' / repport / 'tmp.txt'
        file = open(filePath, 'a')
        for x in range(len(outputClean)):
            if x == (len(outputClean)-1):
                outputClean[x] = outputClean[x].lstrip(" ")
                outputClean[x] = outputClean[x].strip()
            else:
                outputClean[x] = outputClean[x].lstrip(" ")
            file.write(outputClean[x])
        file.close()
        #cleaner.clean_public(filePath, repport)
    except Exception as e:
        return e
    ssh.close()

## test function ##
#if __name__ == "__main__":
    #print("\n")
    #print("[+] Starting ssh connection")
    #user = encode_cred.use_cred()[0]
    #password = encode_cred.use_cred()[1]
    #repport = '09052022_21853'
    #attemptCommand = get_usb_devices(read_ip()[0], user, password, read_port()[0])
    #attemptCommand = get_public_ip(read_ip()[1], user, password, read_port()[1], repport)
    #if 'WARNING' in attemptCommand[0]:
    #    del attemptCommand[0:4]
    #attemptCommand[0] = attemptCommand[0].split("$")
    #attemptCommand[0] = attemptCommand[0][1].replace(" Version","Version")
    #for x in  range(len(attemptCommand)):
    #    print(f'{attemptCommand[x]}\n')
    #print(attemptCommand)