## import modules ##
from pathlib import Path

def parse_output(output):
    if 'WARNING' in output[0]:
        del output[0:4]
        del output[len(output)-2]
        del output[len(output)-1]
    output[0] = output[0].split("$")
    output[0] = output[0][1].lstrip(' ')
    if 'Unknown' in output[0]:
        del output[0:5]
        for i in range(1,3):
            del output[len(output)-i]
    if '(global)' in output[1]:
        del output[0]
        output[0] = output[0].split('$')
        output[0] = output[0][1].lstrip(' ')
    del output[len(output)-1]
    return output

def parse_usb(output):
    if 'WARNING' in output[0]:
        del output[0:4]
        del output[len(output)-2]
        del output[len(output)-1]
    output[0] = output[0].split("$")
    output[0] = output[0][1].lstrip(' ')
    for x in range(len(output)):
        if "unable" in output[x]:
            count = 1
        else:
            continue
    if count == 1:
        return True
    else:
        return False

## clean file of useless lines ##
def clean_filtrage(file, host):
    pathToFilter = Path(__file__).parent.parent.resolve() / 'output' / host / file
    with open(pathToFilter, "r") as f:
        lines = f.readlines()
    with open(pathToFilter, "w") as f:
        for line in lines:
            if "$" not in line:
                if "uuid" not in line:
                    if "comments" not in line:
                        if "next" not in line:
                            f.write(line)
    with open(pathToFilter) as f:
        lines = f.readlines()
    with open(pathToFilter, 'w') as f:
        lines = filter(lambda x: x.strip(), lines) #remove empty lines with filter function
        f.writelines(lines)

def clean_groups(file, host):
    pathToFilter = Path(__file__).parent.parent.resolve() / 'output' / host / file
    with open(pathToFilter, "r") as f:
        lines = f.readlines()
    with open(pathToFilter, "w") as f:
        for line in lines:
            if "member" in line:
                f.write(line)
    with open(pathToFilter) as f:
        lines = f.readlines()
    with open(pathToFilter, 'w') as f:
        lines = filter(lambda x: x.strip(), lines) #remove empty lines with filter function
        f.writelines(lines)

def clean_obj(file, host):
    pathToFilter = Path(__file__).parent.parent.resolve() / 'output' / host / file
    with open(pathToFilter, "r") as f:
        lines = f.readlines()
    with open(pathToFilter, "w") as f:
        for line in lines:
            if "edit" in line or "subnet" in line:
                f.write(line)
    with open(pathToFilter) as f:
        lines = f.readlines()
    with open(pathToFilter, 'w') as f:
        lines = filter(lambda x: x.strip(), lines) #remove empty lines with filter function
        f.writelines(lines)

def clean_public(file, repport):
    listIp = []
    pathToFilter = Path(__file__).parent.parent.resolve() / 'output' / repport / file
    with open(pathToFilter, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if 'ip' in line:
                linesNext = line.split(" ")
                linesNext = list(filter(None, linesNext))
                for x in range(len(linesNext)):
                    if 'management-ip:' in linesNext[x]:
                        del(linesNext[x+2])
                        del(linesNext[x+1])
                        del(linesNext[x])
                tmpIp = linesNext[5]
                tmpMask = linesNext[6]
                concat = tmpIp + ':' + tmpMask
                listIp.append(concat)
        for x in range(len(listIp)):
            if '0.0.0.0' in listIp[x]:
                del(listIp[x])
        pathCleaned = Path(__file__).parent.parent.resolve() / 'output' / repport / 'public.txt'
        with open(pathCleaned, 'a') as f:
            for x in range(len(listIp)):
                f.write(listIp[x] + "\n")

#if __name__ == '__main__':
#    clean_file('filtrage.txt')