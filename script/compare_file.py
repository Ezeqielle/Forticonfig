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
    return lineArray, templateArray, outputArray
    templateFile.close()
    outputFile.close()