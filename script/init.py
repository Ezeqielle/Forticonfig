## import modules ##
import subprocess

## import my funcion ##
import encode_cred

if __name__ == "__main__":
    print("Encoding Credentials....")
    encode_cred.encode_cred()
    print("Credentials encoded\nInstalling required module....")
    cmd = 'pip install -r ../requirement.txt'
    subprocess.call(cmd, shell=True)
    print("Module installed")
    print("You can run forticonfig.py")