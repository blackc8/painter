import platform, sys, os, math
columns, rows = os.get_terminal_size(0)

ncol   ="\033[0m"
bold   ="\033[1m"
dim    ="\033[2m"
uline  ="\033[4m"
reverse="\033[7m"
red    ="\033[31m"
green  ="\033[32m"
yellow ="\033[33m"
blue   ="\033[34m"
purple ="\033[35m"
cyan   ="\033[36m"
white  ="\033[37m"

if platform.system == "Windows":
    ncol=bold=dim=uline=red=green=yellow=blue=purple=cyan=white=''

def eint(str):
    if str == "": return 0
    intgr = []
    for char in str:
        if char.isdigit():
            intgr.append(char)
    if intgr == []: return 0
    return int("".join(intgr))

def label(labelName):
    print(reverse+bold+cyan+labelName+ncol)

def head(name):
    print(bold+uline+name+ncol)

def addPad(text,color=''):
    print(color+"  "+text.replace("\n","\n  ")+ncol)

def addLog(symbol,color,text,end='\n',flush=True):
    print(dim+bold+color+symbol+ncol+bold+color+text+ncol,end=end,flush=flush)

def desc(text,color=''):
    addPad(text,color=color)

def cSym(pre,symbol,post,color):
    return ncol+dim+color+pre+ncol+bold+color+symbol+ncol+dim+color+post+ncol

def blt(text):
    addLog(cSym('[','*',']',purple)+' ',purple,bold+purple+text)

def scs(text,end='\n',flush=True):
    addLog(cSym('[','+',']',green)+' ',green,text,end=end,flush=flush)

def err(text):
    addLog(cSym('[','-',']',red)+' ',red,text)

def wrn(text,end='\n',flush=True):
    addLog(cSym('[','!',']',yellow)+' ',yellow,text,end=end,flush=flush)

def say(text):
    print("   "+text+ncol)

def ask(text,default='',type='str',show=False,force=False):
    inp=""
    while inp=="":
      if not text=="":addLog(cSym('[','?',']',blue)+' ',blue,text,end='',flush=False)
      inp=input()
      if not force: break

    if inp == "": inp=str(default)
    if type == 'int': inp=eint(inp)
    if show: print(bold+cyan+"  ==> "+ncol+str(inp))
    return inp

def inp(text):
    print(bold+blue+text+ncol,flush=False,end='')
    return ask('')

