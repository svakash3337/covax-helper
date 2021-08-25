import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import font
from tkinter.font import Font
from tkinter import ttk
import sys
from sql import *
import re

# TODO add more hospitals -
# TODO add page taht shows location of chosen hospital
# TODO add "Check Occupancy" feature on book11
# TODO hover interactions
# TODO debug the program
# TODO make the UI better
# TODO add random lines for extra credit
# TODO REDACTED

# areo = Selected area,
# general variables reused multiple times in the program are here:
strg = tkinter.StringVar
h = 0
root = Tk()
screen_width = root.winfo_screenwidth()  # this is a function used to get width of the computer running windows
sw = screen_width / 2
screen_height = root.winfo_screenheight()
sh = screen_height / 2
appw = 1280
apph: int = 720
backg = PhotoImage(file="E:\d.png")
rootbool = False

x = int(sw - (appw / 2))
# this is used to position the app widget relative to the resolution of whatever monitor it's running on
y = int(sh - (apph / 2))
# xn=int(appw+x) deprecated
# xy=int(apph+y) deprecated
geo = f'{appw}x{apph}+{x}+{y}'

print(geo)  # debugging for window width/height

# main window
root.title('CoVax Helper')
root.geometry(geo)
label1 = Label(root, image=backg)
label1.place(x=0, y=0)
txt1 = Label(root, text="Welcome to Covax Helper", bg='#ffffff')
# txt2 = Label(root, text= "Covax Helper", bg='#e9f2f9')
txt3 = Label(root, text="I want to..", bg='#ddeaf6')

# globally used font definitions
fint = font.Font(family='Mont ExtraLight DEMO', size=20)
fynt: Font = font.Font(family='Mont ExtraLight DEMO', size=25)
fent = font.Font(family='Mont ExtraLight DEMO', size=35)
txt1['font'] = fent
# txt2['font']=fint
txt3['font'] = fynt
if not rootbool:
    txt1.pack(pady=30)
# txt2.pack()
txt3.pack(pady=30)
boo1 = 0


# BOOKING SECTION START
def nwback():
    endwindow.root3.withdraw()
    mmenu()


def endwindow():
    endwindow.root3 = Toplevel()
    ui = endwindow.root3
    endwindow.root3.geometry(geo)
    label1 = Label(ui, image=backg)
    label1.place(x=0, y=0)
    top = Frame(endwindow.root3, bg='#bad5ed')
    bottom = Frame(endwindow.root3, bg='#bad5ed')
    top.pack(pady=10)
    bottom.pack()
    t1 = Label(endwindow.root3, text="Thank you for using CoVax Helper.", bg='#bad5ed')
    t1['font'] = fent
    b2 = Button(endwindow.root3, text="Go back to main menu", bg='#bad5ed', command=nwback)
    b3 = Button(ui, text="Exit", bg='#bad5ed', command=die)
    b2['font'] = fynt
    b3['font'] = fynt
    t1.pack(in_=top, pady=10)
    b2.pack(in_=top, pady=10)
    b3.pack(in_=top, pady=10)


def kill():  # gives you the referral code for search function
    test = Tk()
    test.withdraw()
    msg = "Your appointment has been booked." + " Please note this code down to " \
                                                "use for referral: \n " + "'" + str(bookcommit.searchcode) + \
          "'\n Would you like to copy this code to your clipboard?"
    copy = tkinter.messagebox.askquestion("Booking Complete", msg)
    test.withdraw()
    if copy == 'yes':
        test.clipboard_append(bookcommit.searchcode)
        tkinter.messagebox.showinfo("Booking Complete", "Code copied to clipboard.")
    test.withdraw()
    finalbook.new.withdraw()
    endwindow()


def bookcommit():  # this is where icall the sql file to make changes to database

    area = ''
    uid = 0
    ar = 0
    print("please work ty")
    areo = book11.area.get()
    hospital = area_caller.hospitals.get()
    name = finalbook.text1.get(1.0, "end-1c")
    if re.search('.+wrong.+', name) or name in ['test', 'lol', 'yes', 'no', 'sussy', 'sus', 'impostor']:
        tkinter.messagebox.showwarning('INCORRECT NAME', 'Please enter a real name.')
        hospital = 'sabotage!!!!!!!!!'
        wrong = True

    else:
        wrong = False
    namecheck = name.replace(' ', '')
    if not namecheck.isalpha():  # check if it is proper to sanitize input. we don't want bobby tables here
        tkinter.messagebox.showwarning("INCORRECT NAME", "Please enter a proper name without special characters.")
        sys.exit()
    else:
        wrong = False
    age = finalbook.text2.get(1.0, "end-1c")
    if not age.isnumeric() or int(age) >= 120 or int(age) <= 0 or int(age) <= 18:
        tkinter.messagebox.showwarning("REATARD", "Please enter your real age as a number.")
    else:
        wrong = False
    gender = finalbook.text3.get()
    print(gender)
    vax = finalbook.text4.get()
    print(vax)
    if not wrong:
        if areo == "North Chennai":
            ar = 1
            area = "northchennai"
            uid = sqlfunc(area, hospital, name, age, gender, vax)
        elif areo == "Central Chennai":
            ar = 2
            area = "centralchennai"
            uid = sqlfunc(area, hospital, name, age, gender, vax)
        elif areo == "South Chennai":
            ar = 3
            area = "southchennai"
            uid = sqlfunc(area, hospital, name, age, gender, vax)
    print(uid, name, age, gender, vax, area)
    bookcommit.q = uid
    bookcommit.searchcode = str(ar) + '--' + str(hospital) + '--' + str(uid)
    if bookcommit.searchcode[0] == '0':
        print("screwup")
        finalbook.new.withdraw()
        finalbook('<<ComboboxSelected>>')
    else:
        kill()


# noinspection PyUnusedLocal
def finalbook(event):  # get details of patient and add to table finally
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground="#bad5ed", background="#bad5ed")
    print("data time")
    old = book11.root3
    old.withdraw()
    finalbook.new = Toplevel()
    ui = finalbook.new
    ui.geometry(geo)
    label1 = Label(ui, image=backg)
    label1.place(x=0, y=0)
    tl1 = Label(ui, text="Enter your name:", bg='#bad5ed')
    finalbook.text1 = Text(ui, height=2, width=40, bg='#bad5ed')
    tl2 = Label(ui, text="Enter age:", bg='#bad5ed')
    finalbook.text2 = Text(ui, height=2, width=40, bg='#bad5ed')
    tl3 = Label(ui, text="Enter gender (M or F):", bg='#bad5ed')
    finalbook.text3 = ttk.Combobox(ui, width=40, textvariable=strg)
    tl4 = Label(ui, text="Choose vaccine:", bg='#bad5ed')
    finalbook.text4 = ttk.Combobox(ui, width=40, textvariable=strg)
    finalbook.text3['values'] = ('M', 'F')
    finalbook.text3['state'] = 'readonly'
    finalbook.text4['values'] = ('Covaxin', 'Covishield')
    finalbook.text4['state'] = 'readonly'
    btn = Button(ui, text="Submit", bg='#bad5ed', command=bookcommit)
    btn['font'] = fint
    tl1['font'] = fynt
    tl2['font'] = fynt
    tl3['font'] = fynt
    tl4['font'] = fynt
    tl1.place(x=sw / 8, y=sh / 8)  # relative positioning, better than grid positioning but more work less flexibility
    tl2.place(x=sw / 8, y=sh / 8 + sh / 10)
    tl3.place(x=sw / 8, y=sh / 8 + sh / 5)
    tl4.place(x=sw / 8, y=sh / 8 + sh / 3)
    finalbook.text1.place(x=sw / 2, y=sh / 8)
    finalbook.text2.place(x=sw / 2, y=sh / 8 + sh / 10)
    finalbook.text3.place(x=sw / 2, y=sh / 8 + sh / 5)
    finalbook.text4.place(x=sw / 2, y=sh / 8 + sh / 3)
    btn.place(x=sw - (appw / 3.5), y=sh - (apph / 4))


# noinspection PyUnusedLocal
def ac_caller(event):
    area_caller()


def book11():  # book widget 2
    print("gg")
    book11.root3 = Toplevel()
    ui = book11.root3
    book11.root3.geometry(geo)
    label1 = Label(ui, image=backg)
    label1.place(x=0, y=0)
    top = Frame(book11.root3)
    bottom = Frame(book11.root3)
    top.pack(pady=10)
    bottom.pack()
    t1 = Label(book11.root3, text="Welcome to our booking system")
    t1['font'] = fent
    t2 = Label(book11.root3, text="Enter area:")
    book11.area = ttk.Combobox(book11.root3, width=100, textvariable=strg)
    book11.area['state'] = 'readonly'
    book11.area['values'] = ('North Chennai', 'Central Chennai', 'South Chennai')
    t2['font'] = fynt
    t1.pack(in_=top, pady=10)
    t2.pack(in_=top, pady=10)
    book11.area.pack()
    book11.area.bind('<<ComboboxSelected>>', ac_caller)


def area_caller():  # give them a hospital list depending on area, part of book widget 2
    areo = book11.area.get()
    ui = book11.root3
    area_caller.hospitals = ttk.Combobox(ui, width=100, textvariable=strg)
    area_caller.hospitals['state'] = 'readonly'
    labela = Label(ui, text='Choose a hospital:')
    labela.pack(pady=10)
    print()
    area_caller.value = area_caller.hospitals.get()
    print(areo)
    if areo == 'North Chennai':
        area = 'northchennai'
        aria = 1
        hospitals = hospitalz(area)
        print(hospitals)
        area_caller.hospitals['values'] = hospitals
        print("bepis")
        area_caller.hospitals.pack()
        area_caller.hospitals.bind('<<ComboboxSelected>>', finalbook)

    elif areo == 'Central Chennai':
        area = 'centralchennai'
        aria = 2
        hospitals = hospitalz(area)
        area_caller.hospitals['values'] = hospitals
        area_caller.hospitals.pack()
        area_caller.hospitals.bind('<<ComboboxSelected>>', finalbook)
        print()

    elif areo == 'South Chennai':
        area = 'southchennai'
        aria = 3
        hospitals = hospitalz(area)
        area_caller.hospitals['values'] = hospitals
        area_caller.hospitals.pack()
        area_caller.hospitals.bind('<<ComboboxSelected>>', finalbook)
        print()


def die():  # kills the program because not over 18
    print("die")
    sys.exit()


def bwdraw():
    book.root2.withdraw()
    mmenu()


def book():  # the first window of the booking widget
    root.withdraw()
    book.root2 = Toplevel()
    ui = book.root2
    book.root2.geometry(geo)
    label1 = Label(ui, image=backg)
    label1.place(x=0, y=0)
    top = Frame(book.root2, bg='#ffffff')
    bottom = Frame(book.root2, bg='#bad5ed')
    top.pack(pady=10)
    bottom.pack()
    t1 = Label(ui, text="Welcome to our booking system", bg='#ffffff')
    t1['font'] = fent
    t2 = Label(ui, text="Are you 18 or above?", bg='#ffffff')
    t2['font'] = fynt
    b1 = Button(ui, text="Yes", bg='#bad5ed', command=book1)
    b1['font'] = fint
    b2 = Button(ui, text="No", bg='#bad5ed', command=die)
    btn2 = Button(ui, text="   Back   ", bg='#bad5ed', command=bwdraw)
    b2['font'] = fint
    btn2['font'] = fint
    b1.pack(in_=bottom, side=LEFT)
    b2.pack(in_=bottom, side=LEFT)
    t1.pack(in_=top, pady=10)
    t2.pack(in_=top, pady=10)
    btn2.pack(in_=bottom, pady=10)


def book1():  # calling function used to kill the root widget
    book.root2.destroy()
    book11()


# BOOKING SECTION END

# SEARCH SECTION START
def swedow():
    search2.window.withdraw()
    endwindow()


def search2():  # second window of search that shows fetched data
    print("gamer")
    aria = int(search.text1.get(1.0, "end-1c"))
    hosp = search.text2.get(1.0, "end-1c")
    aidi = int(search.text3.get(1.0, "end-1c"))
    # if int(search.text3.get(1.0, "end-1c")).isnumeric(): DEPRECATED

    # else:
    # tkinter.messagebox.showerror("numnum", "Incorrect ID. Exiting..")
    # sys.exit()
    real = isreal(aria, hosp, aidi)
    if not real:
        tkinter.messagebox.showerror("Invalid entry", "This booking does not exist in the DB. Please check your entry")

    nam, ag, gendr, vax = search_1(aria, hosp, aidi)
    print(nam, ag, gendr, vax, "but in the main this time")
    search.window1.withdraw()
    search2.window = Toplevel()
    ui = search2.window
    ui.geometry(geo)
    label1 = Label(ui, image=backg)
    label1.place(x=0, y=0)
    tex = "Your name is:" + nam
    agi = "Your age is: " + str(ag)
    gendur = "Your gender is " + gendr
    aidee = "You are " + str(aidi) + " in queue."
    vaks = "You have chosen the " + vax + " vaccine."

    tl1 = Label(ui, text=tex, bg='#bad5ed')
    tl2 = Label(ui, text=agi, bg='#bad5ed')
    tl3 = Label(ui, text=gendur, bg='#bad5ed')
    tl4 = Label(ui, text=vaks, bg='#bad5ed')
    tl5 = Label(ui, text=aidee, bg='#bad5ed')
    btn = Button(ui, text="   End   ", bg='#bad5ed', command=swedow)
    tl1.pack(pady=10)
    tl1['font'] = fynt
    tl2['font'] = fynt
    tl3['font'] = fynt
    tl4['font'] = fynt
    tl5['font'] = fynt
    btn['font'] = fynt

    tl2.pack(pady=10)
    tl3.pack(pady=10)
    tl4.pack(pady=10)
    tl5.pack(pady=10)
    btn.pack(pady=10)


def swdraw():
    search.window1.withdraw()
    mmenu()


def search():  # gets user input
    root.withdraw()
    search.window1 = Toplevel()
    ui = search.window1
    ui.geometry(geo)
    label1 = Label(ui, image=backg)
    label1.place(x=0, y=0)
    tl1 = Label(ui, text="Enter the first digit \n of your search code", bg='#bad5ed')
    search.text1 = Text(ui, height=2, width=40, bg='#bad5ed')
    tl2 = Label(ui, text="Enter the second part \n of your search code:", bg='#bad5ed')
    search.text2 = Text(ui, height=2, width=40, bg='#bad5ed')
    tl3 = Label(ui, text="Enter the last two digits \n of your search code:", bg='#bad5ed')
    search.text3 = Text(ui, height=2, width=40, bg='#bad5ed')
    # tl4 = Label(ui, text="Choose vaccine: \n (Covaxin or Covishield)", bg='#bad5ed') DEPRECATED
    # finalbook.text4 = Text(ui, height=2, width=40, bg='#bad5ed') DEPRECATED
    btn = Button(ui, text="Submit", bg='#bad5ed', command=search2)
    btn2 = Button(ui, text="   Back   ", bg='#bad5ed', command=swdraw)
    btn['font'] = fint
    btn2['font'] = fint
    tl1['font'] = fynt
    tl2['font'] = fynt
    tl3['font'] = fynt
    # tl4['font'] = fynt DEPRECATED
    tl1.place(x=sw / 10, y=sh / 8)  # relative positioning, better than grid positioning but more work less flexibility
    tl2.place(x=sw / 10, y=sh / 8 + 150)
    tl3.place(x=sw / 10, y=sh / 8 + 300)
    # tl4.place(x=sw / 8, y=sh / 8 + sh / 3) DEPRECATED
    search.text1.place(x=sw - 300, y=sh / 8)
    search.text2.place(x=sw - 300, y=sh / 8 + 150)
    search.text3.place(x=sw - 300, y=sh / 8 + 300)
    # search.text4.place(x=sw / 2, y=sh / 8 + sh / 3)
    btn.place(x=sw - (appw / 3.5), y=sh - (apph - 700))
    btn2.place(x=sw - (appw / 3.5), y=sh - (apph - 775))


# SEARCH SECTION END

# CANCEL SECTION START

def cancel2():  # makes changes in sql database
    print("gamer")
    aria = int(cancel.text1.get(1.0, "end-1c"))
    hosp = cancel.text2.get(1.0, "end-1c")
    aidi = int(cancel.text3.get(1.0, "end-1c"))
    # if int(cancel.text3.get(1.0, "end-1c")).isnumeric(): DEPRECATED

    # else:
    # tkinter.messagebox.showerror("numnum", "Incorrect ID. Exiting..")
    # sys.exit()
    cancel_1(aria, hosp, aidi)
    tkinter.messagebox.showinfo('Cancellation complete', 'Your booking has been cancelled.')
    print('gg')
    cancel.window1.withdraw()
    endwindow()


def cwdraw():
    cancel.window1.withdraw()
    mmenu()


def cancel():  # cancel function
    root.withdraw()
    cancel.window1 = Toplevel()
    ui = cancel.window1
    ui.geometry(geo)
    label1 = Label(ui, image=backg)
    label1.place(x=0, y=0)
    tl1 = Label(ui, text="Enter the first digit \n of your search code", bg='#bad5ed')
    cancel.text1 = Text(ui, height=2, width=40, bg='#bad5ed')
    tl2 = Label(ui, text="Enter the second part \n of your search code:", bg='#bad5ed')
    cancel.text2 = Text(ui, height=2, width=40, bg='#bad5ed')
    tl3 = Label(ui, text="Enter the last two digits \n of your search code:", bg='#bad5ed')
    cancel.text3 = Text(ui, height=2, width=40, bg='#bad5ed')
    # tl4 = Label(ui, text="Choose vaccine: \n (Covaxin or Covishield)", bg='#bad5ed') DEPRECATED
    # finalbook.text4 = Text(ui, height=2, width=40, bg='#bad5ed') DEPRECATED
    btn = Button(ui, text="Submit", bg='#bad5ed', command=cancel2)
    btn2 = Button(ui, text="   Back   ", bg='#bad5ed', command=cwdraw)
    btn['font'] = fint
    btn2['font'] = fint
    tl1['font'] = fynt
    tl2['font'] = fynt
    tl3['font'] = fynt
    # tl4['font'] = fynt DEPRECATED
    tl1.place(x=sw / 10, y=sh / 8)  # relative positioning, better than grid positioning but more work less flexibility
    tl2.place(x=sw / 10, y=sh / 8 + 150)
    tl3.place(x=sw / 10, y=sh / 8 + 300)
    # tl4.place(x=sw / 8, y=sh / 8 + sh / 3) DEPRECATED
    cancel.text1.place(x=sw - 300, y=sh / 8)
    cancel.text2.place(x=sw - 300, y=sh / 8 + 150)
    cancel.text3.place(x=sw - 300, y=sh / 8 + 300)
    # cancel.text4.place(x=sw / 2, y=sh / 8 + sh / 3)
    btn.place(x=sw - (appw / 3.5), y=sh - (apph - 700))
    btn2.place(x=sw - (appw / 3.5), y=sh - (apph - 775))


def mmenu():
    global rootbool
    rootbool = True
    print('sos')
    root.deiconify()


# buttons come last because functions must be declared first
bt1 = Button(root, text="Book a vaccine slot", bg='#d2e3f3', command=book)
bt2 = Button(root, text="Check booking details", bg='#bad5ed', command=search)
bt3 = Button(root, text="Cancel my booking", bg='#bad5ed', command=cancel)
btn2 = Button(root, text="   Exit   ", bg='#bad5ed', command=die)

bt1['font'] = fint
bt2['font'] = fint
bt3['font'] = fint
btn2['font'] = fint
bt1.pack(pady=15)
bt2.pack(pady=15)
bt3.pack(pady=15)
btn2.pack(pady=15)

root.mainloop()
