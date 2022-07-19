## compare files content ##
def compare_file(template, output):
    i = 0
    
    templateArray = []
    lineArray = []
    outputArray = []

    outputFile = open(output, "r")
    templateFile = open(template, "r")

    for line1 in templateFile:
        i += 1
        for line2 in outputFile:
            if line1 != line2:
                lineArray.append(i)
                templateArray.append(line1)
                outputArray.append(line2)
            break

    temp = templateFile.readlines()
    out = outputFile.readlines()
    if len(temp) == len(out):
        nbline = True
    else:
        nbline = False
    return lineArray, templateArray, outputArray, nbline
    templateFile.close()
    outputFile.close()