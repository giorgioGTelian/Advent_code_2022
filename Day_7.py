class glob(any):
    def __init__(self):
        track=[]
        fileSys=["/"]
        lines_list=[]



#def parse_line(l):



MyG=glob
with open("shortdata07.txt","r") as indata:
    lines=indata.read()
indata.close()
MyG.lines_list=lines.splitlines()
for line in MyG.lines_list:
    if line[0]=='$':
        l1=line[2:]
        if l1[0]=='c':
            if l1[3:]=="..":

            else:
                
        if l1[0]=='l':


first=MyG.lines_list.pop(0)
print(first)
