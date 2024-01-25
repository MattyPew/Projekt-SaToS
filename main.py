import time
from tinydb import TinyDB, Query
import os
import platform

version = 1

Inquiry = Query()
db = TinyDB('database.json')
cp = ["root"]

def cls():
    os.system("cls")

def mkdir(name):
    global cp
    if db.get((Inquiry.location == cp) & (Inquiry.type == "folder") & (Inquiry.name == name)):
        print(f"Directory '{name}' already exists in the current location.")
    else:
        db.insert({'type': "folder",
                   'location': cp.copy(),  # Create a copy to avoid reference issues
                   "time_created": time.time(),
                   "name": name,
                   "version": version})
        print(f"Directory '{name}' created successfully.")

def lsdir():
    global cp
    dirs = db.search((Inquiry.location == cp))
    for i in dirs:
        print(i["name"])

def cd(name):
    global cp
    if name == "..":
        if len(cp) == 1:
            print("Already on top.")
        else:
            cp.pop()
    else:
        if db.search((Inquiry.location == cp) & (Inquiry.name == name)):
            cp.append(name)
        else:
            print(f"Directory '{name}' does not exist.")

def rmdir(name):
    global cp
    location_to_remove = cp + [name]
    if not db.get((Inquiry.location == location_to_remove) & (Inquiry.type == "folder")):
        print(f"Directory '{name}' does not exist.")
    else:
        matching_documents = db.search(Inquiry.location.test(lambda x: x[:len(location_to_remove)] == location_to_remove))
        if matching_documents:
            print(matching_documents)
            for i in matching_documents:
                db.remove(Inquiry.location == i['location'])
            print(f"Directory '{name}' and its contents removed successfully.")
        else:
            print(f"No matching directories found for '{name}'.")



while True:
    location_string = ""
    for i in cp:
        location_string = location_string + i + "/"
    try:
        exec(input(f"{location_string}> "))
    except Exception as e:
        print(e)
