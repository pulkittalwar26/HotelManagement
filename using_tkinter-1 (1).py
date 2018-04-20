from tkinter import *

from tkinter import ttk

from shutil import copyfile

import os

root = Tk()

count=0



btn1=StringVar()

btn2=StringVar()



def addrec():



    f = open('open.txt', 'a')

    firstname = s1.get()

    lastname = s2.get()

    gender=btn1.get()

    rooms=s3.get()

    people=s4.get()

    startingdate=s5.get()

    endingdate=s6.get()



    finalcost = (float(endingdate)-float(startingdate))*(float(people))*100;



    f.writelines(firstname.ljust(10) + lastname.ljust(10) + gender.ljust(10) + rooms.ljust(10)+people.ljust(10)+startingdate.ljust(10)+endingdate.ljust(10)+"\n")

    f.close()





def nextrec():

    global count

    f=open('open.txt','r')

    i=0

    while(i<=count):

        l=f.readline()

        i=i+1

    list1=l.split()

    if list1.__len__() != 0:

        s1.set(list1[0])

        s2.set(list1[1])

        s3.set(list1[2])

        s4.set(list1[3])

        s5.set(list1[4])

        s6.set(list1[5])

        count = count + 1

    f.close()

    l6.config(text=count)


def search():
    fname = "db.txt"

    aid=input("Enter the Name of the Model of the phone you want to search:")
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            if words[0]==aid:
                print(line)


def prevrec():

    global count

    if count!=1:

        f=open('open.txt','r')

        i=0

        count = count - 1

        while(i<count):

            l=f.readline()

            i=i+1

        list1=l.split()

        s1.set(list1[0])

        s2.set(list1[1])

        s3.set(list1[2])

        s4.set(list1[3])

        s5.set(list1[4])

        s6.set(list1[5])

        f.close()

        l6.config(text=count)



def delete_record():

    infile = open('open.txt', 'r').readlines()

    with open('output.txt', 'w') as outfile:

        for index, line in enumerate(infile):

            if index != count-1:

                outfile.write(line)

    copyfile("output.txt","open.txt")

    os.remove("output.txt")



def show_entry_fields():

    print("Mr. FIRST NAME: %s LAST NAME: %s" % (s1.get(), s2.get()))



    people=s4.get()

    startingdate=s5.get()

    endingdate=s6.get()

    finalcost = (float(endingdate)-float(startingdate))*(float(people))*300;

    print("Your Final Amount Due is : {}".format(finalcost))





s1 = StringVar()

s2 = StringVar()

s3=StringVar()

s4=StringVar()

s5=StringVar()

s6=StringVar()



label1 = ttk.Label(root, text="FIRST NAME : ")

label1.grid(row=0,pady=4)



l2 = Label(root, text="LAST NAME : ")

l2.grid(row=1,pady=4)



l3 = Label(root, text="Number of Rooms")

l3.grid(row=2,pady=4)



l4=Label(root,text="AC OR NON AC :")

l4.grid(row=3,column=0)



l5=Radiobutton(root,text="AC",value="AC",variable=btn1)

l5.grid(row=3,column=1)



l6=Radiobutton(root,text="NON AC",value="NON AC",variable=btn1)

l6.grid(row=3,column=2)



l7 = Label(root, text="Number of People")

l7.grid(row=4,column=0,pady=4)



l8 = Label(root, text="Starting Date")

l8.grid(row=5,column=0,pady=4)



l9 = Label(root, text="Ending Date")

l9.grid(row=6,column=0,pady=4)



l10 = Label(root, text="*** PLEASE NOTE : COST PER DAY PER HEAD IS RS 300 ***")

l10.grid(columnspan=2,row=7,column=0,pady=4)















e1 = Entry(root,textvariable=s1)

e1.grid(row=0, column=1,pady=4)



e2 = Entry(root,textvariable=s2)

e2.grid(row=1, column=1,pady=4)



e3 = Entry(root,textvariable=s3)

e3.grid(row=2, column=1,pady=4)



e4 = Entry(root,textvariable=s4)

e4.grid(row=4, column=1,pady=4)



e5 = Entry(root,textvariable=s5)

e5.grid(row=5, column=1,pady=4)



e6 = Entry(root,textvariable=s6)

e6.grid(row=6, column=1,pady=4)



Button(root, text='Quit', command=root.quit).grid(row=8, column=0, sticky=W, pady=4)

Button(root, text='SHOW', command=show_entry_fields).grid(row=8, column=1, sticky=W, pady=4)

Button(root, text='ADD', command=addrec).grid(row=8, column=2, sticky=W, pady=4)

Button(root, text='>', command=nextrec).grid(row=8, column=3, sticky=W, pady=4)

Button(root, text='<', command=prevrec).grid(row=8, column=4, sticky=W, pady=4)

Button(root, text='DELETE', command=delete_record).grid(row=8, column=5, sticky=W, pady=4)

Button(root, text='SEARCH', command=delete_record).grid(row=8, column=6, sticky=W, pady=4)

root.mainloop()

