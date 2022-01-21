import os
import zipfile
from pathlib import Path
from tkinter import filedialog
from tkinter import *
import getpass
import socket
username = getpass.getuser()
wksname = socket.gethostname()
root = Tk()
root.geometry("500x430+1300+550")
root.config(bg="white")
header1 = LabelFrame(root, text="", borderwidth=0, bg="darkblue")
header1.grid(row=0, column=0, columnspan=10, sticky='ew')

labeloben = Label(header1, text="Alstertech Clienttool Backup Modul", height=1, bg="darkblue", fg="White",
                  font=("Helvetica", 14))
labeloben.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
labeloben = Label(header1, text="", height=1, bg="darkblue", fg="White", font=("Helvetica", 14), width=20)
labeloben.grid(row=0, column=1, padx=5, pady=5, columnspan=3, sticky="nsew")
overframe = LabelFrame(root, text="", borderwidth=0, bg="white")
overframe.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
labelwhichback = Label(overframe, text="Bitte Quelle wählen", height=1, bg="white", fg="blue", font=("Helvetica", 14), width=20)
labelwhichback.grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky="nsew")
labelpath = Label(overframe, text="Gewählter Pfad", height=1, bg="white", fg="blue",
                 font=("Helvetica", 14))
labelpath.grid(row=2, column=0, padx=5, pady=5, columnspan=2, sticky="nsew")



def userbackup():
    global backuppath
    backuppath = Path.home()
    director = Label(overframe, text=backuppath, height=1, bg="white", fg="blue",
                           font=("Helvetica", 14), width=16)
    director.grid(row=3, column=0, padx=5, pady=5,sticky="nsew", columnspan=2)
    def get_size(start_path=backuppath):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

        return total_size
    sizeget = get_size() / 1000000
    sizeget = int(sizeget)
    sizeget = str(sizeget)
    print(sizeget)
    sizeoffiles = Label(overframe, text="Größe: " + sizeget + " MB", height=1, bg="white", fg="blue",
                           font=("Helvetica", 14), width=16)
    sizeoffiles.grid(row=4, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
nutzerback = Button(overframe, text="Nutzer Backup", command=userbackup, font=('Helvetica', 14), bg="white", fg="blue", borderwidth=2,
                         relief="groove", width=20)
nutzerback.grid(row=1, column=0)
def otherbackup():
    global backuppath
    backuppath = filedialog.askdirectory()
    director = Label(overframe, text=backuppath, height=1, bg="white", fg="blue",
                           font=("Helvetica", 14), width=16)
    director.grid(row=3, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)

    def get_size(start_path=backuppath):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

        return total_size
    sizeget = get_size() / 1000000
    sizeget = int(sizeget)
    sizeget = str(sizeget)
    print(sizeget)
    sizeoffiles = Label(overframe, text="Größe: " + sizeget + " MB", height=1, bg="white", fg="blue",
                           font=("Helvetica", 14), width=16)
    sizeoffiles.grid(row=4, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
otherback = Button(overframe, text="Anderes Backup", command=otherbackup, font=('Helvetica', 14), bg="white", fg="blue", borderwidth=2,
                         relief="groove", width=20)
otherback.grid(row=1, column=1)

def goalpath():
    global thegoalpath
    thegoalpath = filedialog.askdirectory()
    directorfinal = Label(overframe, text=thegoalpath, height=1, bg="white", fg="blue",
                           font=("Helvetica", 14), width=16)
    directorfinal.grid(row=6, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
zielpfad = Button(overframe, text="Zielpfad", command=goalpath, font=('Helvetica', 14), bg="white", fg="blue", borderwidth=2,
                         relief="groove", width=20)
zielpfad.grid(row=5, column=0,columnspan=2)

def finalbackup():
    zf = zipfile.ZipFile(thegoalpath + r"/" + wksname + "-" + username + ".zip", "w")
    thepath = thegoalpath + r"/" + wksname + "-" + username + ".zip"
    for dirname, subdirs, files in os.walk(backuppath):
        # zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname, filename))
    zf.close()
    readyfinal = Label(overframe, text="Backup erfolgreich " + thepath, height=1, bg="white", fg="blue",
                           font=("Helvetica", 14), width=16)
    readyfinal.grid(row=8, column=0, padx=5, pady=5, sticky="nsew", columnspan=2)
startback = Button(overframe, text="Start Backup", command=finalbackup, font=('Helvetica', 14), bg="white", fg="blue", borderwidth=2,
                         relief="groove", width=20)
startback.grid(row=7, column=0,columnspan=2)


root.mainloop()
"""
#region Auf C:\Alstertech\Module entpacken

ze = zipfile.ZipFile(r"C:\Alstertech\Clienttool.zip", "r")
with ze as zipobj:
    zipobj.extractall('C:\Alstertech\Module')
"""
#endregion