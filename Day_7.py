import sys

class glob():
# we declare track, fileSys and lines_list here, before any method and __init__,
# as class variables, not varying with each object-instance of the class
    track=[]
    fileSys=[]
    lines_list=[]
    total=0
    best_candidate=70000000
#    def __init__(self):
#        self.track=[]
#        self.fileSys=["/"]
#        self.lines_list=[]

def read_file():
    with open("/media/alberto/Data_Disk/Dropbox_Debian/Dropbox/Linux/0-MyPythonProgs/Advent of Code/07/data07.txt","r") as indata:
        lines=indata.read()
    indata.close()
    glob.lines_list=lines.splitlines()

def init_glob_vars():
    first=glob.lines_list.pop(0)
    if (first[:6] == "$ cd /"):
        glob.fileSys=[["/"]]  # main dir: begins with name of dir
        glob.track=[0]  # last item in track==index(es) of current dir in fileSys
    else:
        sys.exit("error, file doesn't begin with cd /")

def initialize():
    read_file()
    init_glob_vars()


def deep_get(l,i):
# gets the item in list l that is multidimensionally indexed by indices in list i
    for j in i:
        l=l[j]
    return(l)

def deep_set(l,v,i):
# replaces the item in list l that is multidimensionally indexed by indices in list i with item v
    for j in i[:-1]:
        l=l[j]
    l[i[-1]]=v
    return(l)


def num(s): # converts the beginning of a string up to the first space into integer
    chunk=s.split(' ')
    return(int(chunk[0]))

def cd_parent(): # makes the list of indices point to parent node
    glob.track.pop()

def cd_child(child_name):
    tmp=glob.fileSys
    search_list=deep_get(tmp,glob.track)
    i=0
    for i in range(len(search_list)):
        try: # comparison in following if is ok only if search_list[i] is a list; use try to avoid
             # deprecated type comparison 
            if search_list[i][0] == child_name:
                glob.track.append(i)
                return
        except:
            continue
    err_msg="Input error: no child name "+child_name+" exists"
    sys.exit(err_msg)


def ls_command():   # called if the last popped line is a ls command
    tmp_dir=[]
    while (glob.lines_list!=[] and glob.lines_list[0][0] != '$'):
        s=glob.lines_list.pop(0)
        if (s[:3]=="dir"):
            tmp_dir.append([s[4:]]) # if it's a dir, append list containing dir name
        else:
            tmp_dir.append(num(s))
#   The full dir has now to be added to the current dir (cur_dir + tmp_dir; cur_dir only contains
#       one item, the name of the current dir)
#   We have the index(es) of our current dir in fileSys in glob.track
    focus_list=glob.fileSys
    for i in glob.track:
        focus_list=focus_list[i]
    focus_list=focus_list + tmp_dir
    deep_set(glob.fileSys,focus_list,glob.track)


def line_process(l):
# This function is entered after l has been popped from glob.lines_list; therefore, if a cd command
# is found, another $ line is expected; if a ls command is found, a series of file/dir names is expected
# or another $ line, in case series length==0
    if (l[0]!='$'):
        sys.exit("line_process entered without $ command\n")
    l=l[2:]
    if (l[:2]=="cd"):
        l=l[3:]
        if l[:2]=="..":
            cd_parent()
        else:
            cd_child(l)
    elif (l[:2]=="ls"):
        ls_command() # in fact, all ls commands in the file don't specify a dir, they are about the current dir

def generate_structure():
    while (glob.lines_list != []):
        line_process(glob.lines_list.pop(0))    

def parse_structure(l): # using deprecated type comparisons by and large ;)
    name=l[0]
    tot_dir=0
    for i in l:
        if type(i) == int:
            tot_dir+=i
        if type(i) == list:
            tot_dir+=parse_structure(i)
        # if it's a string, just ignore it
    print("dir ",name," size = ",tot_dir)
    if (tot_dir <= 100000):
        glob.total+=tot_dir
    return(tot_dir)        

def second_part(l):
#    name=l[0]
    tot_dir=0
    for i in l:
        if type(i) == int:
            tot_dir+=i
        if type(i) == list:
            tot_dir+=second_part(i)
        # if it's a string, just ignore it
    if tot_dir >= 8381165:
        if tot_dir < glob.best_candidate:
            glob.best_candidate = tot_dir
    return(tot_dir)        


initialize()
generate_structure()
parse_structure(glob.fileSys[0]) # the root dir is the first and only element-list of glob.fileSys
print("total size = ",glob.total)
second_part(glob.fileSys[0])
print (glob.best_candidate)
#print("fileSys ",glob.fileSys, end='\n')
#print("track ",glob.track, end='\n')
