## import modules ##
import hashlib

sha1 = hashlib.sha1()

## compare sha1 of files ##
def compare_hash(template, output):
    with open(template, 'rb') as f:
        sha1.update(f.read())
        templateHash = sha1.hexdigest()
        

    with open(output, 'rb') as f:
        sha1.update(f.read())
        outputHash = sha1.hexdigest()
    
    if templateHash == outputHash:
        return True
    else:
        print(f'template {templateHash}')
        print(f'output {outputHash}')
        return False