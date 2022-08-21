# Importing the necessary inbuilt modules of python for finding out errors and then searching
# it automatically on web
from subprocess import Popen, PIPE
import requests
import webbrowser
from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry("1280x720")
root.title("PBL 2")
# root.attributes("-fullscreen",True)

# This is a function for running the python code file which is given in the location and then storing
# the error
def ret_error():
    global loc
    proc = Popen(loc, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    return out, err

# This function will generate the necessary json file and will make request to web browser using 
# stackexchange api 
def make_req(error):
    result = requests.get("https://api.stackexchange.com/" +
                          "/2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(error))
    return result.json()


def get_urls(json_dict):
    url_list = []
    count = 0

    for i in json_dict['items']:
        if i['is_answered']:
            url_list.append(i["link"])
        count += 1
        if count == 3 or count == len(i):
            break

# If the error has a effective and efficient solution on stackoverflow website, the web browser will
# open the tabs having the solutions related to the error
    for i in url_list:
        webbrowser.open(i)

# def quits():
#     root.destroy()

global loc

def main():
    global loc
    str1="python "
    # str2=entry.get()
    str2=root.filename
    loc=str1+str2
    out, err = ret_error()
    error = err.decode("utf-8").strip().split("\r\n")[-1]
    print(error)

    if error:
        filter_error = error.split(":")
        json1 = make_req(filter_error[0])
        json2 = make_req(filter_error[1])
        json = make_req(error)
        get_urls(json1)
        get_urls(json2)
        get_urls(json)

    else:
        print("No error")

f2=Frame(root,bg="DarkSlategray1")
f2.pack(fill="x")

l1 = Label(f2,text="Welcome to PYTHON Solutions!",font="Helvetica 20 bold",fg="red")
l1.pack(padx=10,pady=50)

l2 = Label( text="Choose your file location : ",font="Helvetica 20 bold")
l2.pack(padx=10,pady=50)

def browse():
    root.filename=filedialog.askopenfilename(initialdir="C:\pbl_python",title="select a file",filetypes=(("py files","*.py"),("all files","*.*")))
    l3=Label(f1,text=root.filename)
    l3.pack()

b2=Button(text=" Browse Files ",font="Helvetica 15 bold",command=browse)
b2.pack(pady=10)

f1=Frame(root,bg="light yellow")
f1.pack(fill="x")

b1 = Button(text=" Search ERROR ", font="Helvetica 15 bold", command=main)
b1.pack(pady=15)

def quits():
    root.destroy()

b3 = Button(text=" EXIT ", font="Helvetica 15 bold", command=quits)
b3.pack(pady=15)

root.configure(bg="light yellow")
root.mainloop()