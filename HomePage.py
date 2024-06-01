import os
from tkinter import *
from tkinter import ttk, messagebox
import random
import pymysql
import tk as tk
from PIL import ImageTk, Image


def Back():
    window_1.destroy()
    os.system("HomePage.py")


def Exit():
    window_1.destroy()


# here we have to show users fullname , email ,  type of artist , type of Instrument , phone
def showprofile():
    win0 = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win0.winfo_screenwidth()
    screen_height = win0.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    # win0.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win0.geometry("630x230")
    win0.title('Your Profile...')
    win0.iconbitmap('images\\aa.ico')
    win0.resizable(0, 0)

    Photo_icon = Image.open('images\\profile.png')
    photo = ImageTk.PhotoImage(Photo_icon)
    Photo_icon_label = Label(win0, image=photo  # highlightbackground='blue' , highlightthickness=2,
                             )
    Photo_icon_label.image = photo
    Photo_icon_label.place(x=35, y=37)

    fullname_label = Label(win0, text='Name', fg="black",
                           font=("yu gothic ui", 13, 'bold'))
    fullname_label.place(x=190, y=30)
    mail_label = Label(win0, text='Email', fg="black",
                       font=("yu gothic ui", 13, 'bold'))
    mail_label.place(x=192, y=60)
    Typeofartist_label = Label(win0, text='Type of Artist', fg="black",
                               font=("yu gothic ui", 13, 'bold'))
    Typeofartist_label.place(x=190, y=90)
    Typeofinstr_label = Label(win0, text='Type of Instrument', fg="black",
                              font=("yu gothic ui", 13, 'bold'))
    Typeofinstr_label.place(x=190, y=120)
    phoneno_label = Label(win0, text='Phone No', fg="black",
                          font=("yu gothic ui", 13, 'bold'))
    phoneno_label.place(x=190, y=150)
    colon_label = Label(win0, text=':', fg="black",
                        font=("yu gothic ui", 13, 'bold'))
    colon_label.place(x=350, y=30)
    colon_label = Label(win0, text=':', fg="black",
                        font=("yu gothic ui", 13, 'bold'))
    colon_label.place(x=350, y=60)
    colon_label = Label(win0, text=':', fg="black",
                        font=("yu gothic ui", 13, 'bold'))
    colon_label.place(x=350, y=90)
    colon_label = Label(win0, text=':', fg="black",
                        font=("yu gothic ui", 13, 'bold'))
    colon_label.place(x=350, y=120)
    colon_label = Label(win0, text=':', fg="black",
                        font=("yu gothic ui", 13, 'bold'))
    colon_label.place(x=350, y=150)


# def logout():
#     window_1.destroy()
#     import main


window_1 = Tk()
window_1.rowconfigure(0, weight=1)
window_1.columnconfigure(0, weight=1)
window_1.state('zoomed')
# window_1.geometry('1350x740+50+50')
window_1.resizable(0, 0)
window_1.title('BANDTribe HomePage')

# window_1 Icon Photo
icon = PhotoImage(file='images\\pic-icon.png')
window_1.iconphoto(True, icon)

ArtistPage = Frame(window_1)
InstrumentPage = Frame(window_1)
EventPage = Frame(window_1)
LWUPage = Frame(window_1)
AboutPage = Frame(window_1)

for frame in (ArtistPage, InstrumentPage, EventPage, LWUPage, AboutPage):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(ArtistPage)

# =====================================================================================================================
# =====================================================================================================================
# ==================== Artist PAGE FRAME =====================================================================================
# =====================================================================================================================
# =====================================================================================================================

design_frame1 = Listbox(ArtistPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame1.place(x=0, y=0)

design_frame2 = Listbox(ArtistPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame2.place(x=676, y=0)

design_frame3 = Listbox(ArtistPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame3.place(x=75, y=106)

design_frame4 = Listbox(ArtistPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame4.place(x=676, y=106)


# ===================================================================================================================
# ===================================================================================================================
# === Singer  , dancer ,  comedy PAGE =========================================================================================
# ===================================================================================================================
# ===================================================================================================================


def singer():
    # if  :
    # else:

    win1 = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win1.winfo_screenwidth()
    screen_height = win1.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    # win1.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win1.geometry("470x500")
    win1.title('List of Singers...')
    win1.iconbitmap('images\\aa.ico')
    win1.resizable(0, 0)

    cnt1 = Label(win1, text="Please Wait Singers Are being Listed....", font=("yu gothic ui bold", 16, 'bold'),
                 fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt1.place(x=50, y=20)

    cnt2 = Label(win1, text=" • Singer's Data", font=("yu gothic ui bold", 12, 'bold'), fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=28, y=90)

    # style = ttk.Style(tab0)
    # style.configure("Treeview" , rowheight ="38")

    # hsb = ttk.Scrollbar(win1,orient="horizontal")

    tree = ttk.Treeview(win1, columns=(1, 2), show='headings', height="7")
    tree.place(x=30, y=120,  # width=400 ,
               height=350
               )

    tree.column(1, anchor='c')
    tree.column(2, anchor='c')
    tree.heading(1, text="Singer's Name")
    tree.heading(2, text="Contact No.")

    try:
        con = pymysql.connect(host='localhost', user='root', password='aryan123', database='bandtribe')
        mycursor = con.cursor()
        query = 'select name,phoneno from signup where artist = "singer"'
        mycursor.execute(query)
        i = 0
        for r in mycursor:
            tree.insert("", 'end', iid=r[0], values=(r[0], r[1]))

        # for singer in mycursor:
        #     for j in range(len(singer)):
        #         e=Entry(tree)
        #         e.grid(row=i,column=j)
        #         e.insert(END,singer[j])
        #     i=i+1
        # row = mycursor.fetchone()
    except:
        messagebox.showerror('Error', 'database connectivity issue, please Try Again')
        return


def Dancer():
    win2 = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win2.winfo_screenwidth()
    screen_height = win2.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    # win1.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win2.geometry("470x500")
    win2.title('List of Dancers...')
    win2.iconbitmap('images\\aa.ico')
    win2.resizable(0, 0)

    cnt1 = Label(win2, text="Please Wait Dancer's Are being Listed....", font=("yu gothic ui bold", 16, 'bold'),
                 fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt1.place(x=48, y=20)

    cnt2 = Label(win2, text=" • Dancer's Data", font=("yu gothic ui bold", 12, 'bold'), fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=28, y=90)

    tree = ttk.Treeview(win2, columns=(1, 2), show='headings', height="7")
    tree.place(x=30, y=120,  # width=1000 ,
               height=350
               )

    tree.heading(1, text="Dancer's Name")
    tree.heading(2, text="Contact No.")
    tree.column(1, anchor='c')
    tree.column(2, anchor='c')

    try:
        con = pymysql.connect(host='localhost', user='root', password='aryan123', database='bandtribe')
        mycursor = con.cursor()
        query = 'select name,phoneno from signup where artist = "dancer"'
        mycursor.execute(query)
        i = 0
        for r in mycursor:
            tree.insert("", 'end', iid=r[0], values=(r[0], r[1]))
    except:
        messagebox.showerror('Error', 'database connectivity issue, please Try Again')
        return


def Comedy():
    win3 = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win3.winfo_screenwidth()
    screen_height = win3.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    # win1.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win3.geometry("470x500")
    win3.title('List of Comedian...')
    win3.iconbitmap('images\\aa.ico')
    win3.resizable(0, 0)

    cnt1 = Label(win3, text="Please Wait Comedian's Are being Listed....", font=("yu gothic ui bold", 16, 'bold'),
                 fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt1.place(x=40, y=20)

    cnt2 = Label(win3, text=" • Comedian's Data", font=("yu gothic ui bold", 12, 'bold'), fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=28, y=90)

    tree = ttk.Treeview(win3, columns=(1, 2), show='headings', height="7")
    tree.place(x=30, y=120  # width=1000
               , height=350
               )
    tree.heading(1, text="Comedian's Name")
    tree.heading(2, text="Contact No.")
    tree.column(1, anchor='c')
    tree.column(2, anchor='c')

    try:
        con = pymysql.connect(host='localhost', user='root', password='aryan123', database='bandtribe')
        mycursor = con.cursor()
        query = 'select name,phoneno from signup where artist = "comedian"'
        mycursor.execute(query)
        i = 0
        for r in mycursor:
            tree.insert("", 'end', iid=r[0], values=(r[0], r[1]))
    except:
        messagebox.showerror('Error', 'database connectivity issue, please Try Again')
        return


# ========= Buttons ===============
# ---------------your profile---------------------

profile_button = Button(ArtistPage, text='YourProfile', font=("yu gothic ui bold", 12, 'bold'), bg='#f8f8f8',
                        fg="#89898b",
                        borderwidth=0, command=showprofile, activebackground='white', cursor='hand2')
profile_button.place(x=1130, y=121)

# profile_line = Canvas(ArtistPage, width=90, height=2, bg='#1b87d2')
# profile_line.place(x=1145, y=150)
# ===== profile icon =========
profile_icon = Image.open('images\\name-icon.png')
photo = ImageTk.PhotoImage(profile_icon)
profileIcon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
profileIcon_label.image = photo
profileIcon_label.place(x=550, y=17)

# ==============Back Button============
backBtn = Button(design_frame4, fg='#89898b', bd=0, text='Return to HomePage | ', bg='#f8f8f8',
                 font=("yu gothic ui bold", 12),
                 cursor='hand2', activebackground='White', command=Back)
backBtn.place(x=80, y=470)

# ==============Exit Button============
exitBtn = Button(design_frame4, fg='#89898b', bd=0, text='Exit', bg='#f8f8f8', font=("yu gothic ui bold", 12),
                 cursor='hand2', activebackground='White', command=Exit)
exitBtn.place(x=250, y=470)

# ==============Logout Button============
# lgoutBtn = Button(design_frame4 , fg='#89898b', bd = 0, text='LogOut', bg='#f8f8f8', font=("yu gothic ui bold", 12),
#                    cursor='hand2', activebackground='White', command=logout)
# lgoutBtn.place(x=475, y=470)

Instrument_button = Button(ArtistPage, text='Instrument', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                           command=lambda: show_frame(InstrumentPage), borderwidth=0, activebackground='white',
                           cursor='hand2')
Instrument_button.place(x=835, y=175)

# =============Event Button ========
Event_button = Button(ArtistPage, text='Event', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='white', command=lambda: show_frame(EventPage), cursor='hand2')
Event_button.place(x=950, y=175)

# ===== Welcome Label ==============
welcome_label = Label(design_frame4, text='BANDTribe', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=210, y=15)

# ===== typeofartist Label ==============
toa_label = Label(design_frame4, text='Select the Type of Artist >> ', font=("yu gothic ui bold", 16), fg="#1b87d2",
                  bg='#f8f8f8')
toa_label.place(x=175, y=140)

# ==========================lwu BUTTON=============
LWU_button = Button(ArtistPage, text='LearnWithUs', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                    command=lambda: show_frame(LWUPage),
                    borderwidth=0, activebackground='white', cursor='hand2')
LWU_button.place(x=1025, y=175)

# ==========================About BUTTON=============
About_button = Button(ArtistPage, text='About', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      command=lambda: show_frame(AboutPage),
                      borderwidth=0, activebackground='white', cursor='hand2')
About_button.place(x=1145, y=175)

# ======= top Artist Button =========
Artist_button = Button(ArtistPage, text='Artist', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       borderwidth=0, activebackground='white', cursor='hand2')
Artist_button.place(x=760, y=175)

Artist_line = Canvas(ArtistPage, width=60, height=5, bg='#1b87d2')
Artist_line.place(x=755, y=203)

# ==================picture Button==============================

singer_button1 = Button(ArtistPage, command=singer,
                        text='Singer', font=("yu gothic ui bold", 13), bg='#f8f8f8', fg="black",
                        borderwidth=0, activebackground='white', cursor='hand2'
                        )
singer_button1.place(x=810, y=437)
# singer_line1 = Canvas(ArtistPage, width=60, height=3, bg='#1b87d2')
# singer_line1.place(x=810, y=470)

Dancer_button2 = Button(ArtistPage, command=Dancer,
                        text='Dancer', font=("yu gothic ui bold", 13), bg='#f8f8f8', fg="black",
                        borderwidth=0, activebackground='white', cursor='hand2'
                        )
Dancer_button2.place(x=950, y=437)
# Dancer_line2 = Canvas(ArtistPage, width=60, height=3, bg='#1b87d2')
# Dancer_line2.place(x=950, y=470)

Comedy_button3 = Button(ArtistPage, command=Comedy,
                        text='Comedian', font=("yu gothic ui bold", 13), bg='#f8f8f8', fg="black",
                        borderwidth=0, activebackground='white', cursor='hand2'
                        )
Comedy_button3.place(x=1090, y=437)
# Comedy_line3 = Canvas(ArtistPage, width=85, height=3, bg='#1b87d2')
# Comedy_line3.place(x=1090, y=470)

# ===== picture icon =========
picture_icon = Image.open('images\\pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=130, y=5)
#
# ===== Left Side Picture ============
side_image = Image.open('images\\btlogo1copy.jpg')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame3, image=photo, bd=0)
side_image_label.image = photo
side_image_label.place(x=110, y=19)

# ===== singer icon =========
Singer_icon = Image.open('images\\singer.jpg')
photo = ImageTk.PhotoImage(Singer_icon)
Singer_icon_label = Label(design_frame4, image=photo  # highlightbackground='blue' , highlightthickness=2,
                          , bg='#f8f8f8')
Singer_icon_label.image = photo
Singer_icon_label.place(x=95, y=200)

# ===== Dancer icon =========
Dancer_icon = Image.open('images\\dancer.jpg')
photo = ImageTk.PhotoImage(Dancer_icon)
Dancer_icon_label = Label(design_frame4, image=photo,  # highlightbackground='blue' , highlightthickness=2,
                          bg='#f8f8f8')
Dancer_icon_label.image = photo
Dancer_icon_label.place(x=240, y=200)

# ===== Comedian icon =========
comedy_icon = Image.open('images\\comedy.jpg')
photo = ImageTk.PhotoImage(comedy_icon)
comedy_icon_label = Label(design_frame4, image=photo,  # highlightbackground='blue' , highlightthickness=2,
                          bg='#f8f8f8')
comedy_icon_label.image = photo
comedy_icon_label.place(x=385, y=200)

# ============
# =========================================================================================================
# =====================================================================================================================
# ==================== Instrument PAGE FRAME ==============================================================================
# =====================================================================================================================
# =====================================================================================================================

design_frame5 = Listbox(InstrumentPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame5.place(x=0, y=0)

design_frame6 = Listbox(InstrumentPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame6.place(x=676, y=0)

design_frame7 = Listbox(InstrumentPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame7.place(x=75, y=106)

design_frame8 = Listbox(InstrumentPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame8.place(x=676, y=106)

# ---------------your profile---------------------

profile_button = Button(InstrumentPage, text='YourProfile', font=("yu gothic ui bold", 12, 'bold'), bg='#f8f8f8',
                        fg="#89898b",
                        borderwidth=0, command=showprofile, activebackground='white', cursor='hand2')
profile_button.place(x=1130, y=121)

# profile_line = Canvas(ArtistPage, width=90, height=2, bg='#1b87d2')
# profile_line.place(x=1145, y=150)
# ===== profile icon =========
profile_icon = Image.open('images\\name-icon.png')
photo = ImageTk.PhotoImage(profile_icon)
profileIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
profileIcon_label.image = photo
profileIcon_label.place(x=550, y=17)

# ===== typeofinstrument Label ==============
toi_label = Label(design_frame8, text='Select the Type of Instrument >> ', font=("yu gothic ui bold", 16), fg="#1b87d2",
                  bg='#f8f8f8')
toi_label.place(x=150, y=140)

# ==============Back Button============
backBtn = Button(design_frame8, fg='#89898b', bd=0, text='Return to HomePage | ', bg='#f8f8f8',
                 font=("yu gothic ui bold", 12),
                 cursor='hand2', activebackground='White', command=Back)
backBtn.place(x=80, y=470)

# ==============Exit Button============
exitBtn = Button(design_frame8, fg='#89898b', bd=0, text='Exit', bg='#f8f8f8', font=("yu gothic ui bold", 12),
                 cursor='hand2', activebackground='White', command=Exit)
exitBtn.place(x=250, y=470)

# ========= Buttons ====================
Instrument_button = Button(InstrumentPage, text='Instrument', font=("yu gothic ui bold", 12), bg='#f8f8f8',
                           fg="#89898b",
                           command=lambda: show_frame(ArtistPage), borderwidth=0, activebackground='white',
                           cursor='hand2')
Instrument_button.place(x=835, y=175)

Instrument_line = Canvas(InstrumentPage, width=88, height=5, bg='#1b87d2')
Instrument_line.place(x=835, y=203)

# =============EventPage====================
Event_button = Button(InstrumentPage, text='Event', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='white', command=lambda: show_frame(EventPage), cursor='hand2')
Event_button.place(x=950, y=175)

# ========= Artist Button =========
Artist_button = Button(InstrumentPage, text='Artist', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       borderwidth=0, activebackground='white', command=lambda: show_frame(ArtistPage), cursor='hand2')
Artist_button.place(x=760, y=175)

# ==========================lwu BUTTON=============
LWU_button = Button(InstrumentPage, text='LearnWithUs', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                    command=lambda: show_frame(LWUPage), borderwidth=0, activebackground='white', cursor='hand2')
LWU_button.place(x=1025, y=175)

# ==========================About BUTTON=============
About_button = Button(InstrumentPage, text='About', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      command=lambda: show_frame(AboutPage),
                      borderwidth=0, activebackground='white', cursor='hand2')
About_button.place(x=1145, y=175)

# ===== Welcome Label ==================
welcome_label = Label(design_frame8, text='BANDTribe', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=210, y=15)


# -------------------flute------------------
def flute():
    win4 = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win4.winfo_screenwidth()
    screen_height = win4.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    # win1.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win4.geometry("660x500")
    win4.title('List of Flute Beginner/Specialists Users...')
    win4.iconbitmap('images\\aa.ico')
    win4.resizable(0, 0)

    cnt1 = Label(win4, text="Please Wait Flautist's Are being Listed....", font=("yu gothic ui bold", 16, 'bold'),
                 fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt1.place(x=170, y=20)

    cnt2 = Label(win4, text=" • Flautist's Data", font=("yu gothic ui bold", 12, 'bold'), fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=28, y=90)

    tree = ttk.Treeview(win4, columns=(1, 2, 3), show='headings', height="7")
    tree.place(x=30, y=120  # width=1000
               , height=350
               )
    tree.heading(1, text="Flautist's Name")
    tree.heading(2, text="Contact No.")
    tree.heading(3, text="Ratings(i.e.out of 5)")
    tree.column(1, anchor='c')
    tree.column(2, anchor='c')
    tree.column(3, anchor='c')
    #
    # def no():
    #     print(random.randint(0, 10))

    try:
        con = pymysql.connect(host='localhost', user='root', password='aryan123', database='bandtribe')
        mycursor = con.cursor()
        query = 'select name,phoneno from signup where instrument = "flute"'
        mycursor.execute(query)
        i = 0
        for r in mycursor:
            tree.insert("", 'end', iid=r[0], values=(r[0], r[1],random.randint(0,5)))
    except:
        messagebox.showerror('Error', 'database connectivity issue, please Try Again')
        return


# -------------------guitar------------------
def guitar():
    win5 = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win5.winfo_screenwidth()
    screen_height = win5.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    # win1.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win5.geometry("660x500")
    win5.title('List of Guitar Beginner/Specialists Users...')
    win5.iconbitmap('images\\aa.ico')
    win5.resizable(0, 0)

    cnt1 = Label(win5, text="Please Wait Guitarist's Are being Listed....", font=("yu gothic ui bold", 16, 'bold'),
                 fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt1.place(x=170, y=20)

    cnt2 = Label(win5, text=" • Guitarist's Data", font=("yu gothic ui bold", 12, 'bold'), fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=28, y=90)

    tree = ttk.Treeview(win5, columns=(1, 2, 3), show='headings', height="7")
    tree.place(x=30, y=120  # width=1000 ,
               , height=350
               )
    tree.heading(1, text="Guitarist's Name")
    tree.heading(2, text="Contact No.")
    tree.heading(3, text="Ratings(i.e.out of 5)")
    tree.column(1, anchor='c')
    tree.column(2, anchor='c')
    tree.column(3, anchor='c')
    #
    # def no():
    #     print(random.randint(0, 10))

    try:
        con = pymysql.connect(host='localhost', user='root', password='aryan123', database='bandtribe')
        mycursor = con.cursor()
        query = 'select name,phoneno from signup where instrument = "guitar"'
        mycursor.execute(query)
        i = 0
        for r in mycursor:
            tree.insert("", 'end', iid=r[0], values=(r[0], r[1], random.randint(0,5)))
    except:
        messagebox.showerror('Error', 'database connectivity issue, please Try Again')
        return


# -------------------piano------------------
def piano():
    win6 = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win6.winfo_screenwidth()
    screen_height = win6.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    # win1.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win6.geometry("660x500")
    win6.title('List of Piano Beginner/Specialists Users...')
    win6.iconbitmap('images\\aa.ico')
    win6.resizable(0, 0)

    cnt1 = Label(win6, text="Please Wait Pianist's Are being Listed....", font=("yu gothic ui bold", 16, 'bold'),
                 fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt1.place(x=170, y=20)

    cnt2 = Label(win6, text=" • Pianist's Data", font=("yu gothic ui bold", 12, 'bold'), fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=28, y=90)

    tree = ttk.Treeview(win6, columns=(1, 2, 3), show='headings', height="7")
    tree.place(x=30, y=120  # width=1000 , height= 250
               )
    tree.heading(1, text="Pianist's Name")
    tree.heading(2, text="Contact No.")
    tree.heading(3, text="Ratings(i.e.out of 5)")
    tree.column(1, anchor='c')
    tree.column(2, anchor='c')
    tree.column(3, anchor='c')
    #
    # def no():
    #     for r[2] in mycursor:
    #         # print(random.randint(0, 10))
    #         tree.insert("", 'end', iid=r[0], values=random.randint(0, 9))

    try:
        con = pymysql.connect(host='localhost', user='root', password='aryan123', database='bandtribe')
        mycursor = con.cursor()
        query = 'select name,phoneno from signup where instrument = "piano"'
        mycursor.execute(query)
        i = 0
        for r in mycursor:
            tree.insert("", 'end', iid=r[0], values=(r[0], r[1],random.randint(0,5)))
    except:
        messagebox.showerror('Error', 'database connectivity issue, please Try Again')
        return


# ==================picture Button==============================

flute_button1 = Button(InstrumentPage, command=flute,
                       text='Flute', font=("yu gothic ui bold", 13), bg='#f8f8f8', fg="Black",
                       borderwidth=0, activebackground='white', cursor='hand2'
                       )
flute_button1.place(x=810, y=437)
# singer_line1 = Canvas(ArtistPage, width=60, height=3, bg='#1b87d2')
# singer_line1.place(x=810, y=470)

guitar_button2 = Button(InstrumentPage, command=guitar,
                        text='Guitar', font=("yu gothic ui bold", 13), bg='#f8f8f8', fg="Black",
                        borderwidth=0, activebackground='white', cursor='hand2'
                        )
guitar_button2.place(x=950, y=437)
# Dancer_line2 = Canvas(ArtistPage, width=60, height=3, bg='#1b87d2')
# Dancer_line2.place(x=950, y=470)

piano_button3 = Button(InstrumentPage, command=piano,
                       text='Piano', font=("yu gothic ui bold", 13), bg='#f8f8f8', fg="Black",
                       borderwidth=0, activebackground='white', cursor='hand2'
                       )
piano_button3.place(x=1090, y=437)
# Comedy_line3 = Canvas(ArtistPage, width=85, height=3, bg='#1b87d2')
# Comedy_line3.place(x=1090, y=470)


# ===== flute icon =========
flute_icon = Image.open('images\\flute.jpeg')
photo = ImageTk.PhotoImage(flute_icon)
flute_icon_label = Label(design_frame8, image=photo  # highlightbackground='blue' , highlightthickness=2,
                         , bg='#f8f8f8')
flute_icon_label.image = photo
flute_icon_label.place(x=95, y=200)

# ===== guitar icon =========
guitar_icon = Image.open('images\\guitar.jpg')
photo = ImageTk.PhotoImage(guitar_icon)
guitar_icon_label = Label(design_frame8, image=photo,  # highlightbackground='blue' , highlightthickness=2,
                          bg='#f8f8f8')
guitar_icon_label.image = photo
guitar_icon_label.place(x=240, y=200)

# ===== piano icon =========
piano_icon = Image.open('images\\piano.jpg')
photo = ImageTk.PhotoImage(piano_icon)
piano_icon_label = Label(design_frame8, image=photo,  # highlightbackground='blue' , highlightthickness=2,
                         bg='#f8f8f8')
piano_icon_label.image = photo
piano_icon_label.place(x=385, y=200)

# ===== picture icon =========
picture_icon = Image.open('images\\pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=130, y=5)

# ===== Left Side Picture ============
side_image = Image.open('images\\btlogo1copy.jpg')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame7, image=photo, bd=0)
side_image_label.image = photo
side_image_label.place(x=110, y=19)

# =====================================================================================================================
# =====================================================================================================================
# ==================== Event PAGE FRAME ==============================================================================
# =====================================================================================================================
# =====================================================================================================================

design_frame9 = Listbox(EventPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame9.place(x=0, y=0)

design_frame10 = Listbox(EventPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame10.place(x=676, y=0)

design_frame11 = Listbox(EventPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame11.place(x=75, y=106)

design_frame12 = Listbox(EventPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame12.place(x=676, y=106)

# ---------------your profile---------------------

profile_button = Button(EventPage, text='YourProfile', font=("yu gothic ui bold", 12, 'bold'), bg='#f8f8f8',
                        fg="#89898b",
                        borderwidth=0, command=showprofile, activebackground='white', cursor='hand2')
profile_button.place(x=1130, y=121)

# profile_line = Canvas(ArtistPage, width=90, height=2, bg='#1b87d2')
# profile_line.place(x=1145, y=150)
# ===== profile icon =========
profile_icon = Image.open('images\\name-icon.png')
photo = ImageTk.PhotoImage(profile_icon)
profileIcon_label = Label(design_frame12, image=photo, bg='#f8f8f8')
profileIcon_label.image = photo
profileIcon_label.place(x=550, y=17)

# ===== event image  icon =========
eimage_icon = Image.open(
    'images\\music-festival-international-concert-musical-event-banner-musicians-instruments-open-air-party-poster-vector-festive-169147536 (1).jpg')
photo = ImageTk.PhotoImage(eimage_icon)
eimageIcon_label = Label(design_frame12, image=photo, bg='#f8f8f8')
eimageIcon_label.image = photo
eimageIcon_label.place(x=50, y=179)


# =============================search event function==============

# ===================event list frame window====================
def listeventframewindow():
    tab0 = Toplevel()
    window_width = 1000
    window_height = 350
    screen_width = tab0.winfo_screenwidth()
    screen_height = tab0.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    tab0.geometry("1070x350")
    tab0.resizable(0, 0)
    tab0.title('Events...')
    tab0.iconbitmap('images\\aa.ico')

    cnt1 = Label(tab0, text="Please Wait Events Are being Listed....", font=("yu gothic ui bold", 16, 'bold'),
                 fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt1.place(x=400, y=20)

    cnt2 = Label(tab0, text=" • Event Data", font=("yu gothic ui bold", 12, 'bold'), fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=28, y=90)

    tree = ttk.Treeview(tab0, columns=(0, 1, 2, 3, 4), show='headings', height="7")
    tree.place(x=30, y=120  # width=1000 ,
               , height=200
               )

    # tree.tag_configure("checked", image=chkd)
    # tree.tag_configure("checked",img=chkd)

    tree.heading(0, text="EventManager's Contact")
    tree.heading(1, text="EventName")
    tree.heading(2, text="Date")
    tree.heading(3, text="Venue")
    tree.heading(4, text="Timings")
    tree.column(0, anchor='c')
    tree.column(1, anchor='c')
    tree.column(2, anchor='c')
    tree.column(3, anchor='c')
    tree.column(4, anchor='c')

    try:
        con = pymysql.Connect(host='localhost', user='root', password='aryan123', database='bandtribe')
        mycursor = con.cursor()
        query = 'select eventmanager_contact,event_name,event_date,venue,timing from listofevents'
        mycursor.execute(query)
    except:
        messagebox.showerror('Error', 'database connectivity issue,please Try Again')
        return
    i = 0
    for r in mycursor:
        tree.insert("", 'end', values=(r[0], r[1], r[2], r[3], r[4]))
        i = i + 1


# =============listevent Button ========
listevent_button = Button(EventPage, text='Click Here for Upcoming Event Updates >>', font=("yu gothic ui bold", 15),
                          bg='#f8f8f8',
                          fg="#1b87d2",
                          borderwidth=0, activebackground='white', command=listeventframewindow, cursor='hand2')
listevent_button.place(x=775, y=450)
# listevent_line = Canvas(EventPage, width=45, height=3, bg='#1b87d2')
# listevent_line.place(x=950, y=425)


# ==============Back Button============
backBtn = Button(design_frame12, fg='#89898b', bd=0, text='Return to HomePage | ', bg='#f8f8f8',
                 font=("yu gothic ui bold", 12),
                 cursor='hand2', activebackground='White', command=Back)
backBtn.place(x=80, y=470)

# ==============Exit Button============
exitBtn = Button(design_frame12, fg='#89898b', bd=0, text='Exit', bg='#f8f8f8', font=("yu gothic ui bold", 12),
                 cursor='hand2', activebackground='White', command=Exit)
exitBtn.place(x=250, y=470)
# ========= Buttons ====================
Instrument_button = Button(EventPage, text='Instrument', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                           command=lambda: show_frame(InstrumentPage), borderwidth=0, activebackground='white',
                           cursor='hand2')
Instrument_button.place(x=835, y=175)

# ========= Login Button =========
Artist_button = Button(EventPage, text='Artist', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       borderwidth=0, activebackground='white', command=lambda: show_frame(ArtistPage), cursor='hand2')
Artist_button.place(x=760, y=175)

# ==========================lwu BUTTON=============
LWU_button = Button(EventPage, text='LearnWithUs', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                    command=lambda: show_frame(LWUPage), borderwidth=0, activebackground='white', cursor='hand2')
LWU_button.place(x=1025, y=175)

# =============Event Button ========
Event_button = Button(EventPage, text='Event', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='white', command=lambda: show_frame(EventPage), cursor='hand2')
Event_button.place(x=950, y=175)
Event_line = Canvas(EventPage, width=45, height=5, bg='#1b87d2')
Event_line.place(x=950, y=203)

# ==========================About BUTTON=============
About_button = Button(EventPage, text='About', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      command=lambda: show_frame(AboutPage),
                      borderwidth=0, activebackground='white', cursor='hand2')
About_button.place(x=1145, y=175)

# ===== Welcome Label ==================
welcome_label = Label(design_frame12, text='BANDTribe', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=210, y=15)

#
# ===== picture icon =========
picture_icon = Image.open('images\\pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame12, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=130, y=5)

# ===== Left Side Picture ============
side_image = Image.open('images\\btlogo1copy.jpg')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame11, image=photo, bd=0)
side_image_label.image = photo
side_image_label.place(x=110, y=19)

# =====================================================================================================================
# =====================================================================================================================
# ==================== LWU PAGE FRAME =====================================================================================
# =====================================================================================================================
# =====================================================================================================================

design_frame13 = Listbox(LWUPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame13.place(x=0, y=0)

design_frame14 = Listbox(LWUPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame14.place(x=676, y=0)

design_frame15 = Listbox(LWUPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame15.place(x=75, y=106)

design_frame16 = Listbox(LWUPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame16.place(x=676, y=106)
# ==============Back Button============
backBtn = Button(design_frame16, fg='#89898b', bd=0, text='Return to HomePage | ', bg='#f8f8f8',
                 font=("yu gothic ui bold", 12),
                 cursor='hand2', activebackground='White', command=Back)
backBtn.place(x=80, y=470)


# --------------flute lesson ------------------
def flutelesson():
    tab0 = Toplevel()
    window_width = 1000
    window_height = 350
    screen_width = tab0.winfo_screenwidth()
    screen_height = tab0.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    tab0.geometry("1100x680")
    tab0.resizable(0, 0)
    tab0.title('Flute Lesson...')
    tab0.iconbitmap('images\\aa.ico')

    cnt1 = Label(tab0, text="Flute Lesson is Being Loaded...", font=("yu gothic ui bold", 16, 'bold'),
                 fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt1.place(x=400, y=20)
    cnt2 = Label(tab0,
                 text=" • BEGINNER FLUTE LESSON 1 : BREATHING AND POSTURE\nLike all wind instruments, playing the "
                      "flute requires good breath control. It is easy to "
                      "run out of air when playing the flute because it does not\n have a reed or a cup shaped "
                      "mouthpiece to offer blowing resistance. Flutes use a lot of air so we will start with"
                      " posture and breathing.\n\n • "
                      "BEGINNER FLUTE LESSON 2 : THE HEADJOINT, LIP PLATE AND "
                      "TONE HOLE\nUnlike virtually all other wind instruments, the flute does not have a separate"
                      " mouthpiece. It is built into the body of the flute and is referred\n to as the headjoint."
                      "This is where the sound begins so it is one of the most important parts of your flute. For"
                      " this lesson we will concentrate\n on producing a good tone from the headjoint. Before trying"
                      " this, spend some time with the posture and breathing exercises in lesson 1.\n\n"
                      " • BEGINNER FLUTE LESSON 3 : INTRO TO NOTATION\n"
                      "The next thing we need to understand before playing is how to read rhythm."
                      "To begin, notes are typically written on a five line staff which looks\n like this:"
                      "We will discuss the lines and spaces in another lesson.\n\n"
                      " • BEGINNER FLUTE LESSON 4 : PUTTING IT ALL TOGETHER\n"
                      "Before you begin this lesson make sure you have read lessons 1 - 3, which means you can"
                      " tongue a note on your flute headjoint while sitting with\n good posture. In addition, you"
                      " should be familiar with whole half and quarter notes and rests, understand time signatures"
                      " and baronies. If you\n are confused about any of this, review the previous lessons before "
                      "going on.\n\n"
                      " • BEGINNER FLUTE LESSON 5 : MORE RHYTHM\n"
                      "This lesson will build on skills we learned from lesson four. We will start mixing up the "
                      "rhythm using half notes and quarter notes. If you are\n unsure about what these are"
                      " review lesson three.As you listen to it, clap the rhythm. To help get the feel for half "
                      "notes, hold your hands\n together for two counts when you clap a half note."
                      "When you feel confident you understand the rhythm move on in the lesson.\n\n"
                      " • BEGINNER FLUTE LESSON 6 : ASSEMBLING THE FLUTE\n"
                      "Now that you have established good posture and breath control, and have some experience"
                      " with playing various rhythms on your headjoint, you\n are ready for the next phase, playing"
                      " the assembled flute.Before you can play you flute you have to put it together, and though"
                      " it may seem\n obvious how to fit the three pieces together, there are some things you should"
                      " be aware of.\n\n"
                 # " • BEGINNER FLUTE LESSON 7 : PLAYING YOUR FIRST TUNE\n"
                 # "In this lesson we will learn one more note, then, with the three notes we have learned"
                 # ", we will be able to play some familiar music.The third note we will need to learn is "F":"
                 # "To play this note you will add the first finger from your right hand.Make sure you can play"
                 # " all three notes we have learned so far before you proceed. It is okay to move slowly and"
                 # "take frequent breaks."
                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=28, y=90)


# -----------------------guitar lesson----------------------------------
def guitarlesson():
    tab1 = Toplevel()
    window_width = 1000
    window_height = 350
    screen_width = tab1.winfo_screenwidth()
    screen_height = tab1.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    tab1.geometry("1070x400")
    tab1.resizable(0, 0)
    tab1.title('Guitar Lesson...')
    tab1.iconbitmap('images\\aa.ico')

    cnt1 = Label(tab1, text="Guitar Steps are Being Loaded....", font=("yu gothic ui bold", 16, 'bold'),
                 fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt1.place(x=400, y=20)

    cnt2 = Label(tab1,
                 text=" • How to Play Guitar: 12 Steps to Playing the Guitar"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=28, y=70)

    cnt2 = Label(tab1,
                 text=
                 "1. Choose between an acoustic and electric guitar\n"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=110)
    cnt2 = Label(tab1,
                 text="2. Get to know the guitar parts"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=130)
    cnt2 = Label(tab1,
                 text=
                 "3. Learn how to hold the guitar"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=150)
    cnt2 = Label(tab1,
                 text=
                 "4. Learn the guitar strings and fretboard"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=170)
    cnt2 = Label(tab1,
                 text=
                 "5. Tune your guitar"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=190)
    cnt2 = Label(tab1,
                 text=
                 "6. Play basic guitar chords\n"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=210)
    cnt2 = Label(tab1,
                 text=
                 "7. Learn how to strum guitar chords"
                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=230)
    cnt2 = Label(tab1,
                 text=
                 "8. Read guitar tablature "
                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=250)
    cnt2 = Label(tab1,
                 text=
                 "9. Practice picking and using a guitar pick"
                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=270)
    cnt2 = Label(tab1,
                 text=
                 "10. Learn minor and major scales"
                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=290)
    cnt2 = Label(tab1,
                 text=
                 "11. Start playing your favorite songs"
                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=310)
    cnt2 = Label(tab1,
                 text=
                 "12. Practice, practice, practice"
                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=330)


# ----------------------------piano lesson
def pianolesson():
    tab2 = Toplevel()
    window_width = 1000
    window_height = 350
    screen_width = tab2.winfo_screenwidth()
    screen_height = tab2.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    tab2.geometry("1070x350")
    tab2.resizable(0, 0)
    tab2.title('Piano Lesson...')
    tab2.iconbitmap('images\\aa.ico')

    cnt1 = Label(tab2, text="Piano Steps are Being Loaded...", font=("yu gothic ui bold", 16, 'bold'),
                 fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt1.place(x=400, y=20)
    cnt2 = Label(tab2,
                 text="•How to Play Piano in 8 Easy Steps "

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=75)
    cnt2 = Label(tab2,
                 text=
                 "1: Learn the layout of the piano keyboard\n"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=110)
    cnt2 = Label(tab2,
                 text="2: Start to play piano with the right hand"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=130)
    cnt2 = Label(tab2,
                 text=
                 "3: Practice playing piano with your left hand"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=152)
    cnt2 = Label(tab2,
                 text=
                 "4: Play piano with two hands"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=174)
    cnt2 = Label(tab2,
                 text=
                 "5: Learn to play piano chords"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=196)
    cnt2 = Label(tab2,
                 text=
                 "6: Start learning a piano song with chords"

                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=218)
    cnt2 = Label(tab2,
                 text=
                 "7: Play the tune"
                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=240)
    cnt2 = Label(tab2,
                 text=
                 "8: Practice, practice, practice"
                 , font=("yu gothic ui bold", 12, 'bold'), fg="Black",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=33, y=260)


def submittedreview():
    if reviewentry.get() == "":
        messagebox.showerror('Error','Cannot Submit an empty review')
    else:
        try:
            con = pymysql.Connect(host='localhost', user='root', password='aryan123', database='bandtribe')
            mycursor = con.cursor()
            messagebox.showinfo('Success','Review Submitted Successfully')
        except:
            messagebox.showerror('Error', 'database connectivity issue,please Try Again')
            return
        query = 'insert into review(review)values(%s)'
        mycursor.execute(query, (reviewentry.get()))
        con.commit()
        con.close()
        print("success")


def pastreview():
    tab3 = Toplevel()
    window_width = 1000
    window_height = 350
    screen_width = tab3.winfo_screenwidth()
    screen_height = tab3.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    tab3.geometry("1070x450")
    tab3.resizable(0, 0)
    tab3.title('Reviews...')
    tab3.iconbitmap('images\\aa.ico')

    cnt1 = Label(tab3, text="Please Wait ! Past Reviews are Being Loaded...", font=("yu gothic ui bold", 16, 'bold'),
                 fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt1.place(x=300, y=20)
    cnt2 = Label(tab3, text=" • Past fed Reviews Data", font=("yu gothic ui bold", 12, 'bold'), fg="#89898b",
                 borderwidth=0, cursor='hand2')
    cnt2.place(x=28, y=90)

    # style = ttk.Style(tab0)
    # style.configure("Treeview" , rowheight ="38")

    tree = ttk.Treeview(tab3, columns=(0,1), show='headings', height="7")
    tree.place(x=30, y=120, #width=1000,
                height=270)

    tree.heading(0, text="Review Rating")
    tree.heading(1, text="------------Submitted Reviews------------")
    tree.column(0, width=200, anchor='c')
    tree.column(1, width = 800 , anchor='c')

    try:
        con = pymysql.Connect(host='localhost', user='root', password='aryan123', database='bandtribe')
        mycursor = con.cursor()

    except:
        messagebox.showerror('Error', 'database connectivity issue,please Try Again')
        return
    query = 'select reviewno,review from review'
    mycursor.execute(query)
    con.commit()
    con.close()
    print("success")
    i = 0
    for r in mycursor:
        tree.insert("", 'end', values=(random.randint(0,5),r[1]))
        i = i + 1

    # tree.column(0, width=100, anchor=tk.CENTER)
    # tree.column(1, width=100, anchor=tk.CENTER)
    # tree.column(2, width=100, anchor=tk.CENTER)
    # tree.column(3, width=100, anchor=tk.CENTER)
    # tree.column(4, width=100, anchor=tk.CENTER)


# ---------------your profile---------------------

profile_button = Button(LWUPage, text='YourProfile', font=("yu gothic ui bold", 12, 'bold'), bg='#f8f8f8', fg="#89898b",
                        borderwidth=0, command=showprofile, activebackground='white', cursor='hand2')
profile_button.place(x=1130, y=121)

Lessontitle_button = Button(LWUPage, text=' • Lessons', font=("yu gothic ui bold", 17, 'bold'),
                            bg='#f8f8f8', fg="#1b87d2",
                            borderwidth=0, activebackground='white', cursor='hand2')
Lessontitle_button.place(x=730, y=230)

flutetitle_button = Button(LWUPage, text=' • Beginner - Flute Lessons', font=("yu gothic ui bold", 13, 'bold'),
                           bg='#f8f8f8', fg="black",
                           borderwidth=0, command=flutelesson, activebackground='white', cursor='hand2')
flutetitle_button.place(x=750, y=270)

guitartitle_button = Button(LWUPage, text=' • Steps to Play Guitar', font=("yu gothic ui bold", 13, 'bold'),
                            bg='#f8f8f8', fg="black",
                            borderwidth=0, command=guitarlesson, activebackground='white', cursor='hand2')
guitartitle_button.place(x=750, y=299)

pianotitle_button = Button(LWUPage, text=' • Steps to Play Piano', font=("yu gothic ui bold", 13, 'bold'),
                           bg='#f8f8f8', fg="black",
                           borderwidth=0, command=pianolesson, activebackground='white', cursor='hand2')
pianotitle_button.place(x=750, y=329)

reviewtitle_button = Button(LWUPage, text=' • Write a Review ?', font=("yu gothic ui bold", 17, 'bold'),
                            bg='#f8f8f8', fg="#1b87d2",
                            borderwidth=0, activebackground='white', cursor='hand2')
reviewtitle_button.place(x=730, y=363)

reviewentry = Entry(design_frame16, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
reviewentry.place(x=90, y=310, width=400, height=90)
reviewentry.config(highlightbackground="black", highlightcolor="black")

submitreview = Button(design_frame16, fg='black', bg='#f8f8f8', text='Submit', bd=0, font=("yu gothic ui bold", 13),
                      command=submittedreview, cursor='hand2')
submitreview.place(x=90, y=405, width=90, height=30)

seepastreview = Button(design_frame16, fg='#1b87d2', bg='#f8f8f8', text='See Past Reviews >>', bd=0,
                       command=pastreview,
                       font=("yu gothic ui bold", 12),
                       cursor='hand2')
seepastreview.place(x=320, y=405, width=190, height=30)

# profile_line = Canvas(ArtistPage, width=90, height=2, bg='#1b87d2')
# profile_line.place(x=1145, y=150)
# ===== profile icon =========
profile_icon = Image.open('images\\name-icon.png')
photo = ImageTk.PhotoImage(profile_icon)
profileIcon_label = Label(design_frame16, image=photo, bg='#f8f8f8')
profileIcon_label.image = photo
profileIcon_label.place(x=550, y=17)

# ==============Exit Button============
exitBtn = Button(design_frame16, fg='#89898b', bd=0, text='Exit', bg='#f8f8f8', font=("yu gothic ui bold", 12),
                 cursor='hand2', activebackground='White', command=Exit)
exitBtn.place(x=250, y=470)
# ========= Buttons ===============
Instrument_button = Button(LWUPage, text='Instrument', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                           command=lambda: show_frame(InstrumentPage), borderwidth=0, activebackground='white',
                           cursor='hand2')
Instrument_button.place(x=835, y=175)

# =============Event Button ========
Event_button = Button(LWUPage, text='Event', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='white', command=lambda: show_frame(EventPage), cursor='hand2')
Event_button.place(x=950, y=175)

# ===== Welcome Label ==============
welcome_label = Label(design_frame16, text='BANDTribe', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=210, y=15)

# ======= top Artist Button =========
Artist_button = Button(LWUPage, text='Artist', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(ArtistPage), borderwidth=0, activebackground='white', cursor='hand2')
Artist_button.place(x=760, y=175)

# ==========================lwu BUTTON=============
LWU_button = Button(LWUPage, text='LearnWithUs', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                    borderwidth=0, activebackground='white', cursor='hand2')
LWU_button.place(x=1025, y=175)
LWU_line = Canvas(LWUPage, width=95, height=5, bg='#1b87d2')
LWU_line.place(x=1027, y=203)

# ==========================About BUTTON=============
About_button = Button(LWUPage, text='About', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      command=lambda: show_frame(AboutPage),
                      borderwidth=0, activebackground='white', cursor='hand2')
About_button.place(x=1145, y=175)

# ===== picture icon =========
picture_icon = Image.open('images\\pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame16, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=130, y=5)
#
# ===== Left Side Picture ============
side_image = Image.open('images\\btlogo1copy.jpg')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame15, image=photo, bd=0)
side_image_label.image = photo
side_image_label.place(x=110, y=19)

# =====================================================================================================================
# =====================================================================================================================
# ==================== About PAGE FRAME =====================================================================================
# =====================================================================================================================
# =====================================================================================================================

design_frame17 = Listbox(AboutPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame17.place(x=0, y=0)

design_frame18 = Listbox(AboutPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame18.place(x=676, y=0)

design_frame19 = Listbox(AboutPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame19.place(x=75, y=106)

design_frame20 = Listbox(AboutPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame20.place(x=676, y=106)

# ---------------your profile---------------------

profile_button = Button(AboutPage, text='YourProfile', font=("yu gothic ui bold", 12, 'bold'), bg='#f8f8f8',
                        fg="#89898b",
                        borderwidth=0, command=showprofile, activebackground='white', cursor='hand2')
profile_button.place(x=1130, y=121)

# profile_line = Canvas(ArtistPage, width=90, height=2, bg='#1b87d2')
# profile_line.place(x=1145, y=150)
# ===== profile icon =========
profile_icon = Image.open('images\\name-icon.png')
photo = ImageTk.PhotoImage(profile_icon)
profileIcon_label = Label(design_frame20, image=photo, bg='#f8f8f8')
profileIcon_label.image = photo
profileIcon_label.place(x=550, y=17)

# =========================TEXT BOX=======================

# ===== Welcome Label ==============
text_label = Label(design_frame20, text='BANDTribe is a Social Collaboration App that Allows Users to '
                   , font=("yu gothic ui bold", 12,), bg='#f8f8f8', fg="black",
                   borderwidth=0, activebackground='white', cursor='hand2')
text_label.place(x=86, y=140)
text_label1 = Label(design_frame20, text='Interact/Collaborate with each others based on Skills '
                                         'If two or'
                    , font=("yu gothic ui bold", 12,), bg='#f8f8f8', fg="black",
                    borderwidth=0, activebackground='white', cursor='hand2')
text_label1.place(x=86, y=165)
text_label2 = Label(design_frame20, text='more users wants to collab with each other they are then able '
                    , font=("yu gothic ui bold", 12,), bg='#f8f8f8', fg="black",
                    borderwidth=0, activebackground='white', cursor='hand2')
text_label2.place(x=86, y=190)
text_label3 = Label(design_frame20, text='to drop requests through the app.While deciding, '
                                         'BANDTribe'
                    , font=("yu gothic ui bold", 12,), bg='#f8f8f8', fg="black",
                    borderwidth=0, activebackground='white', cursor='hand2')
text_label3.place(x=86, y=215)
text_label4 = Label(design_frame20, text='users are able to view selected Selected Skills of their potential '
                    , font=("yu gothic ui bold", 12,), bg='#f8f8f8', fg="black",
                    borderwidth=0, activebackground='white', cursor='hand2')
text_label4.place(x=86, y=215)
text_label5 = Label(design_frame20, text=
'match , alongside a short bio.'
'With its basis in Skills it dispenses'
                    , font=("yu gothic ui bold", 12,), bg='#f8f8f8', fg="black",
                    borderwidth=0, activebackground='white', cursor='hand2')
text_label5.place(x=86, y=240)
text_label6 = Label(design_frame20, text=
'with the complex algorithms '
'utilized by other apps and reduces'
                    , font=("yu gothic ui bold", 12,), bg='#f8f8f8', fg="black",
                    borderwidth=0, activebackground='white', cursor='hand2')
text_label6.place(x=86, y=265)
text_label7 = Label(design_frame20, text=
'it to simplest level that'
' you might find for Showing your Talent.'
                    , font=("yu gothic ui bold", 12,), bg='#f8f8f8', fg="black",
                    borderwidth=0, activebackground='white', cursor='hand2')
text_label7.place(x=86, y=290)
text_label8 = Label(design_frame20, text=
'The app is currently in Development Stage !!'
                    , font=("yu gothic ui bold", 12,), bg='#f8f8f8', fg="black",
                    borderwidth=0, activebackground='white', cursor='hand2')
text_label8.place(x=86, y=315)
text_label9 = Label(design_frame20, text=
'                                         '
'                                      ~Team BANDTribe'
                    , font=("yu gothic ui bold", 12,), bg='#f8f8f8', fg="#1b87d2",
                    borderwidth=0, activebackground='white', cursor='hand2')
text_label9.place(x=86, y=350)
# ==============Back Button============
backBtn = Button(design_frame20, fg='#89898b', bd=0, text='Return to HomePage | ', bg='#f8f8f8',
                 font=("yu gothic ui bold", 12),
                 cursor='hand2', activebackground='White', command=Back)
backBtn.place(x=80, y=470)

# ==============Exit Button============
exitBtn = Button(design_frame20, fg='#89898b', bd=0, text='Exit', bg='#f8f8f8', font=("yu gothic ui bold", 12),
                 cursor='hand2', activebackground='White', command=Exit)
exitBtn.place(x=250, y=470)

# ========= Buttons ===============
Instrument_button = Button(AboutPage, text='Instrument', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                           command=lambda: show_frame(InstrumentPage), borderwidth=0, activebackground='white',
                           cursor='hand2')
Instrument_button.place(x=835, y=175)

# =============Event Button ========
Event_button = Button(AboutPage, text='Event', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='white', command=lambda: show_frame(EventPage), cursor='hand2')
Event_button.place(x=950, y=175)

# ===== Welcome Label ==============
welcome_label = Label(design_frame20, text='BANDTribe', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=210, y=15)

# ==========================lwu BUTTON=============
LWU_button = Button(AboutPage, text='LearnWithUs', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                    command=lambda: show_frame(LWUPage),
                    borderwidth=0, activebackground='white', cursor='hand2')
LWU_button.place(x=1025, y=175)

# ==========================About BUTTON=============
About_button = Button(AboutPage, text='About', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      command=lambda: show_frame(AboutPage),
                      borderwidth=0, activebackground='white', cursor='hand2')
About_button.place(x=1145, y=175)
About_line = Canvas(AboutPage, width=57, height=5, bg='#1b87d2')
About_line.place(x=1142, y=203)

# ======= top Artist Button =========
Artist_button = Button(AboutPage, text='Artist', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(ArtistPage), borderwidth=0, activebackground='white', cursor='hand2')
Artist_button.place(x=760, y=175)

# ===== picture icon =========
picture_icon = Image.open('images\\pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame20, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=130, y=5)
#
# ===== Left Side Picture ============
side_image = Image.open('images\\btlogo1copy.jpg')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame19, image=photo, bd=0)
side_image_label.image = photo
side_image_label.place(x=110, y=19)

# =====================================================================================================================
# =====================================================================================================================
# ==================== DATABASE CONNECTION ============================================================================
# =====================================================================================================================
# =====================================================================================================================


window_1.mainloop()
