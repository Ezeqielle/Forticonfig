import sys
import hashlib

sha1 = hashlib.sha1()

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
        return False