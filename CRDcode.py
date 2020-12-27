import threading 
from threading import*
import time
dict={} 
def create(key,value,timeout=0):
    if key in dict:
        print("error: this key already exists")
    else:
        if(key.isalpha()):
            if len(dict)<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    dict[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalid key_name!! key_name must contain only alphabets and no special characters or numbers")
            
def read(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        a=dict[key]
        if a[1]!=0:
            if time.time()<a[1]: #comparing the present time with expiry time
                string=str(key)+":"+str(a[0]) 
                return string
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            string=str(key)+":"+str(a[0])
            return string

def delete(key):
    if key not in dict:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        a=dict[key]
        if a[1]!=0:
            if time.time()<a[1]: 
                del dict[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del dict[key]
            print("key is successfully deleted")
