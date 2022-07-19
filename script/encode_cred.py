## import modules ##
import base64

## encode credentials ##
def encode_cred():
    username = read_cred()[0].split(":")[0]
    password = read_cred()[0].split(":")[1]
    username = base64.b64encode(username.encode('utf-8')).decode('utf-8')
    password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    with open("../config/cred.key", "w") as f:
        f.write(str(username) + ":" + str(password))

## use credentials ##
def use_cred():
    username = read_cred()[0].split(":")[0]
    password = read_cred()[0].split(":")[1]
    username = base64.b64decode(username).decode('utf-8')
    password = base64.b64decode(password).decode('utf-8')
    return username, password

## read credentials ##
def read_cred():
    with open("../config/cred.key") as f:
        cred = f.read()
    cred = cred.split("\n")
    return cred

#if __name__ == "__main__":
#    encode_cred()
#    use_cred()
#    print(use_cred()[0])
#    print(use_cred()[1])