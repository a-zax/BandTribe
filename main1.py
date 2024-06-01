from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import ImageTk, Image
import tk as tk


################################################################
def connect_database():
    if name_entry.get() == '' or phone_entry.get() == '' or email_entry.get == '' or type_entry.get() == '' or \
            specialist_entry.get() == '' or password_entry2.get() == '':
        messagebox.showerror('Error', 'All fields are Required')
    # elif password_entry2.cget() != confirmEntry.cget():
    #     # print("hello")
    #     messagebox.showerror('Error','password mismatch')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='AshishIT45')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'database connectivity issue, please Try Again')
            return

        query = 'create database userdata'
        mycursor.execute(query)
        query = 'use userdata'
        mycursor.execute(query)
        query = 'create table data()'


################################################################

def login():
    window.destroy()
    import HomePage


# if email_entry.cget('a') and password_entry1.cget('w'):

# window.withdraw()
# if email_entry.get() == '' and password_entry1.get() == '':
#     messagebox.showerror('Error','Field cannot be empty')
# else:
#     messagebox.showerror('Error','Enter Valid Credentials')


window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')
# window.geometry('1350x740+50+50')
window.resizable(0, 0)
window.title('BANDTribe Login/Signup Page')

# Window Icon Photo
icon = PhotoImage(file='images\\pic-icon.png')
window.iconphoto(True, icon)

LoginPage = Frame(window)
RegistrationPage = Frame(window)

for frame in (LoginPage, RegistrationPage):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(LoginPage)

# =====================================================================================================================
# =====================================================================================================================
# ==================== LOGIN PAGE =====================================================================================
# =====================================================================================================================
# =====================================================================================================================

design_frame1 = Listbox(LoginPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame1.place(x=0, y=0)

design_frame2 = Listbox(LoginPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame2.place(x=676, y=0)

design_frame3 = Listbox(LoginPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame3.place(x=75, y=106)

design_frame4 = Listbox(LoginPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame4.place(x=676, y=106)

# ====== Email ====================
# con=mysql.connector.connect(host="localhost",user="root",password="AshishIT45",database="bandtribe")
# cur=con.cursor(buffered=True)
# try:
# cur.execute("describe login")
# except:
#  cur.execute("create table login(id int primary key auto_increment,email varchar(100),password varchar(20)")

# def login():
# cur.execute("insert in to login(email,password )values ('{email_entry()}','{password_entry1()}')")

email_entry = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
email_entry.place(x=134, y=170, width=256, height=34)
email_entry.config(highlightbackground="black", highlightcolor="black")
email_label = Label(design_frame4, text='• Email account', fg="#89898b", bg='#f8f8f8',
                    font=("yu gothic ui", 11, 'bold'))
email_label.place(x=130, y=140)

# ==== Password ==================
password_entry1 = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
password_entry1.place(x=134, y=250, width=256, height=34)
password_entry1.config(highlightbackground="black", highlightcolor="black")
password_label = Label(design_frame4, text='• Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
password_label.place(x=130, y=220)


# function for show and hide password
def password_command():
    if password_entry1.cget('show') == '•':
        password_entry1.config(show='')
    else:
        password_entry1.config(show='•')


# ====== checkbutton ==============
checkButton = Checkbutton(design_frame4, bd=0, bg='#f8f8f8', command=password_command, font=("yu gothic ui bold", 10),
                          text='Show Password')
checkButton.place(x=132, y=288)

# ========= Buttons ===============
SignUp_button = Button(LoginPage, text='Sign up', font=("yu gothic ui bold", 12, 'bold'), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='WHITE',
                       cursor='hand2')
SignUp_button.place(x=1100, y=165)
info_label1 = Label(design_frame4, text='(Only for new users)', font=("yu gothic ui bold", 10, 'bold'), fg="#89898b",
                    bg='#f8f8f8')
info_label1.place(x=390, y=92)

# ===== Welcome Label ==============
welcome_label = Label(design_frame4, text='BANDTribe', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=210, y=15)

# ======= top Login Button =========
login_button = Button(LoginPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='WHITE', cursor='hand2')
login_button.place(x=845, y=165)

login_line = Canvas(LoginPage, width=60, height=5, bg='#1b87d2')
login_line.place(x=840, y=193)

# ==== LOGIN  down button ============
loginBtn1 = Button(design_frame4, fg='#f8f8f8', text='Login', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2', activebackground='#1b87d2', command=login)
loginBtn1.place(x=133, y=340, width=256, height=50)

# SignUp_button = Button(RegistrationPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
#                        command=lambda: show_frame(LoginPage), borderwidth=0, activebackground='WHITE', cursor='hand2')
# SignUp_button.place(x=1100, y=175)

# ======= ICONS =================

# ===== Email icon =========
email_icon = Image.open('images\\email-icon.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
emailIcon_label.image = photo
emailIcon_label.place(x=100, y=174)

# ===== password icon =========
password_icon = Image.open('images\\pass-icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
password_icon_label.image = photo
password_icon_label.place(x=100, y=254)

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


# ===================================================================================================================
# ===================================================================================================================
# === FORGOT PASSWORD  PAGE =========================================================================================
# ===================================================================================================================
# ===================================================================================================================


def forgot_password():
    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title('Forgot Password')
    win.iconbitmap('images\\aa.ico')
    win.configure(background='#f8f8f8')
    win.resizable(0, 0)

    # ====== Email ====================
    email_entry2 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
    email_entry2.place(x=40, y=30, width=256, height=34)
    email_entry2.config(highlightbackground="black", highlightcolor="black")
    email_label2 = Label(win, text='• Email account', fg="#89898b", bg='#f8f8f8',
                         font=("yu gothic ui", 11, 'bold'))
    email_label2.place(x=40, y=0)

    # ====  New Password ==================
    new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    new_password_entry.place(x=40, y=110, width=256, height=34)
    new_password_entry.config(highlightbackground="black", highlightcolor="black")
    new_password_label = Label(win, text='• New Password', fg="#89898b", bg='#f8f8f8',
                               font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=80)

    # ====  Confirm Password ==================
    confirm_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•',
                                   highlightthickness=2)
    confirm_password_entry.place(x=40, y=190, width=256, height=34)
    confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
    confirm_password_label = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                                   font=("yu gothic ui", 11, 'bold'))
    confirm_password_label.place(x=40, y=160)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1b87d2', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#1b87d2')
    update_pass.place(x=40, y=240, width=256, height=50)


forgotPassword = Button(design_frame4, text='Forgot Password ?', font=("yu gothic ui", 10, "bold"), bg='#f8f8f8',
                        borderwidth=0, activebackground='#f8f8f8', fg='blue', command=lambda: forgot_password(),
                        cursor="hand2")
forgotPassword.place(x=276, y=288)

# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================


# =====================================================================================================================
# =====================================================================================================================
# ==================== REGISTRATION PAGE ==============================================================================
# =====================================================================================================================
# =====================================================================================================================

design_frame5 = Listbox(RegistrationPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame5.place(x=0, y=0)

design_frame6 = Listbox(RegistrationPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame6.place(x=676, y=0)

design_frame7 = Listbox(RegistrationPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame7.place(x=75, y=106)

design_frame8 = Listbox(RegistrationPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame8.place(x=676, y=106)


# ==== Full Name =======

def on_entry(e):
    name_entry.delete(0, 'end')


def on_leave(e):
    if name_entry.get() == '':
        name_entry.insert(0, 'Name')


name_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
name_entry.place(x=134, y=100, width=170, height=34)
name_entry.insert(0, 'Name')
name_entry.bind("<FocusIn>", on_entry)
name_entry.bind("<FocusOut>", on_leave)
name_entry.config(highlightbackground="black", highlightcolor="black")


# ==== PHONE NO =======
def on_enter(e):
    phone_entry.delete(0, 'end')


def on_leave(e):
    if phone_entry.get() == '':
        phone_entry.insert(0, 'PhoneNo')


phone_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
phone_entry.place(x=310, y=100, width=110, height=34)
phone_entry.bind("<FocusIn>", on_enter)
phone_entry.bind("<FocusOut>", on_leave)
phone_entry.insert(0, 'Phone No')
phone_entry.config(highlightbackground="black", highlightcolor="black")


# ======= Email ===========
def on_enter(e):
    email_entry.delete(0, 'end')


def on_leave(e):
    if email_entry.get() == '':
        email_entry.insert(0, 'Email')


email_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
email_entry.place(x=134, y=140, width=286, height=34)
email_entry.bind("<FocusIn>", on_enter)
email_entry.bind("<FocusOut>", on_leave)
email_entry.insert(0, 'Email')
email_entry.config(highlightbackground="black", highlightcolor="black")

# ======= type===========
type_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
type_entry.place(x=134, y=210, width=286, height=34)
type_entry.config(highlightbackground="black", highlightcolor="black")
type_label = Label(design_frame8, text='•Type of Artist (i.e. Singer,Comedian,Dancer)', fg="#89898b", bg='#f8f8f8',
                   font=("yu gothic ui", 11, 'bold'))
type_label.place(x=130, y=185)
# ====== specialist_entry  =============
specialist_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
specialist_entry.place(x=134, y=278, width=286, height=34)
specialist_entry.config(highlightbackground="black", highlightcolor="black")
specialist_label = Label(design_frame8, text='• Type of Instrument you Play (i.e Flute,Guitar,Piano)', fg="#89898b",
                         bg='#f8f8f8',
                         font=("yu gothic ui", 11, 'bold'))
specialist_label.place(x=130, y=250)


# ====== Password =========

def on_enter(e):
    password_entry2.delete(0, 'end')


def on_leave(e):
    if password_entry2.get() == '':
        password_entry2.insert(0, ' Password')


password_entry2 = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
password_entry2.place(x=134, y=350, width=286, height=34)
password_entry2.bind("<FocusIn>", on_enter)
password_entry2.bind("<FocusOut>", on_leave)
password_entry2.insert(0, 'Password')
password_entry2.config(highlightbackground="black", highlightcolor="black")
password_label = Label(design_frame8, text='• Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
password_label.place(x=130, y=320)


#
# # ====== confirm-Password =========
# def on_enter(e):
#    confirmEntry.delete(0,'end')
#
# def on_leave(e):
#     if confirmEntry.get()=='':
#        confirmEntry.insert(0,' Password')
#
#
#
# confirmEntry= Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
# confirmEntry.place(x=134, y=402, width=286, height=34)
# confirmEntry.bind("<FocusIn>",on_enter)
# confirmEntry.bind("<FocusOut>",on_leave)
# confirmEntry.insert(0,'Password')
# confirmEntry.config(highlightbackground="black", highlightcolor="black")
# confirmEntry.config(highlightbackground="black", highlightcolor="black")


def password_command2():
    if password_entry2.cget('show') == '•':
        password_entry2.config(show='')
        # confirmEntry.config(show='')

    else:
        password_entry2.config(show='•')
        # confirmEntry.config(show='•')


# def password_command3():
#     if password_entry2.cget()!=confirmEntry.cget():
#         messagebox.showerror('error','Password doesnt match ')
#     else:
#         messagebox.showinfo('good','passwords are equal')


checkButton = Checkbutton(design_frame8, bd=0, bg='#f8f8f8', font=("yu gothic ui semibold", 10),
                          command=password_command2, text='Show Password')
checkButton.place(x=132, y=390)

# ========= Buttons ====================
SignUp_button = Button(RegistrationPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(LoginPage), borderwidth=0, activebackground='WHITE', cursor='hand2')
SignUp_button.place(x=1100, y=165)

SignUp_line = Canvas(RegistrationPage, width=60, height=5, bg='#1b87d2')
SignUp_line.place(x=1100, y=193)

# ===== Welcome Label ==================
welcome_label = Label(design_frame8, text='BANDTribe', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=210, y=15)

# ========= Login Button =========
login_button = Button(RegistrationPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='WHITE', command=lambda: show_frame(LoginPage), cursor='hand2')
login_button.place(x=845, y=165)

# ==== SIGN UP down button ============
signUp2 = Button(design_frame8, fg='#f8f8f8', text='Sign Up', bg='#1b87d2', font=("yu gothic ui bold", 15),
                 cursor='hand2', activebackground='#1b87d2', command=connect_database)
signUp2.place(x=135, y=420, width=286, height=50)

# ===== password icon =========
password_icon = Image.open('images\\pass-icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
password_icon_label.image = photo
password_icon_label.place(x=100, y=350)
#
# # ===== confirm password icon =========
# confirmEntry_icon = Image.open('images\\pass-icon.png')
# photo = ImageTk.PhotoImage(confirmEntry_icon)
# confirmPassword_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
# confirmPassword_icon_label.image = photo
# confirmPassword_icon_label.place(x=100, y=402)
#
# ===== Email icon =========
email_icon = Image.open('images\\email-icon.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
emailIcon_label.image = photo
emailIcon_label.place(x=100, y=140)

# ===========specialist-icon=========#
specialist_entry = Image.open('images\\download (1).png')
photo = ImageTk.PhotoImage(specialist_entry)
specialist_entry = Label(design_frame8, image=photo, bg='#f8f8f8')
specialist_entry.image = photo
specialist_entry.place(x=100, y=278)

# ===== Full Name icon =========
name_icon = Image.open('images\\name-icon.png')
photo = ImageTk.PhotoImage(name_icon)
nameIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
nameIcon_label.image = photo
nameIcon_label.place(x=100, y=100)
#

# =====typeicon =========
type_icon = Image.open('images\\name-icon.png')
photo = ImageTk.PhotoImage(name_icon)
typeIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
typeIcon_label.image = photo
typeIcon_label.place(x=100, y=210)

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

# database connection
window.mainloop()
