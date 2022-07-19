## import modules ##
from pathlib import Path

def output_file(repport, host):
    outputFolder = path = Path(__file__).parent.parent.resolve() / 'output' / repport / host 
    outputFiles = [x for x in outputFolder.iterdir() if x.is_file()]
    return outputFiles