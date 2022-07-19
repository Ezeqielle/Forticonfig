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
# version: 1.7

## import modules ##
from doctest import REPORT_CDIFF
from pyfiglet import figlet_format
from termcolor import colored
from pathlib import Path

## import my funcion ##
#import compare_hash
import compare_file
import ssh_connect
import create_dir
import create_rapport
import encode_cred
import get_output
from create_rapport import PDF

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
print(f'\t{str(folder)}')
repportFolder = path = Path(__file__).parent.parent.resolve() / 'output' / folder.name

## get all template ##
print("\n")
print(colored("[+] Load all template", "cyan"))
templateFolder = path = Path(__file__).parent.parent.resolve() / 'template'
templateFile = [x for x in templateFolder.iterdir() if x.is_file()]
for x in range(len(templateFile)):
    print(f'\t{templateFile[x]}')

## test ssh connection ##
print('\n')
print(colored("[+] Starting ssh connection", "cyan"))
user = encode_cred.use_cred()[0]
password = encode_cred.use_cred()[1]
hostDict = {}
for i in range(len(ssh_connect.read_ip())):
    for x in range(len(ssh_connect.read_port())):
        attemptSsh = ssh_connect.ssh_check(ssh_connect.read_ip()[i], user, password, ssh_connect.read_port()[x])
        if attemptSsh == True:
            print(colored(f"[+] Connected on {ssh_connect.read_ip()[i]} with port {ssh_connect.read_port()[x]}", "green"))
            hostDict[ssh_connect.read_ip()[i]] = ssh_connect.read_port()[x]
            break 
        else:
            print(colored(f"[-] Connection on {ssh_connect.read_ip()[i]} with port {ssh_connect.read_port()[x]} impossible", "red"))
            print(colored(f"\tError: {attemptSsh}", "red"))

## init repport creation ##
pdf = PDF()
title = repportFolder.name
pdf.set_title(title)
create_rapport.get_title(title)

## start ssh connection ##
## get data to feed output file ##
for host, port in hostDict.items():
    pdf.new_page()
    pdf.chapter_title(str(host), str(port))
    create_dir.create_host_dir(repportFolder, host)
    ssh_connect.ssh_filtrage(host, user, password, port, repportFolder)
    ssh_connect.ssh_groups(host, user, password, port, repportFolder)
    ssh_connect.ssh_obj(host, user, password, port, repportFolder)
    usb = ssh_connect.get_usb_devices(host, user, password, port)
    ## get all output for host ##
    outputFolderContent = get_output.output_file(repportFolder, host)
    ssh_connect.get_public_ip(host, user, password, port, repportFolder)
    ## start compare output of forti with template line by line ##
    print("\n")
    print(colored(f"[§] Start comparing files for {host}", "yellow"))
    for x in range(len(templateFile)):
        templateName = templateFile[x].name
        templateName = templateName.split("_")[0]
        for y in range(len(outputFolderContent)):
            outputName = outputFolderContent[y].name
            outputName = outputName.split("_")[0]
            if templateName == outputName:
                lineArray, templateArray, outputArray, nbline = compare_file.compare_file(templateFile[x], outputFolderContent[y])
                size = len(lineArray)
                print(colored(f"[+] Starting compare files for {outputName}", "cyan"))
                if not lineArray and nbline == True:
                    conform = f'[+] The {templateName} configuration is conform'
                    print(colored('[+] The configuration is conform', 'green'))
                    pdf.chapter_body(str(conform))
                else:
                    print(colored('[-] Configuration not conform', 'red'))
                    notConform = f'[+] The {templateName} configuration is not conform'
                    pdf.chapter_body(notConform)
                    for i in range(size):
                        if outputName == "groups":
                            template = str(templateArray[i]).replace(" ", "").replace(",", "")
                            output = str(outputArray[i]).replace(" ", "").replace(",", "")
                            print(f"Line {lineArray[i]}:")
                            print("\tTemplate:", template, end="\n")
                            print("\tOutput", "\t:" , output, end="\n")
                            lineOutput = f'Line {lineArray[i]}:'
                            pdf.chapter_body(str(lineOutput))
                            pdf.chapter_body(str(templateArray[i]))
                            pdf.chapter_body(str(outputArray[i]))
                        else:
                            print(f"Line {lineArray[i]}:")
                            print("\tTemplate:", templateArray[i], end="\n")
                            print("\tOutput", "\t:" , outputArray[i], end="\n")
                            lineOutput = f'Line {lineArray[i]}:'
                            pdf.chapter_body(str(lineOutput))
                            pdf.chapter_body(str(templateArray[i]))
                            pdf.chapter_body(str(outputArray[i]))
    if usb == True:
        print(colored('[+] no usb key detected','magenta'))
        pdf.chapter_body('[+] no usb key detected')
    else:
        print(colored('[!!] usb key detected please check manually', 'red'))
        pdf.chapter_usb('[!!] usb key detected please check manually')

## export all output in a pdf ##
print("\n")
rapportFolder = path = Path(__file__).parent.parent.resolve() / 'rapports'
print(colored("[+] Starting export all output in a pdf", "cyan"))
generateRapport = pdf.output(f"{rapportFolder}/{repportFolder.name}.pdf", 'F')
print(colored(f"[+] Rapport exported", "green"))
print(f"\t{rapportFolder}\{repportFolder.name}.pdf")
print("\n")