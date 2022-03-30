#!/usr/bin/python3

#    ______         _   _    _____             __ _       
#   |  ____|       | | (_)  / ____|           / _(_)      
#   | |__ ___  _ __| |_ _  | |     ___  _ __ | |_ _  __ _ 
#   |  __/ _ \| '__| __| | | |    / _ \| '_ \|  _| |/ _` |
#   | | | (_) | |  | |_| | | |___| (_) | | | | | | | (_| |
#   |_|  \___/|_|   \__|_|  \_____\___/|_| |_|_| |_|\__, |
#                                                    __/ |
#                                                   |___/ 

# Devloppers: Ezeqielle
# Description: This script is a simple script that will be used to check fortigate configuration and compare it with the configuration template.
# version: 0.1

## import modules ##
from pyfiglet import figlet_format
from termcolor import colored
from pathlib import Path

## import my funcion ##
import compare_hash
import compare_file
import ssh_connect
import create_dir
import create_rapport

## for color work on windows ##
import colorama
colorama.init()
print(colorama.ansi.clear_screen())

## ascii art ##
print(figlet_format("Forti Config", font="big"))

## create a dir with discriminator+date ##
print(colored("[+] Creating a dir for export", "cyan"))
folder = create_dir.create_dir()
print(colored("[+] Dir created", "green"))
print(colored("\tDir path: " + str(folder), "green"))

## test ssh connection ##
#print(colored("[+] Starting ssh connection", "cyan"))
#user = ssh_connect.read_cred()[0].split(":")[0]
#password = ssh_connect.read_cred()[0].split(":")[1]
#hostDict = {}
#for i in range(len(ssh_connect.read_ip())):
#    for x in range(len(ssh_connect.read_port())):
#        attemptSsh = ssh_connect.ssh_check(ssh_connect.read_ip()[i], user, password, ssh_connect.read_port()[x])
#        if attemptSsh == True:
#            print(colored(f"[+] Connected on {ssh_connect.read_ip()[i]} with port {ssh_connect.read_port()[x]}", "green"))
#            hostDict[ssh_connect.read_ip()[i]] = ssh_connect.read_port()[x]
#            break 
#        else:
#            print(colored(f"[-] Connection on {ssh_connect.read_ip()[i]} with port {ssh_connect.read_port()[x]} impossible", "red"))
#            print(colored(f"\tError: {attemptSsh}", "red"))
#print(f"{hostDict}")

## start ssh connection ##

## get data to feed output file ##

## get all template and output ##
print("\n")
print(colored("[+] Get all template and output files", "cyan"))

## get all template and output ##
templateFolder = path = Path(__file__).parent.parent.resolve() / 'template'
templateFile = [x for x in templateFolder.iterdir() if x.is_file()]
for x in range(len(templateFile)):
    print(templateFile[x])

#outputFolder = path = Path(__file__).parent.parent.resolve() / 'output' / folder.name
outputFolder = path = Path(__file__).parent.parent.resolve() / 'output' / "29032022_79101"
outputFile = [x for x in outputFolder.iterdir() if x.is_file()]
for x in range(len(outputFile)):
    print(outputFile[x])

## compare hash of template and output ##
for x in range(len(templateFile)):
    templateName = templateFile[x].name
    templateName = templateName.split("_")[0]
    for y in range(len(outputFile)):
        outputName = outputFile[y].name
        outputName = outputName.split("_")[0]
        if templateName == outputName:
            templateHash = compare_hash.compare_hash(templateFile[x], outputFile[y])
            if templateHash == True:
                print(colored("\n[+] Starting compare the hash of forti output with template", "cyan"))
                print(colored(f"[+] File are the same for {outputName}", "green"))
            else:
                print(colored("\n[+] Starting compare of forti output with template", "cyan"))
                print(colored(f"[-] File are different for {outputName}", "red"))
                ## start compare output of forti with template line by line ##
                lineArray, templateArray, outputArray = compare_file.compare_file(templateFile[x], outputFile[y])
                size = len(lineArray)
                #print(outputArray)
                print(colored(f"[+] Starting compare files for {outputName}", "cyan"))
                for i in range(size):
                    if outputName == "groups":
                        template = str(templateArray[i]).replace(" ", "").replace(",", "")
                        output = str(outputArray[i]).replace(" ", "").replace(",", "")
                        print(f"Line {lineArray[i]}:")
                        print("\tTemplate:", template, end="\n")
                        print("\tOutput", "\t:" , output, end="\n")
                    else:
                        template = str(templateArray[i]).split("[")[1].split("]")[0]
                        output = str(outputArray[i]).split("[")[1].split("]")[0]
                        print(f"Line {lineArray[i]}:")
                        print("\tTemplate:", template, end="\n")
                        print("\tOutput", "\t:" , output, end="\n")

## export all output in a pdf ##
print("\n")
print(colored("[+] Starting export all output in a pdf", "cyan"))
generateRapport = create_rapport.generate_rapport(outputFolder.name)
print(colored(f"[+] Rapport exported in {generateRapport}/{outputFolder.name}.pdf", "green"))
print("\n")