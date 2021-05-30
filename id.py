from tkinter import *

import random 

root=Tk()
root.geometry("500x500")
root.title("Forever Black - Lucky Black Ranger")

enter_ranger=Entry(root)
enter_ranger.place(relx=0.5, rely=0.2, anchor= CENTER)
list_label=Label(root)
random_num_label=Label(root)
luckyranger_label=Label(root)
list1=[]
def addrangger ():
    addranger=enter_ranger.get()
    list1.append(addranger)
    list_label["text"]="Your Rangers are : " + str(list1)
    enter_ranger.delete(0,END)
    
def lucckyranger():
    length=len(list1)
    random_no=random.randint(0,length-1)
    random_num_label["text"]= str(random_no)
    raanger=list1[random_no]
    luckyranger_label["text"]= "Your lucky Ranger is : " + raanger

btn1=Button(root,text="Add your Rangers", command=addrangger)
btn2=Button(root,text="Find the Lucky Ranger", command=lucckyranger)
btn1.place(relx=0.5, rely=0.3, anchor=CENTER)
list_label.place(relx=0.5, rely=0.4, anchor=CENTER)
btn2.place(relx=0.5, rely=0.5, anchor=CENTER)
random_num_label.place(relx=0.5, rely=0.6, anchor=CENTER)
luckyranger_label.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()