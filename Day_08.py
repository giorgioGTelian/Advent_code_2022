class glob():
    trees=[]
    tot_visible=0

def read_data():
    with open ("/media/alberto/Data_Disk/Dropbox_Debian/Dropbox/Linux/0-MyPythonProgs/Advent of Code/08/08.shortdata",'r') as dati:
        input=dati.read()
        dati.close()
        glob.trees=input.split()
