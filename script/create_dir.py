import os
import random
from pathlib import Path
from datetime import date

def check_dir(folder):
    if folder.exists():
        return True
    else:
        return False

def create_dir():
    disc = random.randint(1, 100000)
    today = date.today()
    today = today.strftime("%d%m%Y")
    folderName = today + '_' + str(disc)
    path = Path(__file__).parent.parent.resolve()
    folder = path / 'output' /folderName
    if check_dir(folder) == False:
        os.mkdir(folder)
    return folder

def create_host_dir(repport, host):
    path = Path(__file__).parent.parent.resolve()
    folder = path / 'output' / repport / host
    if check_dir(folder) == False:
        os.mkdir(folder)
    return folder